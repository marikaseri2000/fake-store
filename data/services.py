
def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"],
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }

def new_product_model(titolo_product: str, prezzo_product: int, descrizione_product: str) -> dict[str, any]:
    return {
        "title": titolo_product,
        "price": prezzo_product, 
        "description": descrizione_product,
        "categoryId": 1,
        "images": ["---"]
    }
