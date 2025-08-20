
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
DataBase_Url = "postgresql://postgres:Artur@localhost:5432/postgres"

engine = create_engine(DataBase_Url)
        
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
