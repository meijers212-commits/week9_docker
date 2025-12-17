from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
import json

app = FastAPI(title = "my_app" , versiun = "1.0.0")

DB_PATH = Path("./db/shopping_list.json")

class Item(BaseModel):
    name: str
    quantity: int


def load_data():
    with open(DB_PATH,"r") as db:

        try:
            return json.load(db)
        
        except Exception as r:
            raise f"chat load db sexsespul error:{r}"


def save_new_db(data):
     with open(DB_PATH,"w") as db:

        try:
            json.dump(data,db,indent=2)
            return{"data updated sexsesful !"}
        
        except Exception as r:
            raise f"chat load db sexsespul error:{r}"
        

@app.get("/items")
def get_all_items():
    return load_data()

@app.post("/items")
def create_item(item: Item):
    data =  load_data()
    new_id = len(data)+1
    data.append({"id":new_id,"name":item.name,"quantity":item.quantity})
    save_new_db(data)


if __name__=="__maine__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)