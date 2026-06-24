from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser(strict=False)
config.read("/etc/config.ini")

DATABASE_URL = 'postgresql://' + config['dashboard_dummy']['user'] + ':' + config['dashboard_dummy']['pass'] + '@' + config['dashboard_dummy']['host'] + ':' + config['dashboard_dummy']['port'] + '/' + config['dashboard_dummy']['db']

engine = create_engine(DATABASE_URL)
