from typing import List
import json

def load_data():
    with open('products.json', 'r') as f:
        data = json.load(f)
    return data

def validate_id(product_id: int) -> bool:
    if not isinstance(product_id, int) or product_id <= 0:
        raise ValueError("ID must be a positive integer.")
    data = load_data()
    if any(product['id'] == product_id for product in data):
        raise ValueError(f"Product ID {product_id} already exists.")
    
    return True

def validate_name(name: str) -> bool:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    return True

def validate_price(price: float) -> bool:
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Price must be a positive number.")
    return True

VALID_CATEGORIES = ["Electronics", "Furniture", "Accessories", "Stationery"]

def validate_category(category: str) -> bool:
    if category not in VALID_CATEGORIES:
        raise ValueError(f"Category must be one of: {', '.join(VALID_CATEGORIES)}")
    return True

def validate_in_stock(in_stock: bool) -> bool:
    if not isinstance(in_stock, bool):
        raise ValueError("In stock must be a boolean value.")
    return True