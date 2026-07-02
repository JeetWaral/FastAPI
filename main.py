from fastapi import FastAPI
from models import Product
# for Database
from database import session, engine
import database_model 



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


# database Connection
database_model.Base.metadata.create_all(bind=engine)
def init_db():

    db = session()
    count = db.query(database_model.Product).count() # Nothing but select count(*) from product(In Mysql)
    
    # So we craeted count varaible to check if there is data already in the Db.
    # As we are running the script again and again it will try to add the same thing again and again.
    if count ==0:
        for product in Products:
            #db.add(product) So ths will not work as it is a model of pydantci and not Alechemy.
            db.add(database_model.Product(**product.model_dump()))
            # We will need to pass the Db object, so we are basically converting the pydantic model to database model
            # The database_model.product expects a key value pair to create a object for it.
            # model_dum() gives a dictionary
            # So we will not need dictionary we will need actuall key and values and thus we used **- unpacking

        db.commit()
init_db()#


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