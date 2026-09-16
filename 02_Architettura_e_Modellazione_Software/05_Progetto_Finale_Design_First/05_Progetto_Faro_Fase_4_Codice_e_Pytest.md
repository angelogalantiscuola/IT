# Progetto Faro - Fase 4: Implementazione in Python e Suite Pytest

Ora traduciamo tutti i modelli e le sequenze in codice Python pulito, organizzato nelle cartelle `src/` e `tests/`.

```text
progetto_rpg/
├── src/
│   ├── __init__.py
│   ├── modello.py              <-- Classi di dominio con @dataclass
│   └── gestore_salvataggi.py   <-- Modulo di persistenza JSON
└── tests/
    ├── __init__.py
    └── test_rpg.py             <-- Suite di collaudo con Pytest (US-01, 02, 03, 04)
```

---

## 1. Il Modello di Dominio (`src/modello.py`)

```python
# src/modello.py
from dataclasses import dataclass, field

@dataclass
class Oggetto:
    """Rappresenta un item trasportabile (arma, pozione)."""
    id: int
    nome: str
    tipo: str
    valore_effetto: int

@dataclass
class Inventario:
    """Rappresenta lo zaino dell'eroe (Relazione 1:1 con Personaggio e 1:N con Oggetto)."""
    id: int
    capacita_slot: int = 20
    oggetti: list[Oggetto] = field(default_factory=list)

    def aggiungi(self, ogg: Oggetto) -> bool:
        """Aggiunge un oggetto se c'è spazio disponibile (US-01)."""
        if len(self.oggetti) >= self.capacita_slot:
            return False
        self.oggetti.append(ogg)
        return True

@dataclass
class Personaggio:
    """Classe base per tutti gli eroi del gioco."""
    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100
    inventario: Inventario | None = None

    def subisci_danno(self, danno: int) -> None:
        """Riduce i punti vita garantendo che non vadano sotto zero."""
        if danno > 0:
            self.punti_vita = max(0, self.punti_vita - danno)

    def attacca(self, bersaglio: "Personaggio") -> str:
        """Attacco base generico."""
        danno = 10
        bersaglio.subisci_danno(danno)
        return f"{self.nome} attacca {bersaglio.nome} infliggendo {danno} danni."

    def raccogli_oggetto(self, ogg: Oggetto) -> bool:
        """Delega la raccolta al proprio inventario se presente (US-01)."""
        if self.inventario is None:
            return False
        return self.inventario.aggiungi(ogg)

@dataclass
class Guerriero(Personaggio):
    """Specializzazione fisica del Personaggio (Relazione IS-A, US-02)."""
    forza: int = 5

    def attacca(self, bersaglio: Personaggio) -> str:
        """Override del metodo attacca: calcola il danno sommando la forza fisica."""
        danno_totale = 10 + self.forza
        bersaglio.subisci_danno(danno_totale)
        return f"⚔️ {self.nome} sferra un fendente da {danno_totale} danni a {bersaglio.nome}!"

@dataclass
class Abilita:
    """Rappresenta una tecnica o magia nel gioco."""
    id: int
    nome_abilita: str
    costo_mana: int

@dataclass
class AbilitaAppresa:
    """Entità di raccordo per la relazione N:N tra Personaggio e Abilita (US-03)."""
    id: int
    personaggio: Personaggio
    abilita: Abilita
    livello_maestria: int = 1

    def potenzia(self) -> None:
        """Aumenta il livello di maestria dell'abilità fino a un massimo di 5."""
        if self.livello_maestria < 5:
            self.livello_maestria += 1
```

---

## 2. Il Modulo di Persistenza (`src/gestore_salvataggi.py`)

```python
# src/gestore_salvataggi.py
import json
from dataclasses import asdict
from src.modello import Personaggio, Guerriero, Inventario, Oggetto

def salva_partita(eroe: Personaggio, percorso_file: str) -> None:
    """Salva lo stato completo dell'eroe e dell'inventario su file JSON (US-04)."""
    dati = asdict(eroe)
    # Tracciamo se l'eroe è un Guerriero per ricostruire la classe corretta
    dati["is_guerriero"] = isinstance(eroe, Guerriero)

    with open(percorso_file, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4)

def carica_partita(percorso_file: str) -> Personaggio:
    """Legge il file JSON e ricostruisce l'intero grafo di oggetti in RAM (US-04)."""
    with open(percorso_file, "r", encoding="utf-8") as f:
        dati = json.load(f)

    # Estraiamo i campi speciali
    dati_inv = dati.pop("inventario", None)
    is_guerriero = dati.pop("is_guerriero", False)

    # 1. Ricostruzione dell'Inventario e della lista di Oggetti
    inventario_ricostruito = None
    if dati_inv:
        oggetti_dati = dati_inv.pop("oggetti", [])
        oggetti_ricostruiti = [Oggetto(**ogg) for ogg in oggetti_dati]
        inventario_ricostruito = Inventario(**dati_inv, oggetti=oggetti_ricostruiti)

    # 2. Ricostruzione dell'istanza esatta dell'Eroe
    if is_guerriero:
        return Guerriero(**dati, inventario=inventario_ricostruito)
    return Personaggio(**dati, inventario=inventario_ricostruito)
```

---

## 3. La Suite di Collaudo Pytest (`tests/test_rpg.py`)

Ogni test corrisponde esattamente a una delle 4 User Stories formalizzate nella Fase 1:

```python
# tests/test_rpg.py
import os
from src.modello import Personaggio, Guerriero, Inventario, Oggetto, Abilita, AbilitaAppresa
from src.gestore_salvataggi import salva_partita, carica_partita

# --- COLLAUDO US-01: GESTIONE INVENTARIO ---
def test_us01_inventario_e_capienza_massima():
    conan = Personaggio(id=1, nome="Conan")
    conan.inventario = Inventario(id=101, capacita_slot=2)

    pozione = Oggetto(id=10, nome="Pozione di Cura", tipo="Consumabile", valore_effetto=30)
    spada = Oggetto(id=20, nome="Spada Lunga", tipo="Arma", valore_effetto=15)
    scudo = Oggetto(id=30, nome="Scudo", tipo="Armatura", valore_effetto=10)

    # Raccogliamo i primi due oggetti (spazio sufficiente)
    assert conan.raccogli_oggetto(pozione) is True
    assert conan.raccogli_oggetto(spada) is True
    assert len(conan.inventario.oggetti) == 2

    # Proviamo ad aggiungere il terzo (zaino pieno!)
    assert conan.raccogli_oggetto(scudo) is False
    assert len(conan.inventario.oggetti) == 2

# --- COLLAUDO US-02: COMBATTIMENTO E POLIMORFISMO GUERRIERO ---
def test_us02_combattimento_guerriero_calcola_forza():
    guerriero = Guerriero(id=1, nome="Conan", forza=8)
    mostro = Personaggio(id=99, nome="Goblin", punti_vita=50)

    messaggio = guerriero.attacca(mostro)

    # Danno atteso: 10 base + 8 forza = 18 danni
    assert mostro.punti_vita == 32
    assert "⚔️" in messaggio

def test_us02_danno_mortale_blocca_punti_vita_a_zero():
    guerriero = Guerriero(id=1, nome="Conan", forza=50)
    mostro = Personaggio(id=99, nome="Goblin", punti_vita=20)

    guerriero.attacca(mostro)
    # I punti vita non devono essere negativi
    assert mostro.punti_vita == 0

# --- COLLAUDO US-03: APPRENDIMENTO E POTENZIAMENTO ABILITÀ ---
def test_us03_apprendimento_e_potenziamento_abilita():
    mago = Personaggio(id=2, nome="Merlino")
    fuoco = Abilita(id=10, nome_abilita="Palla di Fuoco", costo_mana=25)

    legame = AbilitaAppresa(id=101, personaggio=mago, abilita=fuoco, livello_maestria=1)

    assert legame.personaggio.nome == "Merlino"
    assert legame.abilita.nome_abilita == "Palla di Fuoco"
    assert legame.livello_maestria == 1

    # Potenziamo l'abilità
    legame.potenzia()
    assert legame.livello_maestria == 2

    # Verifichiamo che il livello non superi 5
    for _ in range(10):
        legame.potenzia()
    assert legame.livello_maestria == 5

# --- COLLAUDO US-04: PERSISTENZA E RICARICAMENTO JSON ---
def test_us04_salvataggio_e_ricaricamento_completo():
    file_test = "test_salvataggio_partita.json"

    # Preparazione dell'eroe completo
    eroe_originale = Guerriero(id=1, nome="Aragorn", forza=6, punti_vita=85)
    eroe_originale.inventario = Inventario(id=101, capacita_slot=5)
    eroe_originale.raccogli_oggetto(Oggetto(id=1, nome="Pozione", tipo="Cura", valore_effetto=20))

    # Salvataggio
    salva_partita(eroe_originale, file_test)

    # Ricaricamento
    eroe_ricaricato = carica_partita(file_test)

    # Verifiche di integrità dello stato
    assert isinstance(eroe_ricaricato, Guerriero)
    assert eroe_ricaricato.id == 1
    assert eroe_ricaricato.nome == "Aragorn"
    assert eroe_ricaricato.forza == 6
    assert eroe_ricaricato.punti_vita == 85
    assert eroe_ricaricato.inventario is not None
    assert len(eroe_ricaricato.inventario.oggetti) == 1
    assert eroe_ricaricato.inventario.oggetti[0].nome == "Pozione"

    # Pulizia del file temporaneo
    if os.path.exists(file_test):
        os.remove(file_test)
```

---

## 🚀 Esecuzione dei Test e Collaudo Finale

Nel terminale lanciamo la suite:

```bash
pytest
```

```text
============================= test session starts ==============================
collected 5 items

tests/test_rpg.py .....                                                  [100%]

============================== 5 passed in 0.04s ===============================
```

Tutte le 4 User Stories sono verificate e collaudate al 100%!