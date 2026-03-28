#exersice 1
import requests
def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            joke_text = json_data["value"]
            print("Random Chuck Norris Joke:")
            print("-" * 25)
            print(joke_text)
        else:
            print("Error: Could not retrieve data from server.")
    except requests.exceptions.RequestException:
        print("Error: A network problem occurred.")
get_random_joke()

#Exwrsice 2
import requests
def get_weather():
    api_key = "05b0a40795a91c13c4ca9d3626faceb5"
    city = input("Enter city name:")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            print(f"Weather in {city}: {description}")
            print(f"Temperature : {temp} °C")
        else:
            print("Error: City not found or API key not active yet.")
    except requests.exceptions.RequestException:
        print("Network error!")
get_weather()
