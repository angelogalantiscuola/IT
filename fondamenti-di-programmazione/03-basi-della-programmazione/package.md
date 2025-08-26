### Cosa è un Package Python

Un package Python è:

1. **Struttura Organizzativa**
- Una collezione organizzata di moduli Python correlati
- Una directory che contiene più moduli .py
- Un modo per creare namespace gerarchici, ovvero:
  - Organizza il codice in "spazi dei nomi" annidati
  - Permette di usare lo stesso nome per oggetti diversi in contesti diversi
  - Esempio: `matematica.algebra.somma` e `matematica.geometria.somma` possono coesistere
  - Evita conflitti tra moduli con nomi identici ma funzionalità diverse

2. **Caratteristiche Principali**
- Deve contenere un file `__init__.py` (anche vuoto)
- Permette import gerarchici
- Organizza codice correlato in modo logico
- Evita conflitti di nomi (namespace)

3. **Analogia**
- Come una cartella nel filesystem:
  - Package = cartella
  - Moduli = file
  - Subpackages = sottocartelle

4. **Esempio Pratico**

```
matematica/                  # Questo è un package
    __init__.py
    algebra.py              # Questi sono moduli
    geometria.py
    statistica/             # Questo è un subpackage
        __init__.py
        base.py
        avanzata.py
```

5. **Utilizzo**
```python
# Diversi modi di importare da un package
import matematica.algebra
from matematica import geometria
from matematica.statistica import base
```