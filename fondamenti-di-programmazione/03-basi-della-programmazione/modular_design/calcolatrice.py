"""
Scrivi un programma che simula una calcolatrice semplice. 
Il programma deve permettere all'utente di inserire due numeri e scegliere un'operazione 
(addizione, sottrazione, moltiplicazione, divisione). 
Il programma deve quindi visualizzare il risultato dell'operazione.
"""

def inserisci_numeri() -> list[int]:
    """
    This function prompts the user to input a list of numbers and returns the list.

    Returns:
        list[int]: A list of numbers entered by the user.
    """
    pass

def scegli_operazione() -> str:
    """
    This function prompts the user to choose an operation and returns the selected operation as a string.

    Returns:
        str: The selected operation.
    """
    pass

def calcola(numeri: list[int], operazione: str) -> float:
    """
    Perform a mathematical operation on a list of numbers.

    Args:
        numeri (list[int]): A list of numbers.
        operazione (str): The mathematical operation to perform.

    Returns:
        float: The result of the mathematical operation.

    """
    pass

def main():
    numeri_inseriti = inserisci_numeri()
    operazione = scegli_operazione()
    risultato = calcola(numeri_inseriti, operazione)
    print(f"Il risultato dell'operazione è: {risultato}")
