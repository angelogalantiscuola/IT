# Metodologia: La Scomposizione Top-Down a 3 Strati

Di fronte a un problema di programmazione complesso, i principianti cercano di scrivere tutto il codice in un unico blocco. Il risultato è un programma disordinato, difficile da leggere e pieno di bug.

La tecnica professionale per affrontare qualsiasi problema si chiama **Scomposizione Top-Down** (dall'alto verso il basso) ed è organizzata su **3 strati logici separati**.

---

## I 3 Strati di un Programma

```
┌─────────────────────────────────────────────────────────────┐
│ 1. STRATO I/O (Input / Validazione)                         │
│    - Chiede i dati all'utente con input()                   │
│    - Valida che siano corretti                              │
├─────────────────────────────────────────────────────────────┤
│ 2. STRATO LOGICA PURA (Il Cervello)                         │
│    - Riceve parametri ed esegue calcoli o classificazioni   │
│    - NON fa MAI input() né print()                          │
│    - Restituisce sempre il risultato con return             │
├─────────────────────────────────────────────────────────────┤
│ 3. STRATO PRESENTAZIONE (Output)                            │
│    - Riceve i risultati elaborati e li formatta a video     │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ Tutti coordinati da:
┌─────────────────────────────────────────────────────────────┐
│ 4. IL DIRETTORE D'ORCHESTRA (Funzione main())               │
│    - Chiama le funzioni nell'ordine corretto                │
└─────────────────────────────────────────────────────────────┘
```

---

## Esempio Pratico Guidato: Calcolatore Tariffa Parcheggio

> **Richiesta del committente:**
> *"Vogliamo un programma per un parcheggio. L'utente inserisce le ore di sosta e il tipo di veicolo ('auto' o 'moto'). La tariffa oraria è 2.50€ per le auto e 1.50€ per le moto. Se la sosta supera le 5 ore, si applica uno sconto forfettario del 10% sul totale. Il programma deve stampare un ticket dettagliato."*

---

### Passo 1: Progettare lo Strato Logica Pura (Il Cervello)
*Niente print, solo calcoli matematici con parametri e return.*

```python
def calcola_costo_base(ore: float, tipo_veicolo: str) -> float:
    """Calcola il costo orario base."""
    tariffa_oraria = 2.50 if tipo_veicolo.lower() == "auto" else 1.50
    return ore * tariffa_oraria


def applica_sconto_lunga_sosta(costo: float, ore: float) -> float:
    """Applica il 10% di sconto se la sosta supera 5 ore."""
    if ore > 5:
        return costo * 0.90
    return costo
```

---

### Passo 2: Progettare lo Strato I/O e Presentazione
*Si occupano solo di parlare con l'utente umano.*

```python
def chiedi_ore_sosta() -> float:
    """Chiede le ore e valida che siano positive."""
    while True:
        try:
            ore = float(input("Inserisci le ore di sosta: "))
            if ore > 0:
                return ore
            print("Errore: le ore devono essere maggiori di 0.")
        except ValueError:
            print("Errore: inserisci un numero valido.")


def stampa_ticket(ore: float, tipo: str, costo_finale: float) -> None:
    """Stampa lo scontrino formattato."""
    print("\n========= TICKET PARCHEGGIO =========")
    print(f"Veicolo:      {tipo.upper()}")
    print(f"Tempo sosta:  {ore:.1f} ore")
    print(f"TOTALE:       {costo_finale:.2f}€")
    print("=====================================\n")
```

---

### Passo 3: Il Direttore d'Orchestra (`main()`)
*Unisce i pezzi dall'alto verso il basso.*

```python
def main() -> None:
    print("Benvenuto nel Parcheggio Smart")
    tipo = input("Tipo di veicolo (auto/moto): ")
    ore = chiedi_ore_sosta()

    # Elaborazione logica pura
    costo_base = calcola_costo_base(ore, tipo)
    totale = applica_sconto_lunga_sosta(costo_base, ore)

    # Presentazione finale
    stampa_ticket(ore, tipo, totale)


if __name__ == "__main__":
    main()
```

---

## 🎯 Perché questo metodo è imbattibile?
1. **Facile da correggere:** Se il calcolo dello sconto è errato, modifichi solo `applica_sconto_lunga_sosta` senza toccare il resto del programma.
2. **Facile da testare:** Possiamo collaudare i calcoli matematici automaticamente con `pytest` perché le funzioni non aspettano l'`input()` dell'utente.
3. **Pronto per il futuro:** Se domani volessimo trasformare questo programma in un'app web (in 5ª), le funzioni di calcolo rimarranno identiche al 100%!