import requests 

def get_all_product(BASE_URL: str)-> list[dict[str, any]]:
    """Restituisce la lista completa dei prodotti."""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Errore nella richiesta dei prodotti: {e}")    

def get_single_product(id_product: int, BASE_URL: str) -> dict[str, any]:
    """Restituisce un singolo prodotto dato il suo ID."""
    try:
        url=f"{BASE_URL}/{id_product}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Errore nel recupero del prodotto ID: {id_product}: {e}")