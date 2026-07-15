#engine,session creation

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

#import app.database.models as models
load_dotenv()
#connection object 
engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")  

Session = sessionmaker(bind= engine)
#result = Session()
#result.query(models.Lead).all()
