#!/var/www/u997259/data/flaskenv/bin/python3
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Base

DBSession = sessionmaker(bind=engine)  

# Создаём таблицы при первом запуске
Base.metadata.create_all(engine)