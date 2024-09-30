## Getters e Setters  <!-- omit in toc -->

- [Getter](#getter)
- [Setter](#setter)
- [Uso delle Proprietà in Python](#uso-delle-proprietà-in-python)
- [Vantaggi dell’Uso di Getters e Setters](#vantaggi-delluso-di-getters-e-setters)


I **getters** e **setters** sono metodi che permettono di accedere e modificare gli attributi privati di una classe in modo controllato. L’uso di questi metodi è strettamente legato al concetto di **incapsulamento**, poiché permette di nascondere i dettagli interni dell'implementazione e offrire un’interfaccia più sicura e intuitiva per accedere ai dati.

### Getter

Un **getter** è un metodo che restituisce il valore di un attributo. Di solito viene utilizzato quando un attributo è dichiarato privato (con un nome che inizia con un `_` o `__`) per evitare un accesso diretto.

Esempio:

```python
class Studente:
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

    def get_eta(self):
        return self._eta
```

In questo esempio, l'attributo `_eta` è privato, quindi non può essere accessibile direttamente. Tuttavia, possiamo accedervi tramite il metodo `get_eta()`.

### Setter

Un **setter** è un metodo che permette di modificare il valore di un attributo privato. Come per i getter, è utile per controllare e limitare le modifiche che possono essere fatte agli attributi.

Esempio:

```python
class Studente:
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

    def set_eta(self, nuova_eta):
        if nuova_eta > 0:  # Controllo semplice sull’età
            self._eta = nuova_eta
        else:
            raise ValueError("L'età deve essere positiva")
```

### Uso delle Proprietà in Python

In Python, possiamo utilizzare il decoratore `@property` per definire getter e setter in modo più elegante e intuitivo.

Esempio con `@property`:

```python
class Studente:
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, nuova_eta):
        if nuova_eta > 0:
            self._eta = nuova_eta
        else:
            raise ValueError("L'età deve essere positiva")
```

In questo caso, possiamo accedere e modificare l’attributo `eta` come se fosse pubblico:

```python
studente = Studente('Alice', 20)
print(studente.eta)  # Chiama automaticamente il getter
studente.eta = 21    # Chiama automaticamente il setter
```

### Vantaggi dell’Uso di Getters e Setters

- **Incapsulamento**: Mantengono gli attributi privati, ma permettono di accedervi tramite metodi pubblici.
- **Controllo sui dati**: Consentono di aggiungere logica per validare o trasformare i dati quando vengono letti o modificati.
- **Modularità**: Se il modo in cui i dati vengono memorizzati cambia, puoi semplicemente aggiornare i metodi senza influenzare il codice che usa quegli attributi.
