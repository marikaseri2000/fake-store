from data.services import product_model
from ui.console import print_products_list, print_single_product, product
from data.repository import get_all_product, get_single_product,send_product,post_data
from costants import BASE_URL

def main() -> None:
    
    try:
        #Recupero tutti i prodotti
        products=get_all_product(BASE_URL)
        print_products_list(products) 
        
        while True:
            try:
                scelta_products = input("Scegli l'id del prodotto da visualizzare tra quelli mostrati a video: ")
                break
            except ValueError:
                print("Devi inserire un valore valido.")
        
        product_chosen: dict[str, any] = get_single_product(scelta_products, BASE_URL)
        product = product_model(product_chosen)
        print_single_product(product)
        
        #print_single_product(send_product(BASE_URL,product))

    except ValueError as e:
        print(f"Errore: {e}")
    
    except FileNotFoundError as e:
        print(f"Errore: {e}")

    except Exception as e:
        print(f"Errore: {e}")

if __name__=="__main__":
    main()