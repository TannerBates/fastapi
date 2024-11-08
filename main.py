from fastapi import FastAPI, HTTPException, Query
import requests
from datetime import date
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#mount the static files directory at the root url
app.mount("/apod/index.html", StaticFiles(directory="static", html=True), name="static")

NASA_API_URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = "<YOUR_API_KEY>" #replace with your API key

#endpoint to fetch todays APOD data
@app.get("/apod/")
async def get_apod(date: date = Query(None, description="Date in YYY-MM-DD format")):

    params = {"api_key": NASA_API_KEY}
    if date:
        params["date"] = date.strftime("%Y-%m-%d")
        

    try:
        #make a request to the NASA APOD API
        response = requests.get(NASA_API_URL, params=params)
        response.raise_for_status()

        #parse json reponse
        apod_data = response.json()
        return {
            "title": apod_data["title"],
            "date": apod_data["date"],
            "explanation": apod_data["explanation"],
            "url": apod_data["url"],
            "media_type": apod_data["media_type"]            
        }

    except requests.RequestException as e: 
        raise HTTPException(status_code=500, detail="NASA API failed request") from e

