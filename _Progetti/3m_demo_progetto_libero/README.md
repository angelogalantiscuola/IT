# 3M Demo Project: Quiz & Mini-Game

Questo è un esempio di progetto in Python pensato per gruppi di 3 studenti.

## Descrizione

Il programma è una console app con menu principale che permette di:
- giocare a un quiz a scelta multipla
- giocare a una sfida casuale con i dadi
- ricevere una barzelletta usando un package Python esterno

Questo esempio usa `pyjokes` come package esterno, ma ogni gruppo può scegliere un package diverso e applicarlo al proprio progetto.

## Struttura

- `main.py`: menu principale e flusso dell'app
- `quiz.py`: gestione delle domande e calcolo del punteggio
- `game.py`: mini-gioco basato sui dadi
- `utils.py`: funzioni di utilità per input sicuro e barre di progresso
- `requirements.txt`: package esterno richiesto
- `documento_requisiti_template.md`: modello di documento dei requisiti per il gruppo

## Requisiti

Installa il package richiesto con:

```bash
pip install -r requirements.txt
```

## Esecuzione

```bash
python main.py
```

## Suggerimento per i gruppi

Ogni squadra può cambiare il tema del progetto e scegliere un package diverso. Ad esempio:
- `pyjokes` per barzellette
- `colorama` per colorare l'output in console
- `tabulate` per stampare tabelle
- `faker` per generare dati di esempio
- `requests` per leggere dati da API

Nel documento dei requisiti, spiegate sempre quale package avete scelto e perché.
