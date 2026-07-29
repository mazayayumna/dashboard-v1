from fastapi import FastAPI
from services.who_services import WHOService

app = FastAPI()

@app.get("/get-indicators")
def test_who():
    service = WHOService()
    return service.get_indicators()[:5]

@app.get("/fetch-id-indicators")
def fetch_id_indicators():
    service = WHOService()
    return service.fetch_statistics()[:5]