from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:PASS@localhost:5432/disease_dashboard"

engine = create_engine(DATABASE_URL)