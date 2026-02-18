#module 8
#exercise 1
import mysql.connector
icao = input("Enter ICAO code: ")
connection = mysql.connector.connect(
    host="localhost",
    user="zahra",
    passwd="1234",
    database="flight_game"
)
cursor = connection.cursor()
sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao,))
result = cursor.fetchone()
if result:
    print("Airport:", result[0])
    print("City:", result[1])
else:
    print("Airport not found.")
cursor.close()
connection.close()

#EXERCISE 2
import mysql.connector
country = input("Enter country code (e.g. FI): ")
connection = mysql.connector.connect(
    host="localhost",
    user="zahra",
    passwd="1234",
    database="flight_game"
)
cursor = connection.cursor()
sql = """SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type"""
cursor.execute(sql, (country,))
result = cursor.fetchall()
for row in result:
    print(row[1], "-", row[0])
cursor.close()
connection.close()

#exercise3
import mysql.connector
from geopy.distance import geodesic
icao1 = input("Enter first ICAO code: ")
icao2 = input("Enter second ICAO code: ")
connection = mysql.connector.connect(
    host="localhost",
    user="zahra",
    passwd="1234",
    database="flight_game"
)
cursor = connection.cursor()
sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
cursor.execute(sql, (icao1,))
result1 = cursor.fetchone()
cursor.execute(sql, (icao2,))
result2 = cursor.fetchone()
if result1 and result2:
    coords1 = (result1[0], result1[1])
    coords2 = (result2[0], result2[1])
    distance = geodesic(coords1, coords2).kilometers
    print("Distance:", round(distance, 2), "km")
else:
    print("One or both airports not found.")
cursor.close()
connection.close()




