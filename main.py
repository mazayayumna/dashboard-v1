from fastapi import FastAPI
from services.who_services import WHOService

app = FastAPI()

@app.get("/test-who")
def test_who():
    service = WHOService()
    return service.get_indicators()[:5]