from fastapi import FastAPI,HTTPException
from pathlib import Path
import json

app = FastAPI()

path=Path(__file__).parent.parent / "data" / "patient.json"
with open(path, "r") as f:
    data = json.load(f)

@app.get("/")
def hello():
    return {"message": "I'm CEO Bitch"}

@app.get("/view/{id}")
def view(id : str ):   
    for patient in data:
        if patient["patient_id"] == id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/patients")
def patient(sort_by : str = None ,order : str = None):

    valid_field=["name","gender","patient_id"]
    if sort_by and sort_by not in valid_field:
       raise HTTPException(status_code=400,detail="Please enter in valid field ['less_age','gender']")
    if order is not None and order not in ["asc","des"]:
        raise HTTPException(status_code=400,detail="Enter valid order('asc','des')")
    if sort_by:
        reverse=order=="des"
        return sorted(data,key=lambda x: x[sort_by],reverse=reverse)
    return data
