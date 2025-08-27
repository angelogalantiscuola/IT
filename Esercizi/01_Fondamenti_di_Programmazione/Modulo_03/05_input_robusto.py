"""
Esercizio 05: Input Robusto con Gestione delle Eccezioni

Obiettivo:
Imparare a usare i blocchi try...except per gestire gli errori in modo
controllato, prevenendo l'arresto anomalo del programma.

Istruzioni:
Modificheremo l'esercizio 02 del Modulo 01 (quello che calcola l'età) per
renderlo più "robusto".

1.  Crea una funzione `chiedi_anno_nascita()` che non accetta parametri.
2.  All'interno di questa funzione, usa un ciclo `while True` per continuare
    a chiedere all'utente il suo anno di nascita finché non inserisce un
    valore valido (un numero intero).
3.  Dentro il ciclo, usa un blocco `try...except`:
    a. Nel blocco `try`, chiedi l'input all'utente e prova a convertirlo in
       un intero con `int()`.
    b. Se la conversione ha successo, esci dal ciclo usando `return` per
       restituire l'anno convertito.
    c. Nel blocco `except ValueError`, intercetta l'errore che si verifica
       se l'utente inserisce del testo. Stampa un messaggio di errore
       amichevole, ad esempio: "Errore: Inserisci un numero valido."
4.  Nel programma principale:
    a. Chiama la funzione `chiedi_anno_nascita()` e salva il risultato in una variabile.
    b. Calcola e stampa l'età dell'utente come facevi nell'esercizio originale.
"""

# ### INIZIO DEL TUO CODICE ###

ANNO_CORRENTE = 2025


# ### FINE DEL TUO CODICE ###
