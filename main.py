from fastapi import FastAPI
from sqlalchemy import text
from models import engine, SessionLocal
from models import Province

app = FastAPI()

@app.get("/provinces")
def get_provinces():
    
    session = SessionLocal()
    provinces = session.query(Province).all()
    
    result = [
        {
            "id": p.id,
            "name": p.name
        }
        for p in provinces
    ]
    session.close()

    return result