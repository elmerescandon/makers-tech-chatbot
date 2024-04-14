from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field;
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class Product(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    model: str
    category: str
    brand: str
    price: float
    stock: int
    rating: float
    specs: dict
    similar: list