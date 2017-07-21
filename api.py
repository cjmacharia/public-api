import json   #import json
import requests  #import requests


def city():
    """a function that will consume a weather API"""

    print("Welcome to my weather API")

    yourcity = input("Enter A known City name: ")
    api_key = ("077936f695f61908cd19a5a2452a97fb") 
    #our public Api-key 
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={0}&appid=077936f695f61908cd19a5a2452a97fb".format(yourcity, api_key))  #api call
    weather = response.json()
    print("The current weather in {0} is {1}".format(yourcity, weather["weather"][0]["description"]))  #the result

if __name__ == "__main__":
    city()
