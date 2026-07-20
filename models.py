from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import configparser

config = configparser.ConfigParser(strict=False)
config.read("/etc/config.ini")

DATABASE_URL = 'postgresql://' + config['dashboard_dummy']['user'] + ':' + config['dashboard_dummy']['pass'] + '@' + config['dashboard_dummy']['host'] + ':' + config['dashboard_dummy']['port'] + '/' + config['dashboard_dummy']['db']
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Province(Base):
    __tablename__= "provinsi"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)