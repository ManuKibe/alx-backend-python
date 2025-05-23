
#!/usr/bin/python3
import mysql.connector
import csv
import uuid
from mysql.connector import Error


def connect_db():
   
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password"  # Replace with your MySQL root password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
   
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists.")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",  # Replace with your MySQL root password
            database="ALX_prodev"
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
  
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX (user_id)
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):

    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            inserted = 0
            for row in reader:
                user_id = row.get('user_id') or str(uuid.uuid4())
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (user_id,))
                if cursor.fetchone():
                    continue  # skip if record exists

                insert_query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                    user_id,
                    row['name'],
                    row['email'],
                    row['age']
                ))
                inserted += 1

            connection.commit()
        cursor.close()
        print(f"{inserted} rows inserted into user_data")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except Error as e:
        print(f"Error inserting data: {e}")
