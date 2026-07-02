from pydantic import BaseModel

#Without Pydantic
# class Products:
#     id: int
#     name: str
#     description: str
#     price: int
#     quantity: int

#     def __init__(self, id, name, description, price, quantity):
#         self.id =id
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity = quantity

#With Pydantic
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    quantity: int

#With Pydabtic we do not need to create constructor, it happens within so we do not need to worry about the constuctor and validations