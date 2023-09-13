
La programmazione orientata agli oggetti (OOP) è un paradigma di programmazione che permette di definire oggetti software in grado di interagire gli uni con gli altri attraverso lo scambio di messaggi. 
Gli oggetti sono istanze di classi, che sono astrazioni che rappresentano le proprietà comuni e il comportamento di un insieme di oggetti concreti. 
I concetti principali della programmazione orientata agli oggetti sono:
-   **Incapsulamento**: significa nascondere i dettagli dell’implementazione di un oggetto e fornire solo un’interfaccia ben definita per interagire con esso. Questo garantisce il controllo sull’accesso ai dati e alle funzionalità dell’oggetto e favorisce la modularità e il riuso del codice.
-   **Astrazione**: significa usare classi semplificate, invece di codice complesso, per accedere agli oggetti. Questo permette di focalizzarsi sulle caratteristiche essenziali degli oggetti e di ignorare i dettagli irrilevanti o secondari. L’astrazione facilita la comprensione e la manutenzione del codice.
-   **Ereditarietà**: significa che una nuova classe può ereditare automaticamente le proprietà e le funzionalità di una classe esistente (chiamata classe padre o superclasse). Questo permette di creare gerarchie di classi e di riutilizzare il codice esistente senza doverlo riscrivere o modificarlo. L’ereditarietà favorisce il polimorfismo e il raffinamento del codice.
-   **Polimorfismo**: significa che un oggetto può assumere forme diverse a seconda del contesto in cui viene usato. Questo permette di usare lo stesso nome o lo stesso messaggio per invocare funzionalità diverse su oggetti diversi, purché questi siano compatibili tra loro (cioè siano sottotipi della stessa superclasse o implementino la stessa interfaccia). Il polimorfismo aumenta la flessibilità e l’espressività del codice.

## Incapsulamento
L'incapsulamento è il processo di **nascondere i dettagli di implementazione di un oggetto e fornire solo un'interfaccia ben definita per interagire con esso.** 

> Un esempio di incapsulamento potrebbe essere quello di una classe che rappresenta una lampadina. La classe potrebbe avere degli attributi come la potenza, il colore, lo stato (acceso o spento) e dei metodi come accendi, spegni, cambia colore. L'utente della classe non ha bisogno di sapere come funziona internamente la lampadina, ma solo come usare i metodi esposti dall'interfaccia. Questo garantisce il controllo sull'accesso ai dati e alle funzionalità della lampadina e favorisce la modularità e il riuso del codice.


### Esempio di incapsulamento in Javascript

```javascript
// Definiamo una funzione costruttrice che rappresenta una lampadina
function Lampadina(potenza, colore) {
  // Queste sono le variabili private che non sono accessibili dall'esterno
  var potenza = potenza;
  var colore = colore;
  var stato = false; // acceso o spento

  // Questi sono i metodi pubblici che espongono l'interfaccia della lampadina
  this.accendi = function() {
    stato = true;
    console.log("La lampadina è accesa");
  };

  this.spegni = function() {
    stato = false;
    console.log("La lampadina è spenta");
  };

  this.cambiaColore = function(nuovoColore) {
    colore = nuovoColore;
    console.log("La lampadina ha cambiato colore in " + colore);
  };

  this.getPotenza = function() {
    return potenza;
  };

  this.getColore = function() {
    return colore;
  };

  this.getStato = function() {
    return stato;
  };
}

// Creiamo un'istanza della lampadina
var lampadina = new Lampadina(60, "bianco");

// Usiamo i metodi pubblici per interagire con la lampadina
lampadina.accendi(); // La lampadina è accesa
lampadina.cambiaColore("rosso"); // La lampadina ha cambiato colore in rosso
lampadina.spegni(); // La lampadina è spenta

// Non possiamo accedere direttamente alle variabili private
console.log(lampadina.potenza); // undefined
console.log(lampadina.colore); // undefined
console.log(lampadina.stato); // undefined

// Possiamo usare i metodi getter per ottenere i valori delle variabili private
console.log(lampadina.getPotenza()); // 60
console.log(lampadina.getColore()); // rosso
console.log(lampadina.getStato()); // false
```

## Astrazione
L’astrazione è un processo concettuale che permette di **definire regole e concetti generali a partire da esempi specifici, sensibili o concreti.** L’astrazione ci consente di focalizzarci sulle caratteristiche essenziali di un oggetto o di un fenomeno e di ignorare i dettagli irrilevanti o secondari. L’astrazione facilita la comprensione e la manutenzione del codice.

> Una classe è un’astrazione che descrive le proprietà e il comportamento comuni di un insieme di oggetti concreti. Per esempio, una classe Persona potrebbe avere degli attributi come nome, età, sesso e dei metodi come cammina, parla, mangia. Questa classe astrae le caratteristiche comuni di tutte le persone reali e ci permette di usare la stessa interfaccia per interagire con diversi oggetti Persona.



## Ereditarieta
L’ereditarietà è un meccanismo che permette di creare nuove classi a partire da classi esistenti, riutilizzando e modificando le loro proprietà e funzionalità. Una classe che eredita da un’altra classe viene chiamata sottoclasse o classe figlia, mentre la classe da cui eredita viene chiamata superclasse o classe padre. L’ereditarietà favorisce il riuso e il raffinamento del codice.

### Esempio di ereditarieta in Javascript

Per creare una sottoclasse di una classe esistente, si usa la parola chiave extends. Per richiamare il costruttore o i metodi della classe padre, si usa la parola chiave super.

```javascript
// Definiamo una classe che rappresenta un animale
class Animale {
  constructor(nome) { // Questo è il costruttore della classe
    this.nome = nome; // Questa è una proprietà dell'oggetto
  }

  // Questo è un metodo della classe
  mostra() {
    console.log("Questo è " + this.nome);
  }
}

// Definiamo una classe che rappresenta un cane e che eredita dalla classe Animale
class Cane extends Animale {
  constructor(nome, razza) { // Questo è il costruttore della classe
    super(nome); // Richiamiamo il costruttore della classe padre
    this.razza = razza; // Questa è una proprietà dell'oggetto
  }

  // Questo è un metodo della classe
  abbaia() {
    console.log(this.nome + " abbaia");
  }
}

// Creiamo un'istanza della classe Animale
let animale = new Animale("Fido");
animale.mostra(); // Questo è Fido

// Creiamo un'istanza della classe Cane
let cane = new Cane("Fido", "Labrador");
cane.mostra(); // Questo è Fido
cane.abbaia(); // Fido abbaia
```

## Polimorfismo
Il polimorfismo è la **capacità di un oggetto di assumere forme diverse a seconda del contesto in cui viene usato.** Questo permette di usare lo stesso nome o lo stesso messaggio per invocare funzionalità diverse su oggetti diversi, purché questi siano compatibili tra loro (cioè siano sottotipi della stessa superclasse o implementino la stessa interfaccia). Il polimorfismo aumenta la flessibilità e l’espressività del codice.

### Esempio di polimorfismo in Javascript

```javascript
// Definiamo una classe che rappresenta un animale
class Animale {
  constructor(nome) { // Questo è il costruttore della classe
    this.nome = nome; // Questa è una proprietà dell'oggetto
  }

  // Questo è un metodo della classe
  mostra() {
    console.log("Questo è " + this.nome);
  }
}

// Definiamo una classe che rappresenta un cane e che eredita dalla classe Animale
class Cane extends Animale {
  constructor(nome, razza) { // Questo è il costruttore della classe
    super(nome); // Richiamiamo il costruttore della classe padre
    this.razza = razza; // Questa è una proprietà dell'oggetto
  }

  // Questo è un metodo della classe che sovrascrive il metodo della classe padre
  mostra() {
    console.log("Questo è " + this.nome + ", un cane di razza " + this.razza);
  }
}

// Definiamo una funzione che accetta un oggetto di tipo Animale o una sua sottoclasse e invoca il metodo mostra
function stampaInfo(animale) {
  animale.mostra(); // Questo metodo sarà diverso a seconda del tipo di oggetto passato come parametro
}

// Creiamo due istanze delle classi Animale e Cane
let animale = new Animale("Fido");
let cane = new Cane("Fido", "Labrador");

// Usiamo la funzione stampaInfo su entrambi gli oggetti
stampaInfo(animale); // Questo è Fido
stampaInfo(cane); // Questo è Fido, un cane di razza Labrador
```

### Vantaggi del polimorfismo

Il polimorfismo offre diversi vantaggi per la programmazione orientata agli oggetti, tra cui :
-   **Riduzione del codice duplicato**: il polimorfismo permette di scrivere codice più generico e riutilizzabile, evitando di dover scrivere codice specifico per ogni tipo di oggetto. Per esempio, nel nostro esempio precedente, abbiamo scritto una sola funzione stampaInfo che funziona con qualsiasi tipo di animale, invece di scrivere una funzione diversa per ogni sottotipo di animale.
-   **Maggiore astrazione**: il polimorfismo permette di astrarre i dettagli di implementazione dei diversi oggetti e di focalizzarsi solo sull’interfaccia comune che essi espongono. Per esempio, nel nostro esempio precedente, non ci interessa sapere come ogni tipo di animale implementa il metodo mostra, ma solo che esso esiste e che possiamo invocarlo.
-   **Maggiore flessibilità**: il polimorfismo permette di aggiungere nuovi tipi di oggetti senza dover modificare il codice esistente che li usa. Per esempio, nel nostro esempio precedente, potremmo aggiungere una nuova classe che rappresenta un gatto e che eredita dalla classe animale, e la funzione stampaInfo funzionerebbe ancora senza bisogno di cambiamenti.
-   **Maggiore espressività**: il polimorfismo permette di scrivere codice più chiaro e leggibile, usando nomi e messaggi significativi per i diversi oggetti. Per esempio, nel nostro esempio precedente, il metodo mostra ci dice subito cosa fa l’oggetto, invece di usare un nome generico come stampa o toString.
