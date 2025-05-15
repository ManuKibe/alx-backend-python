import mysql.connector

def stream_users():
    """Generator that yields one user at a time from the user_data table"""
    try:
        # Connect to the ALX_prodev database
        conn = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',
            password='your_mysql_password',
            database='ALX_prodev'
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        # Yield one row at a time using a generator
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close cursor and connection when done
        try:
            cursor.close()
            conn.close()
        except:
            pass
