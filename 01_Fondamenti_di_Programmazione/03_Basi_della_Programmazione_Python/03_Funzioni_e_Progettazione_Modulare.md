# Funzioni e Progettazione Modulare

## 1. Cosa sono le Funzioni?

Una **funzione** è un blocco di codice riutilizzabile che esegue un'azione specifica. Le funzioni ci aiutano a organizzare il codice, evitare ripetizioni e rendere i nostri programmi più leggibili e facili da manutenere.

Una funzione può ricevere dei dati in input (i **parametri**) e restituire un risultato in output (il **valore di ritorno**).

### Struttura di una Funzione

```python
def nome_funzione(parametro1: tipo, parametro2: tipo) -> tipo_ritorno:
    # Corpo della funzione: istruzioni da eseguire
    risultato = parametro1 + parametro2
    return risultato
```
- `def`: La parola chiave per definire una funzione.
- `nome_funzione`: Il nome che diamo alla nostra funzione.
- `(parametri)`: I valori in input che la funzione accetta.
- `-> tipo_ritorno`: Il type hint che indica il tipo di dato che la funzione restituirà.
- `return`: La parola chiave per restituire un valore.

**Esempio:**
```python
def calcola_area_rettangolo(base: float, altezza: float) -> float:
    """Calcola l'area di un rettangolo."""
    area = base * altezza
    return area

# Utilizzo (o "chiamata") della funzione
superficie: float = calcola_area_rettangolo(10.5, 3)
print(f"L'area del rettangolo è: {superficie}") # Output: 31.5
```

## 2. Procedure vs Funzioni

-   **Procedura**: Una funzione che esegue delle azioni ma **non restituisce alcun valore**. Il suo tipo di ritorno è `None`.
    ```python
    def saluta(nome: str) -> None:
        """Stampa un saluto personalizzato."""
        print(f"Ciao, {nome}!")
    ```
-   **Funzione**: Restituisce un valore specifico che può essere usato nel resto del programma.

## 3. Parametri Flessibili: `*args` e `**kwargs`

A volte non sappiamo in anticipo quanti argomenti dovrà accettare una funzione. Python ci offre due strumenti speciali:

### `*args` (Argomenti posizionali)
Raccoglie un numero indefinito di argomenti posizionali in una **tupla**.

```python
def somma_tutti(*numeri: int) -> int:
    """Somma un numero indefinito di interi."""
    print(f"Sto sommando i numeri: {numeri}")
    return sum(numeri)

risultato = somma_tutti(1, 2, 3, 4, 5) # numeri sarà (1, 2, 3, 4, 5)
print(risultato) # Output: 15
```

### `**kwargs` (Argomenti con parola chiave)
Raccoglie un numero indefinito di argomenti nominali (con nome) in un **dizionario**.

```python
def stampa_dati_utente(**dati_utente: any) -> None:
    """Stampa i dati di un utente."""
    print(f"Dati ricevuti: {dati_utente}")
    for chiave, valore in dati_utente.items():
        print(f"- {chiave}: {valore}")

stampa_dati_utente(nome="Mario", eta=30, citta="Roma")
```

## 4. Progettazione Modulare: l'Approccio Top-Down

La **progettazione modulare** consiste nel suddividere un problema complesso in sottoproblemi più piccoli e gestibili, ognuno risolto da una funzione.

L'approccio **Top-Down** prevede di:
1.  **Definire la funzione principale** (`main`) che delinea la logica generale del programma.
2.  **Identificare le sotto-funzioni** necessarie per ogni passaggio.
3.  **Scrivere le "firme"** (nome, parametri e tipo di ritorno) delle sotto-funzioni, usando `pass` come segnaposto per il corpo.
4.  **Implementare** ogni sotto-funzione una alla volta.

Questo approccio ci aiuta a concentrarci prima sulla logica generale e poi sui dettagli, rendendo il codice più organizzato e facile da sviluppare.

**Esempio - Calcolatrice Semplice:**
```python
def chiedi_numeri() -> list[float]:
    """Chiede all'utente due numeri e li restituisce in una lista."""
    pass # Implementeremo i dettagli dopo

def scegli_operazione() -> str:
    """Mostra un menu e restituisce l'operazione scelta."""
    pass

def calcola(num1: float, num2: float, operazione: str) -> float | None:
    """Esegue il calcolo e restituisce il risultato."""
    pass

def main() -> None:
    """Funzione principale che orchestra il programma."""
    print("Benvenuto nella Calcolatrice Modulare!")
    numeri = chiedi_numeri()
    operazione = scegli_operazione()
    risultato = calcola(numeri, numeri, operazione)
    
    if risultato is not None:
        print(f"Il risultato è: {risultato}")
    else:
        print("Operazione non valida.")

# Avvio del programma
main()
```