#Exercise 1

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })

if __name__ == '__main__':
    app.run(debug=True)

#Exercise 2
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/airport/<icao>')
def get_airport(icao):
    connection = mysql.connector.connect(
        host="localhost",
        user="zahra",
        password="1234",
        database="flight_game"
    )

    cursor = connection.cursor()

    icao_code = icao.upper()
    query = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        return jsonify({
            "ICAO": icao_code,
            "Name": result[0],
            "Location": result[1]
        })
    else:
        return jsonify({"error": "Airport not found"})


if __name__ == '__main__':
    app.run(debug=True)
