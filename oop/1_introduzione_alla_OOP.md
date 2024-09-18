## Introduzione alla OOP <!-- omit in toc -->

- [Paradigmi di programmazione: imperativo vs orientato agli oggetti](#paradigmi-di-programmazione-imperativo-vs-orientato-agli-oggetti)
- [Oggetti e Classi: il cuore della OOP](#oggetti-e-classi-il-cuore-della-oop)
- [Un esempio pratico: la classe Studente](#un-esempio-pratico-la-classe-studente)
- [Vantaggi dell’OOP](#vantaggi-delloop)
- [Diagrammi UML di base](#diagrammi-uml-di-base)

La programmazione orientata agli oggetti (Object-Oriented Programming, OOP) è un paradigma di programmazione che organizza il codice attorno a **oggetti**, piuttosto che a semplici istruzioni o funzioni. Ogni oggetto rappresenta un'entità del mondo reale o concettuale e possiede delle caratteristiche (dati) e dei comportamenti (funzionalità). Questo approccio è particolarmente utile per gestire sistemi complessi, poiché promuove la modularità e la riusabilità del codice.

### Paradigmi di programmazione: imperativo vs orientato agli oggetti

Prima di esplorare l’OOP, è importante comprendere la differenza tra la **programmazione imperativa** e quella **orientata agli oggetti**. La programmazione imperativa, che probabilmente già conosci, si concentra sull'esecuzione sequenziale di comandi. Un programma imperativo è costituito da una serie di istruzioni che modificano lo stato del programma, aggiornando variabili globali e locali. In questo paradigma, il programmatore indica chiaramente **cosa** fare e **come** farlo.

Nella programmazione orientata agli oggetti, invece, l'enfasi è posta sulla **creazione di oggetti** che interagiscono tra loro per eseguire il programma. Ogni oggetto è una rappresentazione di un’entità che può contenere dati sotto forma di **attributi** (dati o proprietà dell'oggetto) e **metodi** (funzionalità che manipolano i dati). Piuttosto che scrivere una sequenza di istruzioni, l'OOP organizza il codice in entità autonome, ognuna con la propria responsabilità.

> **Esempio**: Se vogliamo modellare un sistema per gestire un insieme di studenti in un istituto, nella programmazione imperativa potremmo usare array o liste per memorizzare i dati degli studenti e una serie di funzioni per gestire queste informazioni. In OOP, invece, creeremmo una **classe** `Studente` con attributi come nome, età e matricola, e metodi come `studia()` o `partecipa_a_lezione()`.

### Oggetti e Classi: il cuore della OOP

Il concetto chiave della OOP è che tutto nel programma è rappresentato da **oggetti**. Un oggetto è una combinazione di dati e metodi che agiscono su quei dati. Per comprendere meglio, è utile introdurre il concetto di **classe**.

- **Classe**: Una classe è un modello, o blueprint, che descrive le proprietà e i comportamenti di un insieme di oggetti. Immagina una classe come una piantina di una casa. Questa piantina non è una casa in sé, ma può essere usata per costruire molte case. Allo stesso modo, una classe definisce le caratteristiche e i metodi di un oggetto, ma è solo un concetto astratto.

- **Oggetto**: Un oggetto è una realizzazione concreta di una classe. Mentre la classe descrive il modello, l'oggetto è un'istanza specifica di quel modello. Ogni oggetto ha uno **stato** (determinato dai valori dei suoi attributi) e un **comportamento** (determinato dai suoi metodi).

### Un esempio pratico: la classe Studente

Immaginiamo di dover creare un programma per gestire gli studenti di una scuola. Potremmo definire una classe `Studente`, che include attributi come il nome, l'età e il numero di matricola, e metodi per eseguire azioni come studiare o partecipare a una lezione.

Ecco come potrebbe essere una classe `Studente` in Python:

```python
class Studente:
    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.matricola = matricola
    
    def studia(self):
        print(f"{self.nome} sta studiando.")


studente1 = Studente("Marco", 16, "12345") # Creazione di un oggetto
print(studente1.nome)  # Output: Marco
studente1.studia()  # Output: Marco sta studiando.
```

Nel codice sopra, la classe `Studente` definisce:
- **Attributi**: `nome`, `eta`, `matricola`, che rappresentano le caratteristiche di ogni studente.
- **Metodo**: `studia()`, che rappresenta una funzionalità associata agli studenti.

Quando creiamo un oggetto `studente1`, usiamo la classe `Studente` come modello per costruire un'entità concreta. L'oggetto `studente1` ha uno stato specifico (il nome è "Marco", l'età è 16, la matricola è "12345") e può eseguire comportamenti definiti (ad esempio, il metodo `studia()`).

### Vantaggi dell’OOP

Perché dovremmo scegliere l'OOP rispetto alla programmazione imperativa? L’OOP offre diversi vantaggi che rendono lo sviluppo del software più efficiente e gestibile, specialmente per sistemi complessi:

- **Riusabilità del codice**: Una classe ben progettata può essere riutilizzata in diversi contesti. Ad esempio, una volta creata una classe `Studente`, possiamo usarla ovunque serva rappresentare uno studente, senza dover riscrivere il codice.
  
- **Modularità**: La divisione del programma in oggetti separati permette di sviluppare, testare e manutenere ogni parte in modo indipendente. Un errore in una classe non influirà necessariamente sul resto del sistema.

- **Manutenibilità**: Poiché ogni oggetto è responsabile del proprio stato e comportamento, il codice è più facile da aggiornare. Modificare una classe non richiede di riscrivere l'intero programma.

- **Incapsulamento**: I dettagli interni di un oggetto possono essere nascosti all’esterno. 

- **Astrazione**: Permette di concentrarsi su cosa fa un oggetto, senza preoccuparsi di come lo fa.

### Diagrammi UML di base

Per facilitare la comprensione e la progettazione dei sistemi OOP, spesso si utilizzano i **diagrammi delle classi UML (Unified Modeling Language)**. Questi diagrammi offrono una rappresentazione visiva delle classi, dei loro attributi e metodi, e delle relazioni tra le classi.

Un diagramma UML di una classe tipica potrebbe essere rappresentato come segue:

```
+------------------------+
|        Studente        |
+------------------------+
| - nome: string         |
| - eta: int             |
| - matricola: string    |
+------------------------+
| + studia(): void       |
+------------------------+
```

In questo esempio:
- La parte superiore contiene il nome della classe (`Studente`).
- La parte centrale elenca gli attributi (ad esempio, `nome`, `eta`, `matricola`).
- La parte inferiore elenca i metodi (in questo caso, `studia()`).

I diagrammi UML sono uno strumento potente per visualizzare il design di un sistema prima di scrivere il codice, aiutando a comprendere meglio la struttura del software.

