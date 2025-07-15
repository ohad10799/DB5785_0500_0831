import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="DB5785_0500_0831",
        user="postgres",
        password="Kahlon7914",
        host="localhost",
        port="5432"
    )

