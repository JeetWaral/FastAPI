from fastapi import FastAPI
from models import Product

app=FastAPI()

@app.get("/")
def home():
    return ({"message": "All Good"})

# Products = [
#     Products(1, "Phone","Budget Phone", 29999, 10 ),
#     Products(2, "Laptop","Gaming Laptop", 45999, 5 )
# ]

Products = [
    Product(id=1, name="Phone",description ="Budget Phone", price =29999, quantity=10 ),
    Product(id=2, name= "Laptop",description ="Gaming Laptop", price =45999, quantity=5 ),
    Product(id=6, name= "Shirt",description ="Mens's Shirts", price =799, quantity=25 ),
    Product(id=10, name= "T-Shirt",description ="Mens's T-Shirts", price =999, quantity=20 )
]

@app.get("/products")
def get_all_products():
    return Products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in Products:
        if product.id == id:
            return product
        
    else:
        return {"message": "Product not found"}
    
@app.post("/product")
def add_product(product: Product):
    for product_already in Products:
        if product_already.id == product.id:
            return {"error": "Need to change the id, id already present in Db"}
    else:
        Products.append(product)
        return product

@app.put("/product")
def update_product(id:int ,product :Product):
    for i in range(len(Products)):
        if Products[i].id == id:
            Products[i] = product
            return {"message": "Product Updated Succesfully"}
        
    else:
        return {"message": f"No such Product with id {id} Exists"}

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(Products)):
        if Products[i].id == id:
            del Products[i]
            return {"succes": "Product Deleted Sucessfully"}
    else:
        return {"error": f"No Such product with id {id} exists"}