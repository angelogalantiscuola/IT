## Magic Methods  <!-- omit in toc -->

- [1. `__init__`: Il Costruttore](#1-__init__-il-costruttore)
- [2. `__str__` e `__repr__`: Rappresentazione degli Oggetti](#2-__str__-e-__repr__-rappresentazione-degli-oggetti)
- [3. `__add__`, `__sub__`, `__mul__`: Operazioni Aritmetiche](#3-__add__-__sub__-__mul__-operazioni-aritmetiche)
- [4. `__eq__`, `__lt__`, `__le__`: Operazioni di Confronto](#4-__eq__-__lt__-__le__-operazioni-di-confronto)
- [Conclusioni](#conclusioni)


I **magic methods** (o metodi speciali) in Python sono metodi che hanno nomi speciali e che permettono di definire o modificare il comportamento predefinito degli oggetti. Questi metodi sono sempre racchiusi tra due doppi underscore (`__`), come `__init__`, e sono automaticamente chiamati in specifici contesti, come durante operazioni aritmetiche o confronti.

### 1. `__init__`: Il Costruttore

Il metodo `__init__` è probabilmente il magic method più conosciuto. Viene invocato automaticamente quando si crea un’istanza di una classe.

Esempio:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 2. `__str__` e `__repr__`: Rappresentazione degli Oggetti

Il metodo `__str__` viene usato per restituire una rappresentazione leggibile dell'oggetto, spesso utile quando si usa `print`. Il metodo `__repr__` invece restituisce una rappresentazione più dettagliata, pensata per essere utilizzata dai programmatori.

Esempio:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __str__(self):
        return f'Punto di coordinate ({self.x}, {self.y})'
```

Con `print()`, viene chiamato `__str__`, mentre con l’uso diretto in una console Python, viene chiamato `__repr__`.

### 3. `__add__`, `__sub__`, `__mul__`: Operazioni Aritmetiche

Python permette di sovraccaricare operatori aritmetici utilizzando magic methods come `__add__` per l’addizione, `__sub__` per la sottrazione, e `__mul__` per la moltiplicazione.

Esempio:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, altro):
        return Punto(self.x + altro.x, self.y + altro.y)
```

Ora possiamo sommare due oggetti di tipo `Punto` come fossero numeri:

```python
p1 = Punto(1, 2)
p2 = Punto(3, 4)
p3 = p1 + p2  # Invoca automaticamente __add__
print(p3)     # Output: Punto di coordinate (4, 6)
```

### 4. `__eq__`, `__lt__`, `__le__`: Operazioni di Confronto

Allo stesso modo, possiamo sovraccaricare gli operatori di confronto usando magic methods come `__eq__` (uguaglianza), `__lt__` (minore di), e `__le__` (minore o uguale).

Esempio:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, altro):
        return self.x == altro.x and self.y == altro.y
```

Ora possiamo confrontare due oggetti di tipo `Punto`:

```python
p1 = Punto(1, 2)
p2 = Punto(1, 2)
print(p1 == p2)  # Output: True
```

### Conclusioni

I magic methods permettono di rendere le classi Python più potenti e flessibili, consentendo di modificare il comportamento degli oggetti in modo elegante e conciso. Questo rende possibile l'uso di sintassi più naturale e migliora la leggibilità del codice.