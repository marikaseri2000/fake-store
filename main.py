from data.services import product_model, new_product_model
from ui.console import print_products_list, print_single_product, product, new_product_c
from data.repository import get_all_product, get_single_product,send_product
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
        
        while True:
            
            try:
                #Titolo
                titolo_product: str = input("Inserisci il titolo del nuovo prodotto: ").strip()
                if titolo_product == "":
                    raise ValueError("Il titolo del nuovo prodotto non può essere vuoto!")
                
                #Prezzo
                prezzo_product: int = input("Inserisci il prezzo del nuovo prodotto: ").strip()
                if prezzo_product == "":
                    raise ValueError("Il prezzo del nuovo prodotto non può essere vuoto!")
                
                #Descrizione
                descrizione_product: str = input("Inserisci la descrizione del nuovo prodotto: ").strip()
                if descrizione_product == "":
                    raise ValueError("La descrizione del nuovo prodotto non può essere vuoto!")
                
                break

            except ValueError as e:
                print("Errore: {e}")

        new_product: dict[str, any]= new_product_model(titolo_product,prezzo_product,descrizione_product)
        print("\nProdotto creato con successo!")
        new_product_c(send_product(BASE_URL,new_product))
        
    except ValueError as e:
        print(f"Errore: {e}")
    
    except FileNotFoundError as e:
        print(f"Errore: {e}")

    except Exception as e:
        print(f"Errore: {e}")

if __name__=="__main__":
    main()