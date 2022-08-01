from pydantic import BaseModel

class Buy(BaseModel):
    id_number: str
    name: str
    price: int
    address: str