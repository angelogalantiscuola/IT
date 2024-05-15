# Scrivi un programma che simula una calcolatrice semplice. 
# Il programma deve permettere all'utente di inserire due numeri e scegliere un'operazione 
# (addizione, sottrazione, moltiplicazione, divisione). 
# Il programma deve quindi visualizzare il risultato dell'operazione.

# def inserisci_numeri() -> list[int]:
#     """
#     This function prompts the user to input a list of numbers and returns the list.

#     Returns:
#         list[int]: A list of numbers entered by the user.
#     """
#     pass

# def scegli_operazione() -> str:
#     """
#     This function prompts the user to choose an operation and returns the selected operation as a string.

#     Returns:
#         str: The selected operation.
#     """
#     pass

# def calcola(numeri: list[int], operazione: str) -> float:
#     """
#     Perform a mathematical operation on a list of numbers.

#     Args:
#         numeri (list[int]): A list of numbers.
#         operazione (str): The mathematical operation to perform.

#     Returns:
#         float: The result of the mathematical operation.

#     """
#     pass

# def main():
#     numeri_inseriti = inserisci_numeri()
#     operazione = scegli_operazione()
#     risultato = calcola(numeri_inseriti, operazione)
#     print(f"Il risultato dell'operazione è: {risultato}")


# Scrivi un programma che gestisce una lista della spesa. 
# Il programma deve permettere all'utente di aggiungere articoli alla lista, 
# visualizzare la lista corrente, e rimuovere articoli dalla lista.
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
    