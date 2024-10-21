## Framework Pytest

Pytest è uno dei framework di testing più popolari e potenti per Python. Offre un approccio semplice ma flessibile per scrivere e eseguire test, rendendolo adatto sia per progetti piccoli che per quelli di grandi dimensioni.

### Introduzione a Pytest

Pytest è progettato per essere facile da usare, altamente configurabile e adatto a testare vari tipi di codice Python. Alcune delle sue caratteristiche principali includono:

- Sintassi semplice e intuitiva
- Rilevamento automatico dei test
- Fixture potenti per la gestione dello stato dei test
- Supporto per il parametrizzazione dei test
- Estensibilità attraverso i plugin

### Installazione

Per installare Pytest, puoi utilizzare pip:

```
pip install pytest
```

### Scrivere Test con Pytest

#### Convenzioni di Naming

Pytest segue alcune convenzioni per riconoscere automaticamente i file di test:

- I file di test dovrebbero iniziare o finire con `test_`
- Le funzioni di test dovrebbero iniziare con `test_`

#### Struttura Base di un Test

Ecco un esempio di un test semplice con Pytest:

```python
def test_somma():
    assert 1 + 1 == 2
```

Pytest utilizza la semplice keyword `assert` di Python per le verifiche, rendendo i test facili da leggere e scrivere.

### Esecuzione dei Test

Per eseguire i test, basta navigare nella directory del progetto e digitare:

```
pytest
```

Pytest cercherà automaticamente i file di test e li eseguirà.

### Fixture

Le fixture in Pytest sono un potente meccanismo per fornire dati o oggetti ai test:

```python
import pytest

@pytest.fixture
def numeri_esempio():
    return [1, 2, 3, 4, 5]

def test_somma_lista(numeri_esempio):
    assert sum(numeri_esempio) == 15
```

### Parametrizzazione dei Test

Pytest permette di eseguire lo stesso test con diversi input:

```python
import pytest

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
def test_incremento(input, expected):
    assert input + 1 == expected
```

### Asserzioni Avanzate

Pytest fornisce messaggi di errore dettagliati per le asserzioni fallite:

```python
def test_lista_uguaglianza():
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 4]
    assert lista1 == lista2
```

Se questo test fallisce, Pytest mostrerà una differenza dettagliata tra le due liste.

### Configurazione

Pytest può essere configurato usando un file `pytest.ini` o `conftest.py` per impostazioni più avanzate.

### Conclusione

Pytest offre un approccio moderno e flessibile al testing in Python. La sua semplicità d'uso, combinata con potenti funzionalità, lo rende una scelta eccellente per progetti di qualsiasi dimensione.
