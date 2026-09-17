# La Pipeline Completa: Da File CSV a Report di Business

Mettiamo insieme tutti i concetti appresi: lettura da file, gestione delle eccezioni, scomposizione modulare e pattern su liste e dizionari.

---

## Lo Scenario Reale
Gestiamo un piccolo e-commerce. Abbiamo un file `ordini.csv` con lo storico delle vendite e dobbiamo realizzare un programma che generi un report riassuntivo per il responsabile commerciale.

### Contenuto del file `ordini.csv`:
```csv
id_ordine,prodotto,categoria,quantita,prezzo_unitario
1,Laptop,Informatica,1,1200.0
2,Tastiera,Informatica,2,80.0
3,Manuale Python,Libri,5,35.0
4,Webcam,Informatica,1,50.0
5,Manuale SQL,Libri,3,30.0
```

---

## Il Codice Completo e Modulare

```python
import csv


# --- 1. STRATO I/O (Caricamento Dati) ---
def carica_ordini(percorso_file: str) -> list[dict]:
    """Legge il file CSV e restituisce una lista di record convertiti."""
    ordini: list[dict] = []
    try:
        with open(percorso_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for riga in reader:
                ordini.append(
                    {
                        "id": int(riga["id_ordine"]),
                        "prodotto": riga["prodotto"],
                        "categoria": riga["categoria"],
                        "quantita": int(riga["quantita"]),
                        "prezzo_unitario": float(riga["prezzo_unitario"]),
                    }
                )
    except FileNotFoundError:
        print(f"Errore: il file '{percorso_file}' non esiste.")
    return ordini


# --- 2. STRATO LOGICA PURA (Pattern di Elaborazione) ---
def calcola_incasso_totale(ordini: list[dict]) -> float:
    """Aggregazione: calcola il fatturato totale."""
    totale = 0.0
    for o in ordini:
        totale += o["quantita"] * o["prezzo_unitario"]
    return totale


def conta_pezzi_per_categoria(ordini: list[dict], categoria: str) -> int:
    """Filtraggio + Aggregazione: somma i pezzi venduti per una data categoria."""
    pezzi = 0
    for o in ordini:
        if o["categoria"].lower() == categoria.lower():
            pezzi += o["quantita"]
    return pezzi


def trova_ordine_piu_redditizio(ordini: list[dict]) -> dict | None:
    """Ricerca del massimo: individua l'ordine con il ricavo maggiore."""
    if not ordini:
        return None

    migliore = ordini[0]
    ricavo_max = migliore["quantita"] * migliore["prezzo_unitario"]

    for o in ordini:
        ricavo_attuale = o["quantita"] * o["prezzo_unitario"]
        if ricavo_attuale > ricavo_max:
            ricavo_max = ricavo_attuale
            migliore = o

    return migliore


# --- 3. STRATO PRESENTAZIONE (Stampa Report) ---
def stampa_report_vendite(incasso: float, pezzi_libri: int, top_ordine: dict | None) -> None:
    """Formatta e visualizza il report finale."""
    print("\n==========================================")
    print("       REPORT COMMERCIALE VENDITE         ")
    print("==========================================")
    print(f"Fatturato Complessivo:       {incasso:.2f}€")
    if pezzi_libri > 0:
        print(f"Totale Libri Venduti:        {pezzi_libri} copie")
    else:
        print("Totale Libri Venduti:        Nessun libro")

    if top_ordine:
        ricavo = top_ordine["quantita"] * top_ordine["prezzo_unitario"]
        print(f"Miglior Ordine:              '{top_ordine['prodotto']}' ({ricavo:.2f}€)")
    print("==========================================\n")


# --- 4. ORCHESTRAZIONE (main) ---
def main() -> None:
    dati_ordini = carica_ordini("ordini.csv")
    if not dati_ordini:
        return

    # Calcoli logici
    incasso = calcola_incasso_totale(dati_ordini)
    totale_libri = conta_pezzi_per_categoria(dati_ordini, "Libri")
    miglior_ordine = trova_ordine_piu_redditizio(dati_ordini)

    # Presentazione
    stampa_report_vendite(incasso, totale_libri, miglior_ordine)


if __name__ == "__main__":
    main()
```