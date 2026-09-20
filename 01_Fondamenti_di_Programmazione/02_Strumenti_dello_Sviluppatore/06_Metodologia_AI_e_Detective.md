# Metodologia AI: Il Pilota, il Copilota e il Detective del Codice

L'avvento dell'Intelligenza Artificiale (come GitHub Copilot o i modelli LLM) ha trasformato radicalmente il lavoro del programmatore. Oggi scrivere codice è diventato velocissimo, ma questo comporta una nuova e fondamentale responsabilità: **saper guidare l'IA e verificare criticamente tutto ciò che produce.**

## Metodologia AI: il Pilota e il Detective del Codice

L'Intelligenza Artificiale rende più veloce la scrittura del codice, ma non sostituisce la responsabilità del programmatore: ogni risultato va compreso e verificato.

## 1. Tu sei il Pilota

L'IA è un **copilota**: suggerisce codice, propone alternative e aiuta nelle operazioni ripetitive. Tu, invece, definisci il problema, scegli la soluzione e approvi il risultato.

> **Regola d'oro:** se accetti una riga di codice, devi essere in grado di spiegarla. Un bug o una perdita di dati restano responsabilità tua, non dell'IA.

## 2. Scrivi una specifica chiara

L'IA non legge nel pensiero. Un prompt utile indica:

1. quali dati riceve in ingresso;
2. quale regola deve applicare;
3. cosa deve restituire;
4. quali casi anomali deve gestire.

### Esempio

- ❌ **Prompt vago:** «Fai una funzione per i biglietti del cinema.»
- ✅ **Prompt preciso:** «Scrivi una funzione Python `calcola_biglietto(eta: int, giorno: str) -> float`. Il prezzo base è 8.50 euro; sotto i 14 o sopra i 65 anni applica uno sconto del 30%; il mercoledì il prezzo è 5.00 euro per tutti; per un'età negativa solleva `ValueError`.»

## 3. Diventa Detective del Codice

Il codice generato può sembrare corretto e contenere comunque errori. Prima di accettarlo, verifica:

1. **Rispetta il contratto?** Gli input e il valore restituito sono quelli richiesti?
2. **Gestisce i casi limite?** Cosa succede con una lista vuota, uno zero o un valore negativo?
3. **È comprensibile?** Sai spiegare ogni riga? Usa variabili esterne o contiene codice inutile?

## In sintesi

**Pensa e scomponi il problema → scrivi una specifica → usa l'IA per una bozza → verifica e correggi il codice.**