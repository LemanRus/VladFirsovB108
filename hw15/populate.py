#!/var/www/u997259/data/flaskenv/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from database_setup import Methodics, Reagents, Assigns, Base

engine = create_engine("mysql+pymysql://u997259_test:Waha40k@localhost/u997259_test")
# Свяжим engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов, 
# загруженных в объект сессии базы данных.
session = DBSession()