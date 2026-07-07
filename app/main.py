from fastapi import FastAPI
from datetime import datetime
import logging

app = FastAPI()

@app.get("/health")

def health_check():
    logging.info("Health check endpoint called")
    return { "status": "healthy" , "service": "AI Operations Automation Platform", "version": "0.0.1", "timestamp": datetime.utcnow().isoformat()}


logging.info("Health check successful!")
