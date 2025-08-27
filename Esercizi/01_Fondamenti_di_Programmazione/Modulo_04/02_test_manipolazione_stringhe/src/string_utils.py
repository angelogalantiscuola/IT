"""
Questo modulo contiene funzioni di utilità per manipolare le stringhe.
"""


def rendi_maiuscolo(s: str) -> str:
    """Converte una stringa in maiuscolo."""
    return s.upper()


def is_question(s: str) -> bool:
    """Verifica se una stringa termina con un punto di domanda."""
    return s.strip().endswith("?")
