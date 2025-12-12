import requests 

def get_all_product(URL: str)-> list[dict[str, any]]:
    """Restituisce la lista completa dei prodotti."""
    if URL is None:
        raise ValueError("L'URL non può essere vuoto!")
    
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Errore nella richiesta dei prodotti: {e}")   

    except requests.exceptions.HTTPError as e:
        raise requests.exceptions.HTTPError(f"Errore HTTP {requests.status_codes} su {URL}:{response.reason}") from e
    
    except requests.exceptions.ConnectionError:
        raise requests.ConnectionError(f"Impossibile connettersi a {URL}")

    except requests.exceptions.Timeout:
        raise requests.Timeout(f"Timeout nella richiesta a {URL}")
    
    except requests.exceptions.RequestException as e:
        raise requests.RequestException(f"Errore di rete imprevisto: {e}") from e 

def get_single_product(id_product: int, BASE_URL: str) -> dict[str, any]:
    """Restituisce un singolo prodotto dato il suo ID."""
    try:
        url=f"{BASE_URL}/{id_product}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Errore nel recupero del prodotto ID: {id_product}: {e}")