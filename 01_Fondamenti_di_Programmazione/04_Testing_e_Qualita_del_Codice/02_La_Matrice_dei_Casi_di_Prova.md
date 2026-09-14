# La Matrice dei Casi di Prova: Pensare Prima di Testare

Prima di scrivere codice di test con `pytest`, il lavoro più importante dello sviluppatore avviene nella mente (o su un foglio): **immaginare tutte le situazioni possibili in cui il programma verrà messo alla prova.**

Un test non serve a dimostrare che il programma funziona quando tutto va bene, ma a garantire che **non si rompa quando riceve dati imprevisti o estremi**.

---

## 1. Le 3 Categorie di Casi di Prova

Ogni funzione deve essere collaudata su tre tipologie di dati:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CASI TIPICI (Happy Path)                                 │
│    - Dati normali e corretti nel mezzo della scala          │
│    - Es. Calcolo sconto su 100€ con sconto del 20%          │
├─────────────────────────────────────────────────────────────┤
│ 2. CASI LIMITE / DI CONFINE (Edge Cases)                    │
│    - Valori esattamente sulle soglie di decisione (< vs <=) │
│    - Es. Sconto 0%, sconto 100%, età esattamente 18 anni    │
├─────────────────────────────────────────────────────────────┤
│ 3. CASI ANOMALI / STRANI (Corner Cases)                     │
│    - Liste vuote [], numeri negativi, zeri, testi vuoti ""  │
│    - Es. Prezzo negativo, divisione per zero                │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Esempio Pratico: La Funzione `valuta_voto`

Immagina di dover testare questa specifica:
> *"Data la media dei voti (da 0 a 10), restituisce 'Ottimo' se >= 8.0, 'Sufficiente' se tra 6.0 e 7.9, 'Insufficiente' se < 6.0. Se il voto è < 0 o > 10, restituisce 'Non Valido'."*

Compiliamo la **Matrice dei Casi di Prova**:

| Categoria | Input (`media`) | Output Atteso | Cosa stiamo collaudando? |
| :--- | :--- | :--- | :--- |
| **Tipico** | `8.5` | `"Ottimo"` | Funzionamento normale fascia alta |
| **Tipico** | `6.5` | `"Sufficiente"` | Funzionamento normale fascia media |
| **Tipico** | `4.0` | `"Insufficiente"` | Funzionamento normale fascia bassa |
| **Confine esatto** | `8.0` | `"Ottimo"` | Il punto esatto di passaggio a Ottimo |
| **Confine esatto** | `6.0` | `"Sufficiente"` | Il punto esatto di sufficienza |
| **Estremo** | `0.0` e `10.0` | Risultati corretti | I valori minimi e massimi possibili |
| **Anomalo** | `-1.0` o `11.5` | `"Non Valido"` | Input fuori scala |

---

## 3. Perché questa matrice è il miglior antidoto all'IA?

Quando chiedi a un'IA di scrivere una funzione, l'IA azzeccherà quasi sempre i **casi tipici**. Ma nell'80% dei casi sbaglierà i **casi di confine** (usando `<` invece di `<=`) o non gestirà i **casi anomali**.

Se hai compilato prima la tua matrice, puoi trasformarla istantaneamente in verifiche automatiche e scoprire se il codice è solido o fragile.