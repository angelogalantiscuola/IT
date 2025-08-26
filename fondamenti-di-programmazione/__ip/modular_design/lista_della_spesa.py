"""
Scrivi un programma che gestisce una lista della spesa. 
Il programma deve permettere all'utente di aggiungere articoli alla lista, 
visualizzare la lista corrente, e rimuovere articoli dalla lista.
"""

def inserisci_articolo() -> str:
    """
    Function to insert an article.

    Returns:
        str: The inserted article.
    """
    pass

def aggiungi_articolo(articolo: str, lista_della_spesa: list[str]) -> list[str]:
    """
    Aggiunge un articolo alla lista della spesa.

    Args:
        articolo (str): L'articolo da aggiungere alla lista.
        lista_della_spesa (list[str]): La lista della spesa corrente.

    Returns:
        list[str]: La lista della spesa aggiornata con l'articolo aggiunto.
    """
    pass

def visualizza_lista(lista_della_spesa: list[str]) -> None:
    """
    Visualizza la lista della spesa.

    Args:
        lista_della_spesa (list[str]): La lista della spesa da visualizzare.

    Returns:
        None
    """
    pass

def rimuovi_articolo(articolo: str, lista_della_spesa: list[str]) -> list[str] | str:
    """
    Rimuove l'articolo specificato dalla lista della spesa.

    Args:
        articolo (str): L'articolo da rimuovere.
        lista_della_spesa (list[str]): La lista della spesa.

    Returns:
        list[str] | str: La lista della spesa aggiornata senza l'articolo specificato,
        oppure un messaggio di errore se l'articolo non è presente nella lista.

    """
    pass

def main():
    lista_della_spesa = []
    for i in range(3):
        nuovo_articolo = inserisci_articolo()
        lista_della_spesa = aggiungi_articolo(nuovo_articolo, lista_della_spesa)
        articolo_da_rimuovere = inserisci_articolo()
        lista_della_spesa = rimuovi_articolo(articolo_da_rimuovere, lista_della_spesa)