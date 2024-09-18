## Attributi e Metodi in Python <!-- omit in toc -->

- [Attributi: i dati degli oggetti](#attributi-i-dati-degli-oggetti)
  - [Attributi di istanza](#attributi-di-istanza)
  - [Attributi di classe](#attributi-di-classe)
- [Metodi: le azioni degli oggetti](#metodi-le-azioni-degli-oggetti)
  - [Metodi di istanza](#metodi-di-istanza)
  - [Metodi di classe](#metodi-di-classe)
  - [Metodi statici](#metodi-statici)


Gli **attributi** e i **metodi** sono gli elementi fondamentali che definiscono il comportamento di una classe e degli oggetti creati da essa. Gli attributi rappresentano i dati associati a un oggetto, mentre i metodi definiscono le azioni che un oggetto può compiere. In questa lezione esploreremo in dettaglio questi concetti e come vengono utilizzati in Python.

### Attributi: i dati degli oggetti

Un **attributo** è una variabile associata a un oggetto o a una classe. Esistono due tipi principali di attributi:
- **Attributi di istanza**: Questi sono specifici di un oggetto particolare e rappresentano lo stato individuale dell'oggetto.
- **Attributi di classe**: Questi sono condivisi tra tutte le istanze della classe.

#### Attributi di istanza

Gli attributi di istanza vengono definiti all'interno del metodo speciale `__init__()`, il costruttore della classe. Ogni volta che si crea un nuovo oggetto, Python chiama automaticamente questo metodo, permettendo di inizializzare gli attributi con valori specifici.

```python
class Studente:
    def __init__(self, nome, eta, matricola):
        self.nome = nome  # Attributo di istanza
        self.eta = eta  # Attributo di istanza
        self.matricola = matricola  # Attributo di istanza
```

In questo esempio, la classe `Studente` ha tre attributi di istanza: `nome`, `eta`, e `matricola`. Ogni volta che creiamo un oggetto della classe `Studente`, possiamo specificare valori diversi per questi attributi.

> **Esempio**: Creiamo un oggetto `studente1` e un oggetto `studente2` della classe `Studente`, ognuno con valori diversi per i propri attributi.

```python
studente1 = Studente("Marco", 16, "12345")
studente2 = Studente("Laura", 17, "67890")

print(studente1.nome)  # Output: Marco
print(studente2.nome)  # Output: Laura
```

Ogni oggetto `studente1` e `studente2` ha i propri valori distinti per gli attributi `nome`, `eta`, e `matricola`. Questi valori sono mantenuti separati per ogni istanza della classe.

#### Attributi di classe

Gli attributi di classe, al contrario degli attributi di istanza, sono condivisi tra tutte le istanze della classe. Vengono definiti direttamente nella classe, al di fuori di qualsiasi metodo, e sono accessibili da ogni oggetto della classe.

```python
class Studente:
    scuola = "Liceo Classico"  # Attributo di classe

    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.matricola = matricola
```

In questo caso, l’attributo `scuola` è condiviso tra tutti gli oggetti `Studente`. Può essere accessibile sia attraverso un'istanza che direttamente dalla classe.

> **Esempio**: Verifica dell’attributo di classe.

```python
print(Studente.scuola)  # Output: Liceo Classico

studente1 = Studente("Marco", 16, "12345")
print(studente1.scuola)  # Output: Liceo Classico
```

Indipendentemente dal numero di istanze della classe `Studente` che creiamo, l’attributo `scuola` rimane invariato.

### Metodi: le azioni degli oggetti

I **metodi** sono funzioni definite all'interno di una classe e rappresentano le azioni che un oggetto può eseguire. Il primo parametro di ogni metodo, per convenzione chiamato `self`, si riferisce all'istanza dell'oggetto che invoca il metodo.

#### Metodi di istanza

I metodi di istanza operano su attributi di istanza e possono accedere sia a questi attributi che ad altri metodi della classe. Possono essere definiti all'interno della classe come normali funzioni, ma il loro primo argomento sarà sempre `self`, che fa riferimento all'oggetto che sta chiamando il metodo.

```python
class Studente:
    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.matricola = matricola

    def studia(self):
        print(f"{self.nome} sta studiando.")
```

> **Esempio**: Utilizzo del metodo `studia()` per far compiere un'azione all'oggetto.

```python
studente1 = Studente("Marco", 16, "12345")
studente1.studia()  # Output: Marco sta studiando.
```

Il metodo `studia()` accede all'attributo `nome` dell'oggetto `studente1` per personalizzare il messaggio di output. Ogni oggetto può invocare questo metodo e ottenere un risultato coerente con i propri dati.

#### Metodi di classe

I metodi di classe operano sugli attributi di classe. Per definire un metodo di classe, si utilizza il decoratore `@classmethod`, e il primo argomento del metodo sarà `cls`, che si riferisce alla classe stessa.

```python
class Studente:
    scuola = "Liceo Classico"  # Attributo di classe

    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.matricola = matricola

    @classmethod
    def cambia_scuola(cls, nuova_scuola):
        cls.scuola = nuova_scuola
```

> **Esempio**: Cambiare l’attributo di classe `scuola` utilizzando un metodo di classe.

```python
Studente.cambia_scuola("Liceo Scientifico")
print(Studente.scuola)  # Output: Liceo Scientifico
```

In questo esempio, il metodo `cambia_scuola()` modifica l’attributo di classe `scuola` per tutte le istanze.

#### Metodi statici

I metodi statici, definiti con il decoratore `@staticmethod`, non accedono né agli attributi di istanza né a quelli di classe. Sono funzioni che appartengono logicamente alla classe, ma non dipendono né dagli oggetti né dalla classe stessa.

```python
class Studente:
    @staticmethod
    def matricola_valida(matricola):
        return matricola.isdigit()
```

> **Esempio**: Verifica se la matricola è valida prima di creare uno studente.

```python
print(Studente.matricola_valida("123456"))  # Output: True
print(Studente.matricola_valida("123ABC"))  # Output: False
```

I metodi statici possono essere utilizzati quando una funzione ha una relazione logica con la classe, ma non necessita di accedere ai dati dell’istanza o della classe.
