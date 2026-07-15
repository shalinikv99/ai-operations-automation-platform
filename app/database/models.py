import sqlalchemy as db
from sqlalchemy.orm import declarative_base
import datetime 

Base = declarative_base()

class Lead(Base):
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key= True, index=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(250),unique = True, nullable = False)
    company = db.Column(db.String(100))
    source = db.Column(db.String(100))
    status = db.Column(db.String(100))
    priority = db.Column(db.String(100))
    ai_summary = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow)