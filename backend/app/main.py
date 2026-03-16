
from fastapi import FastAPI
app = FastAPI(title="County Waste Management API")

@app.get("/")
def root():
    return {"message": "County Waste Management API running"}
