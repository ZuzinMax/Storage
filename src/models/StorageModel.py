from pydantic import BaseModel

class StorageModel(BaseModel):
    item_id: int
    item: str
    weight: float
    place_id: int
    place_name: str
    quantity: int

class ReadStorage(BaseModel):
    place_name: str