from requests import get, post, Response
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def get_all_product(URL: str)-> list[dict[str, any]]:
    """Restituisce la lista completa dei prodotti."""
    if URL is None:
        raise ValueError("L'URL non può essere vuoto!")
    
    try:
        response = get(URL)
        response.raise_for_status()
        return response.json()
    
    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}:{response.reason}") from e
    
    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")

    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}") from e 
    
    except Exception as e:
        raise Exception(f"Errore nella richiesta dei prodotti: {e}")

def get_single_product(id_product: int, BASE_URL: str) -> dict[str, any]:
    """Restituisce un singolo prodotto dato il suo ID."""
    try:
        url=f"{BASE_URL}/{id_product}"
        response = get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Errore nel recupero del prodotto ID: {id_product}: {e}")
    
def send_product(URL: str, data: dict)-> dict[str, any]:
    
    if URL is None:
        raise ValueError("L'URL non può essere vuoto!")
    
    if data is None:
        raise ValueError("L'URL non può essere vuoto!")
    
    if not isinstance(data, dict):
        raise TypeError("" 
                        f"Risposta inattesa: mi aspettavo un dict, "
                        f"ma ho ricevuto {type(data).__name__}"
        "")
    try:
        response=post_data(URL, data)
        return response.json()
    
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

def post_data(URL: str, data:dict)-> Response:
    try:
        response=post(URL, headers={"Content-Type": "application/json"}, json=data)
        response.raise_for_status()

        return response
    
    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}:{response.reason}") from e
    
    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")

    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}") from e 