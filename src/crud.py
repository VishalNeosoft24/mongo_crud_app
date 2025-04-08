from bson import ObjectId
from database import collection

def serialize_item(item):
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item.get("description"),
        "price": item["price"]
    }

def create_item(item_data):
    result = collection.insert_one(item_data)
    return str(result.inserted_id)

def get_all_items():
    return [serialize_item(item) for item in collection.find()]

def get_item_by_id(item_id):
    item = collection.find_one({"_id": ObjectId(item_id)})
    return serialize_item(item) if item else None

def update_item(item_id, item_data):
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})
    return get_item_by_id(item_id)

def delete_item(item_id):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
