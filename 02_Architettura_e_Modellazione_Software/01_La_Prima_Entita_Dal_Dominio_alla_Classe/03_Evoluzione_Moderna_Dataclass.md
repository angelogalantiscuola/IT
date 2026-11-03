# Evoluzione Moderna: Le `@dataclass` in Python

Nella lezione precedente abbiamo capito la meccanica di base:
1. `__init__` riceve i parametri e li assegna a `self.attributo`.
2. `__str__` serve a formattare l'oggetto quando facciamo `print()`.

Ma se una classe ha 6 o 8 attributi, scrivere `self.campo = campo` per ogni singola variabile diventa ripetitivo e lungo (*codice boilerplate*).

Python risolve questo problema con uno strumento moderno standard: il decoratore **`@dataclass`**.

---

## 1. Definire una Classe con `@dataclass`

Guarda lo stesso `Personaggio` riscritto con `@dataclass`:

```python
from dataclasses import dataclass


@dataclass
class Personaggio:
    """Rappresenta un eroe nel nostro gioco."""

    id: int
    nome: str
    livello: int = 1
    punti_vita: int = 100

    def presentati(self) -> str:
        return f"Sono {self.nome}, livello {self.livello} ({self.punti_vita} PV)."

    def subisci_danno(self, danno: int) -> None:
        if danno > 0:
            self.punti_vita -= danno
            if self.punti_vita < 0:
                self.punti_vita = 0
```

---

## 2. Cosa fa `@dataclass` Dietro le Quinte?

Ora che conosci la meccanica tradizionale di `__init__`, capisci esattamente cosa sta facendo Python per te:

1. **Genera il costruttore `__init__` in automatico:**
   Legge i tipi che hai dichiarato (`id: int`, `nome: str`...) e genera da solo il codice `self.id = id`, `self.nome = nome` in background.
2. **Genera una stampa leggibile (`__repr__`):**
   Se stampi l'oggetto con `print(eroe)`, Python mostra subito tutti i campi in modo chiaro:
   ```python
   eroe = Personaggio(1, "Aragorn", livello=5)
   print(eroe)
   # Output automatico: Personaggio(id=1, nome='Aragorn', livello=5, punti_vita=100)
   ```
3. **Genera il confronto di uguaglianza (`==`):**
   Due oggetti con gli stessi identici dati risulteranno uguali senza dover scrivere codice aggiuntivo:
   ```python
   p1 = Personaggio(1, "Aragorn")
   p2 = Personaggio(1, "Aragorn")
   print(p1 == p2)  # True!
   ```

---

## 3. Inizializzare Liste e Dizionari

Per un attributo semplice, come `livello: int = 1`, il valore predefinito può essere scritto direttamente. Liste e dizionari, invece, sono modificabili: un valore predefinito scritto direttamente potrebbe essere condiviso tra le istanze. Le versioni moderne di `dataclasses` rifiutano i default mutabili più comuni, come `[]` e `{}`, proprio per prevenire questo problema.

Con `field(default_factory=...)` chiediamo alla dataclass di creare una nuova lista o un nuovo dizionario ogni volta che costruiamo un oggetto:

```python
from dataclasses import dataclass, field


@dataclass
class Inventario:
    oggetti: list[str] = field(default_factory=list)
    quantita_per_oggetto: dict[str, int] = field(default_factory=dict)
```

`list` e `dict` sono funzioni senza parentesi: la dataclass le chiama per creare le collezioni vuote. Non scrivere `default_factory=list()` o `default_factory=dict()`: in quel caso passeresti il risultato della chiamata, non la funzione da chiamare per ogni istanza.

```python
zaino_eroe = Inventario()
zaino_compagno = Inventario()

zaino_eroe.oggetti.append("Pozione")
zaino_eroe.quantita_per_oggetto["Pozione"] = 2

print(zaino_eroe.oggetti)       # ['Pozione']
print(zaino_compagno.oggetti)   # []
print(zaino_compagno.quantita_per_oggetto)  # {}
```

Ogni oggetto riceve le proprie collezioni. Per questo non si scrivono valori predefiniti mutabili direttamente, come `oggetti: list[str] = []`: per liste e dizionari si usa `default_factory`.

Il costruttore generato accetta comunque collezioni iniziali, se vuoi fornirle tu:

```python
zaino = Inventario(oggetti=["Spada"], quantita_per_oggetto={"Pozione": 3})
```

## 4. Creare e Usare le Istanze

```python
# Creiamo due oggetti distinti
eroe1 = Personaggio(id=1, nome="Aragorn", livello=5)
eroe2 = Personaggio(id=2, nome="Legolas", livello=4, punti_vita=85)

# Chiamiamo i metodi esattamente come prima
eroe1.subisci_danno(40)
print(f"PV residui di {eroe1.nome}: {eroe1.punti_vita}")  # 60
print(f"PV di {eroe2.nome}: {eroe2.punti_vita}")  # 85 (intatto)
```

---

## 5. Collaudare con Pytest

I test scritti con `pytest` funzionano allo stesso identico modo:

```python
# tests/test_personaggio.py
from src.personaggio import Personaggio


def test_creazione_dataclass():
    eroe = Personaggio(id=1, nome="Gimli")
    assert eroe.id == 1
    assert eroe.livello == 1
    assert eroe.punti_vita == 100


def test_subisci_danno_dataclass():
    eroe = Personaggio(id=1, nome="Gimli")
    eroe.subisci_danno(30)
    assert eroe.punti_vita == 70
```

---

## 🎯 Perché useremo le `@dataclass` d'ora in avanti:
* **Il codice è pulito ed essenziale:** definisce le entità esattamente come appaiono nei diagrammi ER e UML.
* **Meno distrazioni sintattiche:** possiamo concentrarci sulle relazioni tra oggetti, sulla logica dei metodi e sull'architettura.