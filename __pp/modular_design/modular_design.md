%% Begin Waypoint %%


%% End Waypoint %%

# Progettazione modulare

Gli esercizi richiedono di seguire un approccio top-down alla progettazione del software. In questo approccio, si inizia definendo l'interfaccia di alto livello del programma (in questo caso, la funzione main) e poi si definiscono le "signature" delle funzioni di supporto.

La "signature" di una funzione include il suo nome, i tipi dei suoi parametri e il tipo del suo valore di ritorno. Non è necessario scrivere l'implementazione completa di queste funzioni; invece, si dovrebbe scrivere solo una versione "stub" della funzione che include la signature ma non il corpo della funzione. Questo è indicato con la parola chiave pass in Python.

Per esempio, per l'esercizio "Gestione di una rubrica di indirizzi", lo studente dovrebbe scrivere la funzione main che usa le funzioni inserisci_dati, aggiungi_contatto, visualizza_contatti, e cerca_contatto. Per queste funzioni, lo studente dovrebbe scrivere solo la signature, non l'implementazione completa.

Questo approccio alla progettazione del software aiuta a pensare in modo modulare e a concentrarsi sull'interfaccia delle funzioni piuttosto che sui dettagli della loro implementazione.

## Gestione di una rubrica di indirizzi

Scrivi un programma che gestisca una semplice rubrica di indirizzi. Il programma deve permettere di aggiungere nuovi contatti, visualizzare tutti i contatti esistenti e cercare un contatto specifico per nome.

```python
# Definizione di un tipo di dato per rappresentare un contatto
Contatto = dict[str, str]  # {'nome': ..., 'indirizzo': ..., 'numero': ...}

# Funzione per chiedere all'utente i dati
def inserisci_dati() -> Contatto:
    pass

# Funzione per aggiungere un nuovo contatto
def aggiungi_contatto(rubrica: list[Contatto], contatto: Contatto) -> list[Contatto]:
    pass

# Funzione per visualizzare tutti i contatti
def visualizza_contatti(rubrica: list[Contatto]) -> None:
    pass


# Funzione per cercare un contatto per nome
def cerca_contatto(rubrica: list[Contatto], nome: str) -> Contatto | None:
    pass


# Funzione principale
def main() -> None:
    rubrica = []
    contatto = inserisci_dati()
    rubrica = aggiungi_contatto(rubrica, contatto)

    visualizza_contatti(rubrica)

    nome = input("Inserisci il nome del contatto da cercare: ")
    contatto = cerca_contatto(rubrica, nome)
    if contatto is not None:
        print(f"Contatto trovato: {contatto}")
    else:
        print("Contatto non trovato")
```


## Calcolatrice Semplice

Scrivi un programma che simula una calcolatrice semplice. Il programma deve permettere all'utente di inserire due numeri e scegliere un'operazione (addizione, sottrazione, moltiplicazione, divisione). Il programma deve quindi visualizzare il risultato dell'operazione.

```python
def inserisci_numeri():
    pass

def scegli_operazione():
    pass

def calcola():
    pass

def main():
    pass
```

## Gestione di una Lista della Spesa

Scrivi un programma che gestisce una lista della spesa. Il programma deve permettere all'utente di aggiungere articoli alla lista, visualizzare la lista corrente, e rimuovere articoli dalla lista.

```python
def inserisci_articolo():
    pass

def aggiungi_articolo():
    pass

def visualizza_lista():
    pass

def rimuovi_articolo():
    pass

def main():
    pass
```

## Gestione di un Catalogo di Libri

Scrivi un programma che gestisce un catalogo di libri. Ogni libro ha un titolo, un autore e un anno di pubblicazione. Il programma deve permettere all'utente di aggiungere libri al catalogo, visualizzare il catalogo corrente, cercare libri per titolo o autore, e rimuovere libri dal catalogo.

## Gestione di un Sistema di Prenotazione di Voli

Scrivi un programma che gestisce un sistema di prenotazione di voli. Ogni volo ha una destinazione, una data e un numero di posti disponibili. Il programma deve permettere all'utente di aggiungere voli, visualizzare i voli disponibili, prenotare un volo, e visualizzare le prenotazioni correnti.

## Gestione di un Sistema di Prenotazione di Hotel

Scrivi un programma che gestisce un sistema di prenotazione di hotel. Ogni hotel ha un nome, una località, un numero di stanze disponibili e un prezzo per notte. Il programma deve permettere all'utente di aggiungere hotel, visualizzare gli hotel disponibili, prenotare una stanza, e visualizzare le prenotazioni correnti. Inoltre, il programma deve gestire le prenotazioni in modo che non sia possibile prenotare una stanza se l'hotel è al completo.

## Gestione di un sistema di prenotazione per un cinema

Scrivi un programma che gestisce un sistema di prenotazione per un cinema. Il cinema ha diverse sale, ognuna con un numero diverso di posti. Gli utenti possono prenotare posti per uno specifico film in una specifica sala. Il programma deve permettere all'utente di:

- Aggiungere una sala al cinema.
- Rimuovere una sala dal cinema.
- Visualizzare tutte le sale del cinema.
- Aggiungere un film a una sala.
- Rimuovere un film da una sala.
- Visualizzare tutti i film in una sala.
- Prenotare un posto per un film in una sala.
- Annullare una prenotazione per un film in una sala.

In questo esercizio, il cinema è rappresentato come un dizionario di tipo `Cinema`, dove ogni chiave è il nome di una sala e il valore è un altro dizionario di tipo `Sala` che contiene i dettagli della sala, come il numero di posti disponibili e l'elenco dei film in programmazione. Le funzioni modificano e interagiscono con questo dizionario per gestire il cinema.

