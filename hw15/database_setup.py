#!/var/www/u997259/data/flaskenv/bin/python3

import sys  
# для настройки баз данных 
from sqlalchemy import Column, ForeignKey, Integer, String, Date  
  
# для определения таблицы и модели 
from sqlalchemy.ext.declarative import declarative_base  
  
# для создания отношений между таблицами
from sqlalchemy.orm import relationship  
  
# для настроек
from sqlalchemy import create_engine  
  
# создание экземпляра declarative_base
Base = declarative_base()  

  
class Methodics(Base):  
    __tablename__ = 'methodics'  
    
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False)  
    year = Column(Integer, nullable=False)


class Reagents(Base):  
    __tablename__ = 'reagents'  
    
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False)  
    qty = Column(String(250), nullable=False) 
    best = Column(Date, nullable=False)
    

class Assigns(Base):  
    __tablename__ = 'assigns'  
    
    id = Column(Integer, primary_key=True)  
    methodic_id = Column(Integer, ForeignKey("methodics.id")) 
    reagent_id = Column(Integer, ForeignKey("reagents.id")) 


  
# создает экземпляр create_engine в конце файла  
engine = create_engine("mysql+pymysql://u997259_test:Waha40k@localhost/u997259_test")
  
Base.metadata.create_all(engine)


