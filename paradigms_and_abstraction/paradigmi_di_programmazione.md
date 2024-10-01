## Paradigmi di programmazione <!-- omit in toc -->

- [Introduzione ai paradigmi di programmazione](#introduzione-ai-paradigmi-di-programmazione)
- [Programmazione imperativa](#programmazione-imperativa)
  - [Programmazione procedurale](#programmazione-procedurale)
  - [Programmazione strutturata](#programmazione-strutturata)
  - [Differenze chiave tra programmazione procedurale e strutturata](#differenze-chiave-tra-programmazione-procedurale-e-strutturata)
- [Programmazione dichiarativa](#programmazione-dichiarativa)
  - [Programmazione funzionale](#programmazione-funzionale)
  - [Programmazione logica](#programmazione-logica)
- [Programmazione orientata agli oggetti (OOP)](#programmazione-orientata-agli-oggetti-oop)
- [Altri paradigmi](#altri-paradigmi)
  - [Programmazione event-driven](#programmazione-event-driven)
  - [Programmazione concorrente](#programmazione-concorrente)
- [Confronto tra paradigmi](#confronto-tra-paradigmi)
- [Scelta del paradigma appropriato](#scelta-del-paradigma-appropriato)

I paradigmi di programmazione rappresentano approcci fondamentalmente diversi alla strutturazione e all'organizzazione del codice. Ogni paradigma offre un modo unico di pensare alla risoluzione dei problemi e alla progettazione del software.

### Introduzione ai paradigmi di programmazione

Un paradigma di programmazione è un modello concettuale per strutturare e organizzare il codice di un programma. Esso fornisce linee guida su come affrontare problemi e progettare soluzioni.

> **Definizione**: Un paradigma di programmazione è un approccio fondamentale alla programmazione di computer, un modo di concettualizzare ciò che significa eseguire computazioni e come strutturare e organizzare le attività di programmazione.

I principali paradigmi di programmazione includono:
- Programmazione imperativa
- Programmazione dichiarativa
- Programmazione orientata agli oggetti



### Programmazione imperativa

La programmazione imperativa è uno dei paradigmi più antichi e fondamentali nella storia dell'informatica. Questo approccio si basa sul concetto di "comando" o "istruzione", dove il programmatore specifica esplicitamente una sequenza di comandi che il computer deve eseguire per raggiungere un determinato risultato.

Caratteristiche principali della programmazione imperativa:
1. **Sequenzialità**: Le istruzioni vengono eseguite una dopo l'altra, in un ordine specifico.
2. **Mutabilità dello stato**: Utilizza variabili che possono cambiare valore durante l'esecuzione del programma.
3. **Assegnazione**: Usa l'operazione di assegnazione per modificare lo stato del programma.
4. **Iterazione**: Impiega strutture di controllo come cicli per ripetere blocchi di codice.
5. **Controllo di flusso condizionale**: Utilizza istruzioni condizionali per prendere decisioni durante l'esecuzione.

La programmazione imperativa si è evoluta nel tempo, dando origine a due importanti sotto-paradigmi: la programmazione procedurale e la programmazione strutturata.

#### Programmazione procedurale

La programmazione procedurale è un'evoluzione della programmazione imperativa che introduce il concetto di procedure o funzioni.

Caratteristiche chiave:
- **Decomposizione funzionale**: Il programma è suddiviso in procedure più piccole e gestibili.
- **Riutilizzo del codice**: Le procedure possono essere chiamate più volte da diverse parti del programma.
- **Passaggio di parametri**: Le procedure possono accettare input e restituire output.
- **Scope delle variabili**: Introduce il concetto di variabili locali e globali.

Esempio in C:

```c
#include <stdio.h>

// Dichiarazione di una procedura
void stampaSaluto(char* nome) {
    printf("Ciao, %s!\n", nome);
}

// Funzione che calcola il quadrato di un numero
int quadrato(int n) {
    return n * n;
}

int main() {
    char nome[20] = "Alice";
    stampaSaluto(nome);
    
    int numero = 5;
    int risultato = quadrato(numero);
    printf("Il quadrato di %d è %d\n", numero, risultato);
    
    return 0;
}
```

#### Programmazione strutturata

La programmazione strutturata è un'ulteriore evoluzione che impone restrizioni sull'uso di alcune istruzioni di controllo di flusso, in particolare l'istruzione `goto`, per migliorare la chiarezza e la manutenibilità del codice.

> L'istruzione `goto` permette di saltare direttamente a un'altra parte del codice. Questo può rendere il codice difficile da seguire e mantenere, poiché i salti non sono sempre lineari e possono creare un "codice spaghetti", dove il flusso logico è complicato e intrecciato.

Caratteristiche chiave:
- **Strutture di controllo limitate**: Utilizza solo tre tipi di strutture di controllo: sequenza, selezione (if-then-else) e iterazione (cicli).
- **Singolo punto di ingresso e uscita**: Ogni blocco di codice ha un unico punto di ingresso e di uscita.
- **Subroutine**: Utilizza subroutine (procedure e funzioni) per organizzare il codice.
- **Scope di blocco**: Introduce il concetto di scope limitato ai blocchi di codice.

Esempio in Python:

```python
def calcola_media(numeri):
    if not numeri:  # Controllo se la lista è vuota
        return None
    
    somma = 0
    conteggio = 0
    
    for numero in numeri:
        if numero < 0:
            continue  # Salta i numeri negativi
        somma += numero
        conteggio += 1
    
    if conteggio == 0:
        return None
    
    return somma / conteggio

# Uso della funzione
numeri = [1, -2, 3, 4, -5, 6]
media = calcola_media(numeri)

if media is not None:
    print(f"La media dei numeri positivi è: {media:.2f}")
else:
    print("Non ci sono numeri positivi nella lista")
```

#### Differenze chiave tra programmazione procedurale e strutturata

1. **Controllo di flusso**:
   - Procedurale: Può utilizzare `goto` e altre istruzioni di salto non strutturate.
   - Strutturata: Evita l'uso di `goto`, favorendo strutture di controllo ben definite.

2. **Organizzazione del codice**:
   - Procedurale: Organizza il codice in procedure, ma non necessariamente in modo gerarchico.
   - Strutturata: Enfatizza una struttura gerarchica e modulare del codice.

3. **Leggibilità e manutenibilità**:
   - Procedurale: Può diventare difficile da seguire in programmi complessi.
   - Strutturata: Promuove codice più leggibile e facile da mantenere.

4. **Approccio alla soluzione dei problemi**:
   - Procedurale: Si concentra sulla sequenza di passi per risolvere un problema.
   - Strutturata: Enfatizza la decomposizione del problema in sottoproblemi più gestibili.

5. **Debugging e testing**:
   - Procedurale: Può essere più difficile da debuggare a causa di flussi di controllo potenzialmente complicati.
   - Strutturata: Facilita il debugging e il testing grazie a una struttura più prevedibile.

> **Nota storica**: La programmazione strutturata emerse negli anni '60 come risposta ai problemi di leggibilità e manutenibilità del codice riscontrati nei grandi sistemi sviluppati con approcci puramente procedurali. Il famoso articolo di Edsger Dijkstra "Go To Statement Considered Harmful" (1968) fu un catalizzatore importante per questo cambiamento di paradigma.

Entrambi questi approcci fanno parte del paradigma imperativo più ampio, ma la programmazione strutturata rappresenta un'evoluzione significativa verso codice più organizzato, leggibile e manutenibile. Molti linguaggi moderni incorporano principi di programmazione strutturata come base, anche quando supportano altri paradigmi come la programmazione orientata agli oggetti o funzionale.



### Programmazione dichiarativa

La programmazione dichiarativa si concentra sul "cosa" deve essere calcolato piuttosto che sul "come" calcolarlo. Il programmatore specifica il risultato desiderato, lasciando al sistema il compito di determinare i dettagli dell'esecuzione.

#### Programmazione funzionale

La programmazione funzionale tratta il calcolo come la valutazione di funzioni matematiche, evitando il cambiamento di stato e i dati mutabili.

Caratteristiche:
- Funzioni pure (senza effetti collaterali)
- Immutabilità dei dati
- Ricorsione invece di iterazione
- Funzioni di ordine superiore

Esempio in Haskell:

```haskell
-- Definizione di una funzione per calcolare il fattoriale
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Uso della funzione
main = do
    putStrLn "Il fattoriale di 5 è:"
    print (factorial 5)
```

#### Programmazione logica

La programmazione logica si basa sulla logica formale. I programmi consistono in un insieme di fatti e regole, e l'esecuzione è un processo di inferenza logica.

Caratteristiche:
- Basata su fatti e regole
- Utilizzo di unificazione e backtracking
- Separazione tra logica e controllo

Esempio in Prolog:

```prolog
% Fatti
genitore(anna, mario).
genitore(luigi, mario).
genitore(mario, giovanni).

% Regola
nonno(X, Z) :- genitore(X, Y), genitore(Y, Z).

% Query
?- nonno(anna, giovanni).
% Output: true
```

### Programmazione orientata agli oggetti (OOP)

La programmazione orientata agli oggetti organizza il codice in oggetti che contengono dati e codice. È basata sul concetto di "oggetti" che possono contenere dati sotto forma di campi (attributi) e codice sotto forma di procedure (metodi).

Caratteristiche:
- Incapsulamento
- Ereditarietà
- Polimorfismo
- Astrazione

Esempio in Java:

```java
public class Persona {
    private String nome;
    private int età;

    public Persona(String nome, int età) {
        this.nome = nome;
        this.età = età;
    }

    public void saluta() {
        System.out.println("Ciao, sono " + nome + " e ho " + età + " anni.");
    }
}

public class Main {
    public static void main(String[] args) {
        Persona p = new Persona("Alice", 30);
        p.saluta();
    }
}
```

### Altri paradigmi

#### Programmazione event-driven

La programmazione event-driven si basa sulla gestione di eventi o segnali generati dal sistema o dall'utente.

Caratteristiche:
- Gestione di eventi
- Callback e listeners
- Ampiamente utilizzata nelle interfacce utente

Esempio in JavaScript:

```javascript
document.getElementById("myButton").addEventListener("click", function() {
    alert("Il pulsante è stato cliccato!");
});
```

#### Programmazione concorrente

La programmazione concorrente si occupa dell'esecuzione simultanea di più task o processi.

Caratteristiche:
- Multithreading
- Sincronizzazione
- Gestione delle risorse condivise

Esempio in Go:

```go
package main

import (
    "fmt"
    "time"
)

func conteggioAsincrono(nome string) {
    for i := 1; i <= 5; i++ {
        fmt.Println(nome, ":", i)
        time.Sleep(time.Millisecond * 500)
    }
}

func main() {
    go conteggioAsincrono("Goroutine 1")
    go conteggioAsincrono("Goroutine 2")
    time.Sleep(time.Second * 3)
}
```

### Confronto tra paradigmi

| Paradigma  | Vantaggi                          | Svantaggi                                  |
| ---------- | --------------------------------- | ------------------------------------------ |
| Imperativo | Efficiente, vicino alla macchina  | Può diventare complesso in progetti grandi |
| Funzionale | Prevedibile, facile da testare    | Curva di apprendimento ripida              |
| OOP        | Modularità, riusabilità           | Overhead di progettazione                  |
| Logico     | Potente per problemi di inferenza | Limitato in applicazioni generali          |

### Scelta del paradigma appropriato

La scelta del paradigma dipende da vari fattori:
1. Natura del problema da risolvere
2. Requisiti di prestazioni e scalabilità
3. Esperienza del team di sviluppo
4. Strumenti e framework disponibili
5. Manutenibilità e estensibilità del codice

> **Nota**: Molti linguaggi moderni supportano più paradigmi, permettendo ai programmatori di scegliere l'approccio più adatto per ogni parte specifica del loro progetto.

La comprensione dei diversi paradigmi di programmazione è essenziale per gli sviluppatori, in quanto fornisce una varietà di strumenti concettuali per affrontare problemi complessi e progettare soluzioni eleganti ed efficienti.