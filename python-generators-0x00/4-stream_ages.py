from seed import connect_to_prodev

def stream_user_ages():
    """Generator that yields user ages one by one"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()


def calculate_average_age():
    """Calculate average age using the generator with memory efficiency"""
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No user data found.")


# Run the function
if __name__ == "__main__":
    calculate_average_age()
