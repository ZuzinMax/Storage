from pydantic import BaseModel


class AddItem(BaseModel):
    item_name: str
    item_weight: float
