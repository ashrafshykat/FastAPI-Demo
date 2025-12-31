from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('product.json', r) as f:
        data = json.load(f)
    
    return data


@app.get("/")
def hello():
    return {'message': 'Hello'}

@app.get("/about")
def about():
    return {'message': 'This is about ODL'}

@app.get("/product")
def product():
    return {'message': 'This is a product'}

@app.get("/view")
def view():
    