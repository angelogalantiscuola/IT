# Lezione 3: Rendere le Classi Espressive con i Metodi Speciali

Un oggetto in Python può fare molto di più che chiamare i propri metodi. Può essere "stampato", "confrontato" con altri oggetti, e persino "sommato". Per fare questo, dobbiamo implementare i **metodi speciali** (o "magici", o "dunder" da *double underscore*).

Questi metodi iniziano e finiscono sempre con un doppio underscore.

## 1. `__str__`: La Rappresentazione per l'Utente

Cosa succede se proviamo a stampare il nostro oggetto `Personaggio`?

```python
eroe = Personaggio("Gimli", 8)
print(eroe)
# Output: <__main__.Personaggio object at 0x...>
```

L'output di default non è molto utile. Per fornire una rappresentazione testuale chiara e leggibile, implementiamo il metodo `__str__`.

```python
class Personaggio:
    def __init__(self, nome: str, livello: int):
        self.nome = nome
        self.__punti_vita = 100
        self.__livello = livello

    def __str__(self) -> str:
        # Questo metodo deve restituire (return) una stringa
        return f"Personaggio: {self.nome} | Livello: {self.__livello} | PV: {self.__punti_vita}"

# --- Esempio di utilizzo ---
eroe = Personaggio("Gimli", 8)
print(eroe)
# Output: Personaggio: Gimli | Livello: 8 | PV: 100
```
Il metodo `__str__` viene chiamato automaticamente ogni volta che un oggetto viene convertito in stringa, ad esempio con `print()` o `str()`.

## 2. `__repr__`: La Rappresentazione per lo Sviluppatore

Esiste un altro metodo simile, `__repr__`, che ha uno scopo diverso. La sua rappresentazione dovrebbe essere **inequivocabile** e, idealmente, dovrebbe essere un codice Python valido che può ricreare l'oggetto.

```python
class Personaggio:
    # ... (init e str come prima) ...

    def __repr__(self) -> str:
        return f"Personaggio(nome='{self.nome}', livello={self.__livello})"

# --- Esempio di utilizzo ---
eroe = Personaggio("Legolas", 10)
print(repr(eroe)) # Chiamata esplicita
# Output: Personaggio(nome='Legolas', livello=10)
```

**Regola pratica:** Se implementate solo uno dei due, implementate `__repr__`. Se `__str__` non è definito, Python userà `__repr__` al suo posto.

## 3. Altri Metodi Speciali Utili

Esistono decine di metodi speciali. Eccone alcuni comuni:

*   `__eq__(self, other)`: Definisce il comportamento dell'operatore di uguaglianza (`==`). Permette di decidere quando due oggetti sono da considerarsi "uguali".
    ```python
    def __eq__(self, other):
        # Due personaggi sono uguali se hanno lo stesso nome
        if isinstance(other, Personaggio):
            return self.nome == other.nome
        return False
    ```

*   **Metodi per operazioni aritmetiche:** `__add__` (+), `__sub__` (-), `__mul__` (*), etc.
*   **Metodi per il confronto:** `__lt__` (<), `__gt__` (>), `__le__` (<=), `__ge__` (>=).

Padroneggiare i metodi speciali permette di creare oggetti che si integrano perfettamente con il linguaggio Python, rendendo il codice più intuitivo e leggibile.