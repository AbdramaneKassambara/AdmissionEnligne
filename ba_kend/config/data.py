import pymongo
import mysql.connector
#--------------------------------------------connect-Mongoose--------------------------------------------
def connect_to_mongoose():
    try:
        client_mongo = pymongo.MongoClient("mongodb+srv://ak:438462@tp2.6juqutv.mongodb.net/?retryWrites=true&w=majority")
        db_mongo = client_mongo["Admission_Prj"]
        collection_mongo = db_mongo["users"]
        collection_Journal_utilisateur= db_mongo["Journal_Utilisateurs_Mongo"]
        print("\n--------------------------------------\nConnection Reussie MongoDB\n---------------------------------------------------------------")
        return db_mongo, collection_mongo,collection_Journal_utilisateur
    except pymongo.errors.ConnectionFailure as e:
        print(f"Erreur de la Connection: {e}")
        return None, None 
#------------------------------------------------creer table -----------------------------------------------
def create_tables(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Utilisateurs (
                id VARCHAR(255) PRIMARY KEY,
                nom VARCHAR(255),
                prenom VARCHAR(255),
                email VARCHAR(255),
                age INT,
                mot_2_passe VARCHAR(255)
            );
        """
        cursor.execute(create_table_query)
        print("La table 'Utilisateurs' a été créée avec succès.")
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Journal_Utilisateurs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                action_type VARCHAR(10),
                table_name VARCHAR(255),
                id_data VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_query)
        print("La table 'Journal_Utilisateurs' a été créée avec succès.")
        cursor.close()
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Erreur lors de la création des tables : {e}")
#-------------------------------------------------------------connected-Mysql---------------------------------------
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="users"
        )
        if conn.is_connected():
            print("\n--------------------------------------\nConnection Reussie MySQL\n---------------------------------------------------------------")
            create_tables(conn)
            return conn
        else:
            print("Impossible de se connecter à MySQL.")
            return None
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None