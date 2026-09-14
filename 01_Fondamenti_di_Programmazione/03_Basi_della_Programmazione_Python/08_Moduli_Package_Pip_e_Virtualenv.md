# Organizzazione del Codice: Moduli, Package, Pip e Ambienti Virtuali

Quando un progetto cresce, non possiamo tenere tutto in un unico file. Dobbiamo imparare a dividere il codice e a usare librerie esterne in modo sicuro e isolato.

---

## 1. Moduli Locali: Dividere il Codice in File (`.py`)

Un **modulo** è semplicemente un file Python contenente funzioni e variabili che possono essere importate in altri file.

* **File `geometria.py`:**
  ```python
  def calcola_area_cerchio(raggio: float) -> float:
      return 3.14159 * (raggio**2)
  ```

* **File `main.py` (nella stessa cartella):**
  ```python
  import geometria

  area = geometria.calcola_area_cerchio(5.0)
  print(f"Area: {area}")
  ```

---

## 2. Package: Cartelle di Moduli con `__init__.py`

Un **package** è una cartella che raggruppa moduli correlati. Per indicare a Python che una cartella è un package, si inserisce al suo interno un file speciale chiamato `__init__.py` (anche vuoto).

```text
mio_progetto/
├── main.py
└── calcoli/               <-- Package
    ├── __init__.py
    ├── finanza.py         <-- Modulo
    └── statistica.py      <-- Modulo
```

Importazione nel `main.py`:
```python
from calcoli.statistica import calcola_media
```

---

## 3. Librerie Esterne e `pip`

Oltre alla libreria standard di Python, possiamo usare migliaia di librerie create dalla community open source pubblicate su **PyPI** (Python Package Index).

Per installare librerie esterne si usa il gestore **`pip`** da terminale:
```bash
pip install requests
```

---

## 4. L'Ambiente Virtuale (`venv`): La Scatola Isolata del Progetto

Cosa succede se il *Progetto A* richiede la versione 2.0 di una libreria e il *Progetto B* richiede la versione 3.0? Se installiamo tutto globalmente sul computer, si creano conflitti distruttivi.

Un **ambiente virtuale (`venv`)** è una cartella isolata dedicata a un singolo progetto, contenente una copia dell'interprete Python e delle sole librerie necessarie a quel progetto.

```
IL TUO COMPUTER
├── Progetto 1 (.venv isolato) -> usa pytest 7.0
└── Progetto 2 (.venv isolato) -> usa flask 3.0
```

---

## 5. Guida Pratica: Creare e Attivare il tuo `venv`

### Passo 1: Creazione
Posizionati nella cartella del progetto dal terminale ed esegui:
```bash
python -m venv .venv
```
*(Verrà creata una cartella nascosta `.venv` contenente l'ambiente).*

### Passo 2: Attivazione
* **Su Linux / macOS / WSL:**
  ```bash
  source .venv/bin/activate
  ```
* **Su Windows (Git Bash o Command Prompt):**
  ```bash
  source .venv/Scripts/activate
  ```

*(Quando l'ambiente è attivo, vedrai la scritta `(.venv)` all'inizio della riga di comando).*

### Passo 3: Installazione Librerie
Ora qualsiasi installazione con `pip` andrà a finire **solo dentro la scatola del tuo progetto**:
```bash
pip install pytest
```

### Passo 4: Disattivazione
Quando finisci di lavorare:
```bash
deactivate
```

---

## 🎯 Sintesi:
* **Modulo:** un singolo file `.py`.
* **Package:** una cartella di moduli con `__init__.py`.
* **Pip:** lo strumento per scaricare pacchetti esterni.
* **Venv:** la cartella isolata dove installare i pacchetti senza sporcare il sistema operativo.