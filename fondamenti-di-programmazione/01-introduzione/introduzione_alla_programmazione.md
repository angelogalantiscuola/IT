## Introduzione alla Programmazione <!-- omit in toc -->

- [Cosa è la Programmazione](#cosa-è-la-programmazione)
- [I Blocchi Fondamentali](#i-blocchi-fondamentali)
- [Il Primo Programma](#il-primo-programma)
- [Concetti Chiave](#concetti-chiave)

### Cosa è la Programmazione

La programmazione è come dare istruzioni a un computer per svolgere un compito. Immagina di spiegare a qualcuno come preparare un panino - devi elencare ogni passo in modo chiaro e preciso. La programmazione funziona allo stesso modo: scrivi una serie di istruzioni che il computer seguirà per raggiungere un obiettivo.

### I Blocchi Fondamentali

Partirei con i tre concetti base che formano qualsiasi programma:

1. **Variabili**: Come scatole dove conservare informazioni

```python
nome = "Marco"  # Memorizza un testo
eta = 25       # Memorizza un numero
```

2. **Istruzioni**: Azioni da eseguire

```python
print("Ciao!")  # Mostra un messaggio
eta = eta + 1   # Aumenta l'età di 1
```

3. **Controllo del flusso**: Decisioni e ripetizioni

```python
if eta >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")
```

### Il Primo Programma

Inizierei con un esempio semplice ma significativo:

```python
# Programma che saluta l'utente
nome = input("Come ti chiami? ")
print(f"Ciao {nome}! Benvenuto alla programmazione!")

eta = int(input("Quanti anni hai? "))
if eta < 18:
    print("Sei giovane!")
else:
    print("Sei un adulto!")
```

### Concetti Chiave

1. **Input/Output**: Come comunicare con il programma
2. **Sequenza**: Le istruzioni vengono eseguite in ordine
3. **Selezione**: Prendere decisioni con `if/else`
4. **Ripetizione**: Ripetere azioni con i cicli
5. **Organizzazione**: Raggruppare il codice in funzioni

> **Nota**: L'approccio migliore è partire con esempi pratici e far sperimentare attivamente il codice, permettendo di vedere immediatamente i risultati delle proprie istruzioni.
