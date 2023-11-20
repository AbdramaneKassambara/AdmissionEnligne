import mysqlx
import pymongo
from config.data import connect_to_mongoose,connect_to_mysql
from config.CRUD import insert_data_mongoose,insert_data_mysql
data = {
    "nom": "Abdramane",
    "prenom":"kassambara",
    "age": 20,
    "email":"test@gmail.com",
    "mot_2_passe":"1234"
}
def main():
    db_mongo, collection_mongo,collection_Journal_utilisateur = connect_to_mongoose()
    db_mysql = connect_to_mysql()
    if db_mongo is not None and db_mysql is not None:
        try:
            resultat_mongo = insert_data_mongoose(data=data)
            print("Resultat MongoDB insert : ", resultat_mongo)
        except pymongo.errors.PyMongoError as e_mongo:
            print(f"Erreur lors de l'insertion dans MongoDB : {e_mongo}")
        try:
            resultat_mysql = insert_data_mysql(data=data)
            print("Resultat MySQL insert : ", resultat_mysql)
        except mysqlx.connector.Error as e_mysql:
            print(f"Erreur lors de l'insertion dans MySQL : {e_mysql}")
    elif db_mongo is not None:
        try:
            resultat_mongo = insert_data_mongoose(data=data)
            print("Resultat MongoDB insert : ", resultat_mongo)
        except pymongo.errors.PyMongoError as e_mongo:
            print(f"Erreur lors de l'insertion dans MongoDB : {e_mongo}")
    elif db_mysql is not None:
        try:
            resultat_mysql = insert_data_mysql(data=data)
            print("Resultat MySQL insert : ", resultat_mysql)
        except mysqlx.connector.Error as e_mysql:
            print(f"Erreur lors de l'insertion dans MySQL : {e_mysql}")
    else:
        print("Impossible de se connecter à aucune des bases de données.")
