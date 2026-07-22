from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Province(Base):
    __tablename__= "provinsi"

    id = Column(Integer, primary_key=True)
    indicator_code = Column(String(50))
    indicator_name = Column(Text)
    country_code = Column(String(5))
    country_name = Column(String(100))
    year = Column(Integer)
    value = Column(Float)
    source = Column(String(30))
    created_at = Column(DateTime)