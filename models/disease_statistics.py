from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class DiseaseStatistics(Base):
    __tablename__= "disease_statistics"

    id = Column(Integer, primary_key=True)
    indicator_code = Column(String(100))
    indicator_name = Column(String(255))
    country_code = Column(String(10))
    country_name = Column(String(100))
    year = Column(Integer)
    value = Column(Float)
    source = Column(String(50))
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
        )