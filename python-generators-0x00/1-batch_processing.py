import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the user_data table"""
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

        batch = []
        for row in cursor:  # 1st loop
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch  # Yield any remaining users

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25"""
    for batch in stream_users_in_batches(batch_size):  # 2nd loop
        for user in batch:  # 3rd loop
            if user['age'] > 25:
                print(user)
