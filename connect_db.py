import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="zahra",
        password="1234",
        database="flight_game"
    )
    if connection.is_connected():
        print("connection is successful")
except Exception as e:
    print(f"Error: {e}")

