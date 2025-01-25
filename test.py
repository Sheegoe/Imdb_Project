import psycopg2

def test_db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="Data_warehouse",
            user="postgres",
            password=""
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        connection.close()
        if result:
            print("Database connection successful!")
        else:
            print("Database connection failed!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    test_db_connection()