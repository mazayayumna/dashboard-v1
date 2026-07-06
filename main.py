from fastapi import FastAPI
from sqlalchemy import text

from database.connection import engine

app = FastAPI()

@app.get("/provinces")
def get_provinces():
    
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM provinsi")
        )
        provinces = []

        for row in result:
            provinces.append(
                {
                   "id": row.id,
                   "name": row.name 
                }
            )
        return provinces