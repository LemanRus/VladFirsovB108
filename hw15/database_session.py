#!/var/www/u997259/data/flaskenv/bin/python3
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Base

DBSession = sessionmaker(bind=engine)  
session = DBSession() 


# Создаём таблицы при первом запуске один раз, раскоментив вручную
Base.metadata.create_all(engine)