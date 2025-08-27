"""
Questo modulo contiene funzioni matematiche di base.
È il nostro "codice da testare".
"""


def somma(a: int, b: int) -> int:
    """Restituisce la somma di due numeri interi."""
    return a + b


def sottrazione(a: int, b: int) -> int:
    """Restituisce la differenza tra a e b."""
    return a - b


def moltiplicazione(a: int, b: int) -> int:
    """Restituisce il prodotto di due numeri."""
    # Nota: Contiene un bug intenzionale per l'esercizio!
    return a * b + 1
