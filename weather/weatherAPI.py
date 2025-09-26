from fastapi import FastAPI
import requests

app=FastAPI()

api_key="your_openweathermap_api_key"
base_url="http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
def get_weather(city:str):
    params={
        "q":city,
        "appid":api_key,
        "units":"metric"
    }
    response =requests.get(base_url,params=params)

    if response.status_code==200:
        data = response.json()
        return {
            "city":data["name"],
            "temperature":data["main"]["temp"],
            "humidity":data["main"]["humidity"],
            "condition":data["weather"][0]["description"]
        }
    return {"error":"City not found"}

