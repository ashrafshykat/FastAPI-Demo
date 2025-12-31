from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()

def load_data():
    with open('products.json', 'r') as f:
        data = json.load(f)
    
    return data


@app.get('/')
def hello():
    return {'message': 'Hello'}

@app.get('/about')
def about():
    return {'message': 'This is about ODL'}

@app.get('/product')
def product():
    return {'message': 'This is a product'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/products/{id}')
def viewprod(id: int):
    data = load_data()
    for product in data:
        if product['id'] == id:
            return product
    raise HTTPException(status_code=404, detail='product not found')