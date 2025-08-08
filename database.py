import psycopg2

# database.py – Connexion et Initialisation de la Base de Données PostgreSQL
# Ce module configure la connexion à la base de données PostgreSQL et initialise 
# les tables nécessaires au bon fonctionnement de l’application DiabetoWeb.


# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname="DiabData",
    user="postgres",
    password="raja2020",  # ← غيّر كلمة المرور هنا
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Fonction create_tables()
# Cette fonction crée les tables suivantes si elles n'existent pas :

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE,
        email TEXT,
        password TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

# patients
# Stocke les informations cliniques de chaque patient.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id SERIAL PRIMARY KEY,
        doctorid INTEGER,
        name TEXT,
        age INTEGER,
        sex TEXT,
        glucose FLOAT,
        bmi FLOAT,
        bloodpressure FLOAT,
        pedigree FLOAT,
        result INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

# predictions
# Historique des prédictions faites par le modèle ML
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        patientid INTEGER,
        result INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
# Exécution de la création des tables
    conn.commit()
