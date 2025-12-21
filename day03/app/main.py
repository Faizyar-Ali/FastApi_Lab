from fastapi import FastAPI
import json
from pathlib import Path

app=FastAPI()

@app.get("/")
def root():
    return {"message":"i'm CEO bitch"}


file_path=Path(Path(__file__).parent).parent / "data"/ "schedule.json"
with open(file_path,"r")as f:
        schedule=json.load(f)

@app.get("/trips")
def get_trips(from_city : str = None,to_city : str = None):
    filtered=schedule
    if from_city:
         filtered=[trip for trip in filtered if trip["from"].lower()==from_city.lower()]
    if to_city:
         filtered=[trip for trip in filtered if trip["to"].lower()==to_city.lower()]
    return filtered

