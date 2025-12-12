def print_products_list(products: list[dict[str, any]]) -> None:
    print("-"*30)
    print("LISTA COMPLETA PRODOTTI")
    print("-"*30)

    for i in products:
        print(f"ID: {i["id"]} - TITLE: {i["title"]}")

def print_single_product(product: dict[str, any]) -> None:
    
    print("\n" + "*" * 60)
    print("DETTAGLI PRODOTTO")
    print("*" * 60)

    print(f"ID: {product["id"]}")
    print(f"Titolo: {product["title"]}")
    print(f"Category: {product["category"]}")
    print(f"Price: {product["price"]}")
    print(f"Description: {product["description"]}")

def new_product_c(product: dict[str, any]) -> None:
    print("\n" + "*" * 60)
    print("DETTAGLI PRODOTTO CREATO")
    print("*" * 60)

    print(f"Titolo: {product["title"]}")
    print(f"Category: {[]}")
    print(f"Images: {[]}")
    print(f"Price: {product["price"]}")
    print(f"Description: {product["description"]}")



product = {
  "title": "M&YOU",
  "price": 10,
  "description": "A description",
  "categoryId": 7,
  "images": ["https://placehold.co/600x400"]
}