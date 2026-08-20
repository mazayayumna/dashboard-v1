from fastapi import FastAPI
from services.who_services import WHOService
from api.statistics import router

app = FastAPI()
app.include_router(router)

@app.get("/get-indicators")
def test_who():
    service = WHOService()
    return service.get_indicators()[:5]

@app.get("/fetch-id-indicators")
def fetch_id_indicators():
    service = WHOService()
    return service.fetch_statistics()[:5]