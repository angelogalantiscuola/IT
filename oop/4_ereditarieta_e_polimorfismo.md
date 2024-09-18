## Ereditarietà e Polimorfismo

L'ereditarietà e il polimorfismo sono concetti fondamentali nella programmazione orientata agli oggetti (OOP). Questi meccanismi permettono di riutilizzare il codice in modo più efficiente e flessibile, riducendo la duplicazione e migliorando la manutenzione.

### Ereditarietà: Specializzazione delle Classi

L'ereditarietà consente a una classe (classe derivata o sottoclasse) di ereditare attributi e metodi da un'altra classe (classe base o superclasse). Questo permette di creare nuove classi basate su quelle esistenti, estendendo o modificando il loro comportamento.

Ad esempio, immagina di avere una classe base chiamata `Veicolo`, che rappresenta un generico mezzo di trasporto:

```python
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def descrizione(self):
        return f'{self.marca} {self.modello}'
```

Ora, possiamo creare una classe derivata, come `Auto`, che eredita da `Veicolo`, ma aggiunge caratteristiche specifiche delle automobili:

```python
class Auto(Veicolo):
    def __init__(self, marca, modello, porte):
        super().__init__(marca, modello)
        self.porte = porte
    
    def descrizione_auto(self):
        return f'Auto:{self.marca} {self.modello}, {self.porte} porte'
```

In questo esempio, la classe `Auto` eredita il costruttore e il metodo `descrizione` dalla classe `Veicolo`. Usando la funzione `super()`, possiamo richiamare il costruttore della superclasse e aggiungere nuovi attributi o metodi nella sottoclasse.

Vantaggi dell'Ereditarietà:
- **Riutilizzo del codice**: Evita di riscrivere codice già presente in altre classi.
- **Gerarchia logica**: Permette di organizzare le classi in una gerarchia di specializzazione, con le classi più generiche che stanno alla base e quelle più specifiche in cima.

### Polimorfismo: Diversi Comportamenti per Classi Derivate

Il polimorfismo è la capacità di usare lo stesso metodo in contesti diversi, a seconda dell'oggetto su cui viene chiamato. In altre parole, classi diverse possono implementare lo stesso metodo, ma con comportamenti diversi.

Ad esempio, potremmo avere una classe `Moto` che eredita da `Veicolo`, ma implementa un proprio metodo `descrizione`.

```python
class Moto(Veicolo):
    def descrizione(self):
        return f'Moto: {self.marca} {self.modello}'
```

Ora possiamo avere oggetti di classi diverse (`Auto` e `Moto`) e invocare lo stesso metodo (`descrizione`) su di essi, ottenendo risultati differenti:

```python
veicolo1 = Auto('Toyota', 'Yaris', 5)
veicolo2 = Moto('Yamaha', 'R1')

print(veicolo1.descrizione())  # Output: Toyota Yaris
print(veicolo2.descrizione())  # Output: Moto: Yamaha R1
```

Il polimorfismo permette di trattare oggetti di classi diverse in modo uniforme, migliorando la flessibilità del codice.

### Ereditarietà Multipla in Python

In Python, una classe può ereditare da più classi contemporaneamente, un concetto chiamato "ereditarietà multipla". Ad esempio:

```python
class Elettrico:
    def __init__(self, batteria):
        self.batteria = batteria
    
    def descrizione_batteria(self):
        return f'Batteria: {self.batteria} kWh'

class AutoElettrica(Veicolo, Elettrico):
    def __init__(self, marca, modello, batteria):
        Veicolo.__init__(self, marca, modello)
        Elettrico.__init__(self, batteria)
    
    def descrizione(self):
        return f'{self.marca} {self.modello} con {self.batteria} kWh'
```

L'ereditarietà multipla è potente, ma va usata con attenzione per evitare problemi di complessità e ambiguità (ad esempio, quando più superclassi contengono metodi con lo stesso nome).

### Diagrammi UML: Ereditarietà e Polimorfismo

Nel diagramma UML, l'ereditarietà viene rappresentata con una freccia vuota che punta dalla sottoclasse alla superclasse. Un esempio di diagramma UML per il nostro sistema di `Veicolo`, `Auto`, e `Moto` potrebbe apparire così:

```
            -----------------
            |     Veicolo    |
            -----------------
               ^          ^
               |          |
       ----------------- -----------------
       |     Auto       | |     Moto       |
       ----------------- -----------------
```

In questo diagramma, `Auto` e `Moto` ereditano da `Veicolo`, condividendo parte del comportamento ma potendo sovrascrivere o estendere i metodi della superclasse.
