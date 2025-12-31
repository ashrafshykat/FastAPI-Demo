from fastapi import FastAPI, Path, HTTPException, Query
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
def viewprod(id: int = Path(..., description='enter integer value to get product')):
    data = load_data()
    for product in data:
        if product['id'] == id:
            return product
    raise HTTPException(status_code=404, detail='product not found')

@app.get("/query")
def sort_products(
    sort_by: str = Query("id", enum=["id", "name", "price"]),
    order: str = Query("asc", enum=["asc", "desc"])
):
    data = load_data()

    reverse = True if order == "desc" else False

    try:
        sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=reverse)
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    return sorted_data
