import datetime
from mysqlx import Error
import pymongo
from config.data import connect_to_mysql,connect_to_mongoose
import uuid
#----------------------------------------------MYSQL--------------------------------------------------------
def generate_unique_id():
    return str(uuid.uuid4())
def insert_data_mysql(data):
    unique_id = generate_unique_id()
    try:
        db_mysql = connect_to_mysql()
        if db_mysql is not None:
            cursor = db_mysql.cursor()
            insert_query = "INSERT INTO Utilisateurs (id, nom, prenom, email, age, mot_2_passe) VALUES (%s, %s, %s, %s, %s, %s)"
            if isinstance(data, list):
                inserted_ids = []
                for values in data:
                    values["id"] = unique_id
                    cursor.execute(insert_query, (values["id"], values["nom"], values["prenom"], values["email"], values["age"], values["mot_2_passe"]))
                    db_mysql.commit()
                    # Insérer dans le journal
                    cursor.execute("INSERT INTO Journal_Utilisateurs (action_type, table_name, id_data) VALUES ('INSERT', 'Utilisateurs', %s)", (unique_id,))
                    db_mysql.commit()
                    inserted_ids.append(unique_id)
                cursor.close()
                db_mysql.close()
                print(f"{len(data)} enregistrements insérés avec succès dans MySQL.")
                return inserted_ids
            else:
                data["id"] = unique_id
                cursor.execute(insert_query, (data["id"], data["nom"], data["prenom"], data["email"], data["age"], data["mot_2_passe"]))
                db_mysql.commit()
                # Insérer dans le journal
                cursor.execute("INSERT INTO Journal_Utilisateurs (action_type, table_name, id_data) VALUES ('INSERT', 'Utilisateurs', %s)", (unique_id,))
                db_mysql.commit()
                cursor.close()
                db_mysql.close()
                print("1 enregistrement inséré avec succès dans MySQL.")
                return [unique_id]
        else:
            print("Impossible de se connecter à la base de données MySQL.")
            return []
    except Error as e:
        print(f"Erreur lors de l'insertion des enregistrements dans MySQL : {e}")
        return []
#------------------------------------------------------MONGOOSE----------------------------------------------------------------------------------------------------
def insert_data_mongoose(data):
    unique_id = generate_unique_id()
    try:
        db_mongo, collection_mongo,collection_Journal_utilisateur = connect_to_mongoose()
        if db_mongo is not None:
            if isinstance(data, list):
                inserted_ids = []
                for record in data:
                    # l'ID généré
                    record["_id"] = unique_id
                    result = collection_mongo.insert_one(record)
                    inserted_ids.append(unique_id)
                    # Journalisation de l'insertion
                    log_entry = {
                        "action_type": "INSERT",
                        "table_name": "Utilisateurs",
                        "id_data": unique_id,
                        "timestamp": datetime.datetime.now()
                    }
                    collection_Journal_utilisateur.insert_one(log_entry)
                print(f"{len(data)} enregistrements insérés avec succès dans MongoDB.")
                return inserted_ids
            else:
                # l'ID généré
                data["_id"] = unique_id
                result = collection_mongo.insert_one(data)
                print("1 enregistrement inséré avec succès dans MongoDB.")
                # Journal de l'insertion
                log_entry = {
                    "action_type": "INSERT",
                    "table_name": "Utilisateurs",
                    "id_data": unique_id,
                    "timestamp": datetime.datetime.now()
                }
                collection_Journal_utilisateur.insert_one(log_entry)
                return [unique_id]
        else:
            print("Impossible de se connecter à la base de données MongoDB.")
            return []
    except pymongo.errors.PyMongoError as e:
        print(f"Erreur lors de l'insertion des enregistrements dans MongoDB : {e}")
        return []