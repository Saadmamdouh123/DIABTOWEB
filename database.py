import psycopg2

conn = psycopg2.connect(
    dbname="DiabData",
    user="postgres",
    password="raja2020",  # ← غيّر كلمة المرور هنا
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        patientid INTEGER,
        result INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
