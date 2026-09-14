# Metodologia AI: Il Pilota, il Copilota e il Detective del Codice

L'avvento dell'Intelligenza Artificiale (come GitHub Copilot o i modelli LLM) ha trasformato radicalmente il lavoro del programmatore. Oggi scrivere codice è diventato velocissimo, ma questo comporta una nuova e fondamentale responsabilità: **saper guidare l'IA e verificare criticamente tutto ciò che produce.**

---

## 1. La Regola Fondamentale: Pilota vs Copilota

Immagina di essere su un aereo:
* **Tu sei il Pilota:** Hai in mano i comandi, decidi la rotta, conosci la destinazione e sei il solo e unico responsabile della sicurezza del volo.
* **L'IA è il Copilota:** È un assistente instancabile che ti aiuta nelle operazioni ripetitive, ti suggerisce opzioni e consulta i manuali per te, ma **non decide mai cosa fare**.

> **Regola d'Oro:** La responsabilità del codice è **sempre e solo tua**. Se un programma contiene un bug o cancella dei dati, non puoi dire *"è colpa dell'IA"*. Se accetti una riga di codice, devi essere in grado di spiegarla riga per riga a voce.

```
                    ┌────────────────────────────────────────┐
                    │      TU (Il Pilota / Architetto)       │
                    │  - Definisci il problema               │
                    │  - Stabilisci cosa entra e cosa esce   │
                    │  - Verifichi e approvi il codice       │
                    └────────────────────────────────────────┘
                                        ▲
                                        │  Prompt chiari & Revisione
                                        ▼
                    ┌────────────────────────────────────────┐
                    │       L'IA (Il Copilota / Aiutante)    │
                    │  - Suggerisce la sintassi              │
                    │  - Evita lavoro ripetitivo (boilerplate)│
                    │  - Propone alternative di scrittura    │
                    └────────────────────────────────────────┘
```

---

## 2. Come Parlare all'IA: La Specifica Tecnica

L'IA non sa leggere nel pensiero. Se le fai una richiesta generica come *"calcolami lo sconto"*, l'IA inventerà regole arbitrarie.

Per ottenere codice di qualità devi fornirle una **specifica tecnica non ambigua**:
1. **Quali dati riceve in ingresso?** (Tipi e significato).
2. **Qual è la regola precisa di calcolo?**
3. **Cosa deve restituire in uscita?**
4. **Quali casi anomali deve gestire?**

### Esempio a confronto:
- ❌ **Prompt vago:** *"Fai una funzione per i biglietti del cinema."*
- ✅ **Specifica tecnica precisa:** 
  > *"Scrivi una funzione Python `calcola_biglietto(eta: int, giorno: str) -> float` che calcola il prezzo: tariffa base 8.50€, se l'età è minore di 14 o maggiore di 65 anni applica uno sconto del 30%, se il giorno è 'Mercoledì' tariffa fissa a 5.00€ per tutti. Se l'età è minore di 0, solleva un ValueError."*

---

## 3. Il Metodo del "Detective del Codice" (Code Review)

I modelli di intelligenza artificiale non "ragionano", ma generano testo in base a probabilità statistiche. Per questo motivo possono generare **allucinazioni** o codice che sembra perfetto a prima vista ma nasconde trappole logiche.

Prima di premere `Tab` per accettare un suggerimento, attiva la modalità **Detective** e poniti queste 3 domande:

```
┌────────────────────────────────────────────────────────────────────────────┐
│                  LE 3 DOMANDE DEL DETECTIVE DEL CODICE                     │
├────────────────────────────────────────────────────────────────────────────┤
│ 1. RISPETTA IL CONTRATTO?                                                  │
│    I tipi di input e il valore restituito sono esattamente quelli richiesti?│
├────────────────────────────────────────────────────────────────────────────┤
│ 2. HA GESTITO I CASI STRANI?                                               │
│    Cosa succede se la lista è vuota, il numero è zero o negativo?          │
├────────────────────────────────────────────────────────────────────────────┤
│ 3. CI SONO TRAPPOLE O COSE INUTILI?                                        │
│    Il codice tocca variabili esterne senza permesso? Ci sono righe oscure  │
│    che non so spiegare?                                                    │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Gli Anti-Pattern: Cosa NON Fare Mai

1. **Premere `Tab` a raffica:** Accettare codice senza averlo letto è il modo più rapido per riempire il progetto di bug incomprensibili.
2. **Incollare il testo del compito per farsi dare la soluzione completa:** In questo modo non alleni la mente a scomporre il problema e ti troverai bloccato alla prima verifica in classe o colloquio di lavoro.
3. **Chiedere "correggi l'errore" senza capire il perché:** Quando un programma fallisce, chiedi all'IA: *"Qual è la causa di questo messaggio di errore?"*, così impari a fare debug in autonomia.

---

## 5. Sintesi del Flusso di Lavoro Moderno

```
1. PENSA & SCOMPONI  ──>  2. SCRIVI IL CONTRATTO  ──>  3. SFRUTTA L'IA  ──>  4. FAI LA REVIEW (Detective)
   (Su carta o mente)        (Firme, Tipi, Docstring)      (Genera bozza)       (Verifica e correggi con Ruff)
```