from fastapi import FastAPI
from datetime import datetime
from app.core.logging import logger
from app.database.models import Base
from app.database.database import engine
app = FastAPI()

#create table

Base.metadata.create_all(bind=engine)


@app.get("/health")

def health_check():
    logger.info("Health endpoint called")
    return { "status": "healthy" , "service": "AI Operations Automation Platform", "version": "0.0.1", "timestamp": datetime.utcnow().isoformat()}


#logger.info("Health check successful!")


