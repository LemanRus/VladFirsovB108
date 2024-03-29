#!/var/www/u997259/data/flaskenv/bin/python3

import sys
import os

from sqlalchemy import Column, ForeignKey, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base  

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

db_login = os.environ.get("DB_LOGIN")
db_password = os.environ.get("DB_PASSWORD")

Base = declarative_base() 

engine = create_engine(f"mysql+pymysql://{db_login}:{db_password}@localhost/u997259_test")


class Methodics(Base):  
    __tablename__ = 'methodics'  
    
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False, unique=True)  
    year = Column(Integer, nullable=False)


class Reagents(Base):  
    __tablename__ = 'reagents'  
    
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False, unique=True)  
    qty = Column(String(250), nullable=False) 
    best = Column(Date, nullable=False)
    

class Assigns(Base):  
    __tablename__ = 'assigns'  
    
    id = Column(Integer, primary_key=True)  
    methodic_id = Column(Integer, ForeignKey("methodics.id", ondelete='CASCADE')) 
    reagent_id = Column(Integer, ForeignKey("reagents.id", ondelete='CASCADE')) 



