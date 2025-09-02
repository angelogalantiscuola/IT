# Lezione 1: Testare gli Oggetti con `pytest`

Abbiamo già visto nel corso precedente come testare le funzioni "pure", quelle che dato un input restituiscono semplicemente un output. Ma come si testa una classe, un'entità che ha uno **stato** interno che cambia nel tempo?

L'idea di base rimane la stessa: **Arrange, Act, Assert**.

1.  **Arrange:** Prepara l'oggetto da testare, creandone un'istanza.
2.  **Act:** Esegui un'azione sull'oggetto, chiamando uno dei suoi metodi.
3.  **Assert:** Verifica che lo stato dell'oggetto sia cambiato come previsto.

Vediamo come applicare questo schema ai nostri personaggi.

## 1. Testare il Costruttore (`__init__`)

Il primo test da scrivere per una classe è verificare che il costruttore inizializzi correttamente lo stato dell'oggetto.

**Codice da Testare (`Personaggio`)**
```python
class Personaggio:
    def __init__(self, nome: str, livello: int = 1):
        self.nome = nome
        self.__punti_vita = 100
        self.__livello = livello
```

**Test (`test_personaggio.py`)**
```python
from src.personaggio import Personaggio # Assumendo che il codice sia in src/

def test_costruttore_personaggio():
    # Arrange: crea un'istanza della classe
    eroe = Personaggio(nome="Aragorn", livello=5)

    # Act: nessuna azione necessaria, testiamo lo stato post-creazione

    # Assert: verifica che gli attributi siano stati impostati correttamente
    assert eroe.nome == "Aragorn"
    assert eroe.livello == 5
    assert eroe.punti_vita == 100 # Assumendo di avere una property "punti_vita"
```

## 2. Testare i Metodi che Modificano lo Stato

Questo è il tipo di test più comune in OOP. Verifichiamo che un'azione (un metodo) produca il risultato atteso sullo stato interno dell'oggetto.

**Codice da Testare (`Personaggio`)**
```python
class Personaggio:
    # ... init e property ...

    def subisci_danno(self, danno: int):
        self.punti_vita -= danno # Usa il setter della property

    def is_sconfitto(self) -> bool:
        return self.punti_vita == 0
```

**Test (`test_personaggio.py`)**

```python
def test_subisci_danno():
    # Arrange
    eroe = Personaggio(nome="Gimli", livello=8)
    
    # Act
    eroe.subisci_danno(30)
    
    # Assert
    assert eroe.punti_vita == 70

def test_sconfitta_personaggio():
    # Arrange
    eroe = Personaggio(nome="Boromir", livello=7)
    
    # Act
    eroe.subisci_danno(150) # Danno superiore ai PV iniziali
    
    # Assert
    assert eroe.is_sconfitto() is True
    assert eroe.punti_vita == 0 # Verifichiamo anche che il setter abbia impedito PV negativi
```

## 3. Testare le Properties (Logica di Validazione)

Se i nostri setter contengono logica di validazione (come nel caso di `punti_vita` che non possono scendere sotto zero), dobbiamo scrivere test specifici per assicurarci che quella logica funzioni. Il test `test_sconfitta_personaggio` già verifica implicitamente questo comportamento.

Il testing nella OOP non è più complicato, richiede solo di spostare l'attenzione dalla verifica del "valore di ritorno" alla verifica dello "stato dell'oggetto".