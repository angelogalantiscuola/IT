# Funzioni e Contratti Software

Una funzione è un blocco di codice autonomo che esegue un compito specifico. Invece di scrivere "spaghetti code" lunghi centinaia di righe, usiamo le funzioni per dividere il problema in moduli riutilizzabili.

---

## 1. La Funzione come "Contratto"

Nel software moderno una funzione è un **contratto formale** tra chi la scrive e chi la usa:
1. **Cosa richiede in ingresso?** (I parametri e i loro tipi).
2. **Cosa garantisce in uscita?** (Il valore di ritorno e il suo tipo).
3. **Cosa fa?** (La docstring riassuntiva).

```python
def calcola_sconto(prezzo_originale: float, percentuale_sconto: float) -> float:
    """
    Calcola il prezzo finale scontato.
    
    Argomenti:
        prezzo_originale: Prezzo positivo in Euro.
        percentuale_sconto: Valore percentuale tra 0 e 100.
        
    Ritorna:
        Il prezzo finale scontato come numero float.
    """
    quota_sconto = (prezzo_originale * percentuale_sconto) / 100.0
    prezzo_finale = prezzo_originale - quota_sconto
    return prezzo_finale
```

### Anatomia del Contratto:
* `def nome_funzione(...)`: Parola chiave di definizione.
* `prezzo_originale: float`: Parametro con **Type Hint**.
* `-> float`: Indica il tipo esatto di valore che la funzione **restituisce**.
* `""" Docstring """`: La descrizione del contratto in italiano chiaro.
* `return`: Restituisce il valore calcolato a chi ha chiamato la funzione.

---

## 2. La Regola Fondamentale: `return` vs `print`

Questo è l'errore più comune dei principianti: confondere l'azione di *restituire un valore* con quella di *stamparlo sullo schermo*.

```
   ❌ FUNZIONE "CIECA" (usa print)                 ✅ FUNZIONE "PURA" (usa return)
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│ def somma(a, b):                │           │ def somma(a, b):                │
│     print(a + b)  <-- Muore qui!│           │     return a + b  <-- Restituisce│
└─────────────────────────────────┘           └─────────────────────────────────┘
                │                                             │
                ▼                                             ▼
  Non puoi riusare il risultato!               Puoi riusarlo in altri calcoli:
  x = somma(2, 3)  # x vale None!              x = somma(2, 3) * 10  # x vale 50!
```

* **`return` (Il Cervello):** Calcola il risultato e lo spedisce a chi lo ha richiesto. Il dato è vivo e può essere memorizzato, salvato su file o usato in altri calcoli.
* **`print` (La Voce):** Si limita a mostrare dei pixel luminosi sullo schermo del terminale. Non restituisce nulla (`None`).

---

## 3. Parametri Opzionali (Valori di Default)

Possiamo fornire un valore predefinito a un parametro nel caso in cui chi chiama la funzione decida di non specificarlo:

```python
def saluta_utente(nome: str, titolo: str = "Sig./Sig.ra") -> str:
    """Restituisce un saluto formale."""
    return f"Benvenuto {titolo} {nome}"


# Chiamata specificando solo il parametro obbligatorio
print(saluta_utente("Rossi"))  # "Benvenuto Sig./Sig.ra Rossi"

# Chiamata sovrascrivendo il valore di default
print(saluta_utente("Bianchi", "Dott."))  # "Benvenuto Dott. Bianchi"
```

---

## 4. Funzioni Pure vs Procedure

* **Funzione Pura:** Prende dei dati in ingresso, calcola e restituisce (`return`) un nuovo valore senza fare `print()` né modificare variabili esterne. È la tipologia migliore perché è facilissima da testare.
* **Procedura:** Esegue una serie di azioni (es. stampare un menu o pulire lo schermo) e termina senza restituire nulla (`-> None`).

```python
def mostra_menu_principale() -> None:
    """Procedura: si occupa solo della visualizzazione del menu."""
    print("=== GESTIONALE SCUOLA ===")
    print("1. Mostra studenti")
    print("2. Aggiungi voto")
    print("3. Esci")
```