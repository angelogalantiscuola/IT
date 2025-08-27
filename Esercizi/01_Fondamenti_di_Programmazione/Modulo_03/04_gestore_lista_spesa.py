"""
Esercizio 04: Gestore della Lista della Spesa su File

Obiettivo:
Mettere in pratica la lettura e la scrittura di file di testo per creare
un programma interattivo che salva i suoi dati in modo persistente.

Istruzioni:
Il programma deve gestire una lista della spesa salvata su un file 'spesa.txt'.

1.  Definisci una funzione `mostra_lista(lista)` che stampa la lista della spesa
    in modo ordinato e numerato.
2.  Definisci una funzione `salva_lista(lista, nome_file)` che scrive ogni
    elemento della lista in una nuova riga del file specificato.
3.  All'avvio, il programma deve:
    a. Provare a leggere il file 'spesa.txt'.
    b. Se il file esiste, caricare gli elementi in una lista Python.
    c. Se il file non esiste, creare una lista vuota.
4.  Il programma entra poi in un ciclo `while True` che presenta all'utente un menu:
    - "1. Aggiungi elemento"
    - "2. Mostra lista"
    - "3. Esci"
5.  In base alla scelta dell'utente:
    - Se sceglie '1', chiede quale elemento aggiungere e lo inserisce nella lista.
      Dopo l'aggiunta, salva l'intera lista aggiornata sul file `spesa.txt`.
    - Se sceglie '2', mostra la lista corrente.
    - Se sceglie '3', interrompe il ciclo e termina.
"""

# ### INIZIO DEL TUO CODICE ###

NOME_FILE = "spesa.txt"


# ### FINE DEL TUO CODICE ###
