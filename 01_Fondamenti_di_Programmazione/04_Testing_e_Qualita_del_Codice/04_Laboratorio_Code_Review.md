# Laboratorio di Code Review: Il Detective del Codice in Azione

Nel lavoro reale si passa molto più tempo a **leggere, revisionare e collaudare codice scritto da altri** (o generato da strumenti di IA) che a scriverlo da zero.

In questa lezione faremo una sessione di **Code Review** su un problema pratico.

---

## Lo Scenario

> **Requisito richiesto:**
> *"Scrivere una funzione `trova_studenti_sufficienti(studenti: list[dict]) -> list[str]` che riceve una lista di schede studente `{"nome": str, "voto": float}` e restituisce una NUOVA lista contenente SOLO i nomi degli studenti con voto >= 6.0. La lista originale non deve subire alterazioni."*

Tre sviluppatori (o tre prompt di IA) hanno proposto tre soluzioni differenti. Facciamo il collaudo!

---

## Candidato 1: La Soluzione Distruttiva ❌

```python
def trova_studenti_sufficienti_v1(studenti: list[dict]) -> list[str]:
    nomi = []
    for s in studenti:
        if s["voto"] < 6.0:
            studenti.remove(s)  # <-- TRAPPOLA! Modifica la lista originale in-place
        else:
            nomi.append(s["nome"])
    return nomi
```

### Verdetto del Detective:
1. **Errore di Mutabilità (Side-Effect grave):** La funzione usa `.remove()` sulla lista in ingresso, cancellando gli studenti bocciati dai dati originali di chi ha chiamato la funzione.
2. **Bug di Iterazione:** Modificare una lista mentre la si sta ciclando con un `for` fa saltare degli elementi durante lo scorrimento!
3. **Esito:** **BOCCIATA.**

---

## Candidato 2: La Soluzione Cieca sui Dati Limite ⚠️

```python
def trova_studenti_sufficienti_v2(studenti: list[dict]) -> list[str]:
    nomi = []
    for s in studenti:
        if s["voto"] > 6.0:  # <-- TRAPPOLA! Ha usato > invece di >=
            nomi.append(s["nome"])
    return nomi
```

### Verdetto del Detective:
1. **Errore sui Casi di Confine:** Lo studente che ha preso esattamente `6.0` viene escluso! Il requisito chiedeva `>= 6.0`.
2. **Esito:** **DA CORREGGERE (Errore logico di specifica).**

---

## Candidato 3: La Soluzione Pulita e Robusta ✅

```python
def trova_studenti_sufficienti_v3(studenti: list[dict]) -> list[str]:
    """Filtra gli studenti con voto sufficiente senza alterare i dati in ingresso."""
    promossi: list[str] = []
    for s in studenti:
        if s.get("voto", 0.0) >= 6.0:
            promossi.append(s["nome"])
    return promossi
```

### Verdetto del Detective:
1. Rispetta la condizione di confine (`>= 6.0`).
2. Non modifica la lista di partenza (crea una nuova lista `promossi`).
3. Usa `.get("voto", 0.0)` proteggendosi dal caso anomalo in cui un record non abbia la chiave `"voto"`.
4. **Esito:** **APPROVATA AL 100%.**

---

## La Suite di Test di Validazione

Ecco i test `pytest` che smascherano all'istante i problemi dei Candidati 1 e 2:

```python
# tests/test_studenti.py


def test_inclusione_sufficienza_esatta():
    dati = [{"nome": "Marco", "voto": 6.0}, {"nome": "Anna", "voto": 5.5}]
    # Il Candidato 2 fallirà qui!
    assert trova_studenti_sufficienti_v3(dati) == ["Marco"]


def test_rispetto_dati_originali():
    dati_originali = [{"nome": "Luca", "voto": 4.0}, {"nome": "Sara", "voto": 8.0}]
    copia_controllo = dati_originali.copy()

    trova_studenti_sufficienti_v3(dati_originali)

    # Il Candidato 1 fallirà qui perché ha alterato dati_originali!
    assert dati_originali == copia_controllo
```

---

## 🎯 La Lezione del Detective:
> *"Non fidarti del codice solo perché non dà errori di sintassi. Il buon codice rispetta i confini della specifica e non tocca mai i dati di chi lo circonda."*