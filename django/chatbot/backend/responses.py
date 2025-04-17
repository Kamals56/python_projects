import random
import requests
last_message = []

#1.5 Weather
API_KEY = '3c6ce467fc6f7cff301ebab9d57c4140'
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return f"{temperature}°C"
    else:
        return "Sorry, I couldn't fetch the weather data."


def bot_response(message):
    message = message.lower()
    global last_message

    #1.4 Repeated Message
    if message == last_message:
        return "STOP REPEATING YOURSELF!"
    last_message = message

    #1.1 Initial Message
    if message == "hello":
        return "Hello there humanbeing"
    
    elif message.replace(" ", "") == "goodbye":
        return"short circuit executed"
    #1.2 Images
    elif message == "gimme image":
        seed = random.randint(0, 10000)
        return f'<img src = "https://picsum.photos/seed/{seed}/200/300" alt="Random Image" />'
    #1.3 Wikipedia Search
    elif message.startswith("tell me about"):
        topic = message[14:]
        return f'<a href="https://en.wikipedia.org/wiki/{topic}" target="_blank">Wikipedia article about {topic}</a>'
    #1.5 Weather
    elif message.startswith("weather in"):
        city = message[11:]

        weather = get_weather(city)
        return f"Weather in {city} is {weather}."
    #1.6 help
    elif message == "help":
        return f"1. when you send gimme image chatbot gives a random new image everytime. \n 2. if you want to know weather of any city then simply write weather in <city name>. \n 3.if you would like to know about anything then then write tell me about <topic> then, chatbot will give you the link to the wikipedia article about it"
    

    else:
        return"Cannot comprehend"
    

