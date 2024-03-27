from pydantic import BaseModel


class AddPlace(BaseModel):
    place_name: str
    max_weight: float