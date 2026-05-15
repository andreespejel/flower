from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.middleware.cors  import CORSMiddleware
from .database import Base, engine
from .dependencies import get_db
from .models import Flower
from .schemas import FlowerResponse

# create (single)table in the engine
Base.metadata.create_all(engine)

app = FastAPI()

# alllow requests from HTML
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# helper function to deduplicate list
def deduplicate(deduplicate_list): # take in list of communities, remove duplicates
    flattened_list = []
    for sublist in deduplicate_list:
        temp = sublist.split(',')
        for item in temp:
            flattened_list.append(item.strip())
    deduplicate_list = list(dict.fromkeys(flattened_list))
    return deduplicate_list

# route to make dropdown dict, calls deduplicate function
@app.get("/procure-communities", response_model=list[str]) # endpoint
def procure_habitat(db: Session = Depends(get_db)): # 
    results = db.execute(select(Flower.communities)).all()
    communities_list = [row[0] for row in results if row[0] is not None]
    # call deduplicate
    communities_list = deduplicate(communities_list)
    return communities_list

# route, query for flowers that contain {community (habitat)}
@app.get("/flower/{communities}", response_model=list[FlowerResponse])
def get_flowers_by_community(communities: str, db: Session = Depends(get_db)):
    results = db.query(Flower).filter(Flower.communities.contains(communities)).all()
    return results

