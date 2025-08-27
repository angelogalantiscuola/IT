## Costruttori e Incapsulamento <!-- omit in toc -->

- [Costruttori](#costruttori)
- [Incapsulamento](#incapsulamento)
  - [Attributi pubblici e privati](#attributi-pubblici-e-privati)


I **metodi** sono funzioni definite all'interno di una classe che permettono agli oggetti di eseguire azioni. Il primo parametro di un metodo è sempre `self`, che **rappresenta l'istanza corrente dell'oggetto**.
Questo parametro permette al metodo di accedere agli attributi e ad altri metodi della stessa istanza.

### Costruttori

Il metodo speciale `__init__()` è chiamato **costruttore** e viene eseguito automaticamente quando un nuovo oggetto della classe viene creato. Serve per inizializzare gli attributi di istanza con valori specifici.

> **Esempio**: Inizializziamo la classe `Studente` con nome, età e matricola.

```python
class Studente:
    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.matricola = matricola

studente1 = Studente("Marco", 16, "12345")
```

Ogni volta che creiamo un nuovo oggetto `Studente`, il costruttore assegna i valori degli attributi in base ai parametri passati.


### Incapsulamento

L'**incapsulamento** è un principio fondamentale dell'OOP che consente di nascondere i dettagli interni di un oggetto e di controllare l'accesso ai suoi attributi e metodi. Ciò aiuta a mantenere il codice modulare e a ridurre gli errori.

#### Attributi pubblici e privati

Gli attributi possono essere **pubblici** o **privati**:
- Gli attributi pubblici sono accessibili da qualsiasi parte del programma.
- Gli attributi privati sono accessibili solo all'interno della classe e sono prefissati con due underscore (`__`).

Gli attributi privati vengono utilizzati per diverse ragioni:

- **Incapsulamento**: L'incapsulamento è uno dei principi fondamentali della programmazione orientata agli oggetti. Consente di nascondere i dettagli interni di una classe e di esporre solo ciò che è necessario. Questo aiuta a mantenere il codice più pulito e a ridurre la complessità.
- **Protezione dei dati**: Gli attributi privati proteggono i dati sensibili da accessi non autorizzati o modifiche accidentali. Questo è particolarmente importante quando si lavora con informazioni riservate o critiche.
- **Controllo dell'accesso**: Utilizzando attributi privati, è possibile controllare come e quando i dati vengono modificati. Ad esempio, si può fornire un metodo pubblico che esegue controlli o validazioni prima di modificare un attributo privato.

> **Esempio**: Definiamo un attributo privato `__matricola` nella classe `Studente`.

```python
class Studente:
    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.__matricola = matricola  # Attributo privato

    def mostra_matricola(self):
        return self.__matricola  # Metodo pubblico per accedere a un attributo privato

studente1 = Studente("Marco", 16, "12345")
print(studente1.nome) # Attributo pubblico
print(studente1.__matricola) # Questo genererebbe un errore
print(studente1.mostra_matricola())  # Output: 12345
```

In questo caso, l'attributo `__matricola` non è accessibile direttamente dall'esterno della classe, ma possiamo creare un metodo per mostrare il suo valore.

Un diagramma UML per una classe `Studente` con attributi di istanza e metodi potrebbe essere rappresentato come segue:

```
+---------------------------+
|      Studente             |
+---------------------------+
| + nome: string            |
| + eta: int                |
| - __matricola: str        |
+---------------------------+
| + studia(): void          |
| + mostra_matricola(): str |
+---------------------------+
```

In questo diagramma:
- I **segni più (+)** indicano gli attributi e i metodi pubblici.
- I **segni meno (-)** indicano gli attributi privati.
- Gli attributi sono seguiti dal loro tipo (es. `string`, `int`).
