from typing import List
from pydantic import BaseModel

from utils.classes.Products import Product


class EcommerceCollection(BaseModel):
    products: List[Product]