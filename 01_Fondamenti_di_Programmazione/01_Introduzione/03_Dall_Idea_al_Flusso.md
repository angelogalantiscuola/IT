# Metodologia: Dall'Idea al Flusso (Input $\to$ Elaborazione $\to$ Output)

Quando si riceve una richiesta o un problema di programmazione, **l'errore più comune è iniziare subito a digitare codice**.

I programmatori professionisti non toccano la tastiera finché non hanno chiaro lo schema di trasformazione dei dati.

---

## Il Modello a 3 Fasi: I-E-O

Qualsiasi problema software può essere diviso in tre blocchi logici:

```
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│        1. INPUT         │     │     2. ELABORAZIONE     │     │        3. OUTPUT        │
│  Quali dati entrano?    │ ──> │   Come li trasformo?    │ ──> │   Cosa devo mostrare    │
│  Di che tipo sono?      │     │   (Calcoli, if, cicli)  │     │   o restituire?         │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

---

## Esempio Guidato: Il Calcolatore di Spese

> **Richiesta del committente:**
> *"Abbiamo una lista di scontrini di un viaggio. Vogliamo calcolare la spesa totale, verificare se abbiamo superato il budget di 150€ e avvisare l'utente."*

### Passo 1: Individuare l'INPUT
- Una lista di numeri decimali rappresentanti le spese (`spese: list[float]`).
- Una soglia numerica di budget (`budget: float = 150.0`).

### Passo 2: Progettare l'ELABORAZIONE (I Passaggi Logici)
1. Creo una variabile `totale = 0.0`.
2. Scorro ogni spesa nella lista e la sommo a `totale`.
3. Confronto: `totale > budget`?
   - Se sì: calcolo di quanto abbiamo sforato (`totale - budget`).

### Passo 3: Definire l'OUTPUT
- Mostrare la spesa complessiva formattata in Euro.
- Se nei limiti: stampare messaggio di conferma verde.
- Se fuori budget: stampare allarme con la cifra esatta dello sforamento.

---

## Traduzione in Codice

Solo dopo aver chiarito la tabella I-E-O passiamo al codice Python:

```python
# 1. INPUT
spese: list[float] = [34.50, 12.00, 89.90, 45.00]
budget: float = 150.0

# 2. ELABORAZIONE
totale_speso: float = 0.0
for spesa in spese:
    totale_speso += spesa

ha_sforato: bool = totale_speso > budget

# 3. OUTPUT
print(f"Totale speso: {totale_speso:.2f}€")

if ha_sforato:
    sforamento = totale_speso - budget
    print(f"⚠️ Attenzione! Budget superato di {sforamento:.2f}€")
else:
    rimanente = budget - totale_speso
    print(f"✅ Ottimo! Sei nel budget. Ti restano {rimanente:.2f}€")
```

---

## 🎯 Regola Aurea del Problem Solving:
Prima di scrivere anche una sola riga di codice, rispondi sempre per iscritto a queste 3 domande:
1. *Cosa deve entrare nel programma?*
2. *Qual è la sequenza logica dei passaggi per trasformare i dati?*
3. *Cosa deve comparire sullo schermo come risultato finale?*