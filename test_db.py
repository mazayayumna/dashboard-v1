from sqlalchemy import text
from database.connection import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM provinsi"))

    for row in result:
        print(row)