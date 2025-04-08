from fastapi import FastAPI, HTTPException
from models import Item
from crud import create_item, get_all_items, get_item_by_id, update_item, delete_item

app = FastAPI()

@app.post("/items/")
def create(item: Item):
    item_id = create_item(item.dict())
    return {"id": item_id}

@app.get("/items/")
def read_all():
    return get_all_items()

@app.get("/items/{item_id}")
def read(item_id: str):
    item = get_item_by_id(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update(item_id: str, item: Item):
    updated = update_item(item_id, item.dict())
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete(item_id: str):
    if delete_item(item_id):
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
