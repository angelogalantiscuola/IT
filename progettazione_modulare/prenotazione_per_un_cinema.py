# Definizione di un tipo di dato per rappresentare un film
Film = dict[str, str | int]  # {'titolo': ..., 'posti_prenotati': ...}

# Definizione di un tipo di dato per rappresentare una sala
Sala = dict[str, str | int | list[Film]]  # {'nome': ..., 'posti_totali': ..., 'film': ...}

# Definizione di un tipo di dato per rappresentare un cinema
# Ogni chiave è il nome di una sala 
# e il valore è un dizionario che rappresenta i dettagli della sala.
Cinema = dict[str, Sala]

def aggiungi_sala(cinema: Cinema, sala: str, posti: int) -> Cinema:
    pass

def rimuovi_sala(cinema: Cinema, sala: str) -> Cinema:
    pass

def visualizza_sale(cinema: Cinema) -> None:
    pass

def aggiungi_film(cinema: Cinema, sala: str, film: str) -> Cinema:
    pass

def rimuovi_film(cinema: Cinema, sala: str, film: str) -> Cinema:
    pass

def visualizza_film(cinema: Cinema, sala: str) -> None:
    pass

def prenota_posto(cinema: Cinema, sala: str, film: str) -> Cinema:
    pass

def annulla_prenotazione(cinema: Cinema, sala: str, film: str) -> Cinema:
    pass

def main():
    pass