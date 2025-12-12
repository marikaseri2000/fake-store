
def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"],
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }
