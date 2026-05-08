from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models import Flower

app = FastAPI()

@app.get("/flower/{communities}")
def get_flowers_by_community(communities: str, db: Session = Depends(get_db)):
    results = db.query(Flower).filter(Flower.communities.contains(communities)).all()
    return results