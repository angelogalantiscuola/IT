# Mettere Tutto Insieme: Lavorare con Dati Strutturati

Abbiamo imparato i pattern di problem-solving e di manipolazione dei dati. Ora applichiamoli a uno scenario realistico: analizzare dati provenienti da un file esterno, come un file CSV o JSON.

### Lo Scenario
Immaginiamo di essere i gestori di un piccolo e-commerce e di avere un file `ordini.csv` con i dati delle vendite. Il nostro obiettivo è scrivere uno script Python che legga questo file e produca un piccolo report.

**Contenuto del file `ordini.csv`:**
```csv
id_ordine,prodotto,categoria,quantita,prezzo_unitario
1,Laptop,Elettronica,1,1200
2,Tastiera,Elettronica,2,80
3,Libro Python,Libri,5,35
4,Webcam,Elettronica,1,50
5,Libro SQL,Libri,3,30
```

**Il nostro compito è rispondere a queste domande:**
1.  Qual è il ricavo totale di tutte le vendite?
2.  Quanti prodotti della categoria "Libri" sono stati venduti in totale?
3.  Qual è l'ordine con il ricavo più alto?

### Il Processo: Leggere, Analizzare, Stampare

Il nostro script seguirà tre passaggi, proprio come abbiamo imparato:
1.  **Leggere:** Aprire il file `ordini.csv` e caricare i dati in una struttura dati comoda (una lista di dizionari).
2.  **Analizzare:** Applicare i pattern di manipolazione (aggregazione, filtraggio, ricerca) per calcolare le risposte.
3.  **Stampare:** Mostrare i risultati in un report leggibile.

### Il Codice Completo

```python
import csv

NOME_FILE = 'ordini.csv'

# --- 1. FASE DI LETTURA ---
def carica_ordini(nome_file: str) -> list[dict]:
    """Legge un file CSV e lo converte in una lista di dizionari."""
    ordini = []
    try:
        with open(nome_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for riga in reader:
                # Converte i valori numerici da stringa a numero
                riga['quantita'] = int(riga['quantita'])
                riga['prezzo_unitario'] = int(riga['prezzo_unitario'])
                ordini.append(riga)
    except FileNotFoundError:
        print(f"Errore: il file {nome_file} non è stato trovato.")
    return ordini

# --- 2. FASE DI ANALISI ---
def analizza_dati(ordini: list[dict]):
    """Esegue tutte le analisi e restituisce i risultati."""
    # Domanda 1: Ricavo totale (Aggregazione)
    ricavo_totale = 0
    for ordine in ordini:
        ricavo_totale += ordine['quantita'] * ordine['prezzo_unitario']

    # Domanda 2: Quantità totale libri (Filtraggio + Aggregazione)
    quantita_libri = 0
    for ordine in ordini:
        if ordine['categoria'] == 'Libri':
            quantita_libri += ordine['quantita']

    # Domanda 3: Ordine con ricavo più alto (Ricerca)
    ordine_piu_ricco = None
    ricavo_massimo = -1
    for ordine in ordini:
        ricavo_ordine = ordine['quantita'] * ordine['prezzo_unitario']
        if ricavo_ordine > ricavo_massimo:
            ricavo_massimo = ricavo_ordine
            ordine_piu_ricco = ordine
            
    return {
        "ricavo_totale": ricavo_totale,
        "quantita_libri": quantita_libri,
        "ordine_piu_ricco": ordine_piu_ricco
    }

# --- 3. FASE DI STAMPA ---
def stampa_report(risultati: dict):
    """Stampa i risultati in un formato leggibile."""
    print("--- Report Analisi Vendite ---")
    print(f"Ricavo totale: {risultati['ricavo_totale']}€")
    print(f"Totale libri venduti: {risultati['quantita_libri']}")
    if risultati['ordine_piu_ricco']:
        prodotto = risultati['ordine_piu_ricco']['prodotto']
        ricavo = risultati['ordine_piu_ricco']['quantita'] * risultati['ordine_piu_ricco']['prezzo_unitario']
        print(f"L'ordine più redditizio è stato per '{prodotto}' con un ricavo di {ricavo}€.")
    print("----------------------------")

# --- PROGRAMMA PRINCIPALE ---
def main():
    """Orchestra l'esecuzione del programma."""
    ordini_caricati = carica_ordini(NOME_FILE)
    if ordini_caricati:
        risultati_analisi = analizza_dati(ordini_caricati)
        stampa_report(risultati_analisi)

# Esecuzione
if __name__ == "__main__":
    main()
```
Questo esempio finale dimostra come i semplici pattern che abbiamo studiato possano essere combinati per creare script di analisi dati potenti e utili.