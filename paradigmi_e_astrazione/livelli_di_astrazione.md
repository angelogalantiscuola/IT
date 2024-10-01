## Livelli di astrazione dei linguaggi di programmazione <!-- omit in toc -->

- [Introduzione ai livelli di astrazione](#introduzione-ai-livelli-di-astrazione)
- [Linguaggi di basso livello](#linguaggi-di-basso-livello)
- [Linguaggi di alto livello](#linguaggi-di-alto-livello)
  - [Linguaggi di terza generazione (3GL)](#linguaggi-di-terza-generazione-3gl)
  - [Linguaggi di quarta generazione (4GL)](#linguaggi-di-quarta-generazione-4gl)
  - [Linguaggi di quinta generazione (5GL)](#linguaggi-di-quinta-generazione-5gl)
- [Confronto tra linguaggi di basso e alto livello](#confronto-tra-linguaggi-di-basso-e-alto-livello)
- [Linguaggi intermedi e compilazione](#linguaggi-intermedi-e-compilazione)
- [Scelta del livello di astrazione appropriato](#scelta-del-livello-di-astrazione-appropriato)


I linguaggi di programmazione possono essere classificati in base al loro livello di astrazione, che indica quanto il linguaggio si allontana dalle istruzioni dirette della macchina e si avvicina al linguaggio umano. Questa classificazione è fondamentale per comprendere le capacità, i limiti e gli usi appropriati di diversi linguaggi di programmazione.

### Introduzione ai livelli di astrazione

L'astrazione in programmazione si riferisce al processo di nascondere i dettagli complessi dell'implementazione e fornire un'interfaccia più semplice e intuitiva. I livelli di astrazione nei linguaggi di programmazione vanno dal molto basso (vicino al linguaggio macchina) al molto alto (vicino al linguaggio naturale umano).

> **Definizione**: Il livello di astrazione di un linguaggio di programmazione indica quanto il linguaggio nasconde i dettagli dell'hardware sottostante e fornisce costrutti più vicini al modo in cui gli esseri umani pensano e risolvono problemi.

### Linguaggi di basso livello

I linguaggi di basso livello sono quelli più vicini al linguaggio macchina, offrendo un controllo diretto sull'hardware del computer. Questi includono:

1. **Linguaggio macchina**: 
   - Il livello più basso di astrazione
   - Consiste in sequenze di numeri binari (0 e 1)
   - Direttamente eseguibile dal processore
   - Specifico per ogni architettura di processore

2. **Assembly**:
   - Una rappresentazione simbolica del linguaggio macchina
   - Utilizza mnemonici per le istruzioni (es. MOV, ADD, JMP)
   - Offre una corrispondenza uno-a-uno con le istruzioni macchina
   - Richiede una conoscenza dettagliata dell'architettura hardware

```assembly
; Esempio di codice Assembly (x86)
mov eax, 5    ; Carica il valore 5 nel registro EAX
add eax, 3    ; Aggiunge 3 al valore in EAX
```


### Linguaggi di alto livello

I linguaggi di alto livello sono più vicini al linguaggio umano e offrono un maggiore livello di astrazione. Questi possono essere ulteriormente suddivisi in tre categorie principali: 3GL, 4GL e 5GL.

#### Linguaggi di terza generazione (3GL)

I linguaggi di terza generazione rappresentano un significativo passo avanti nell'astrazione rispetto ai linguaggi assembly, offrendo costrutti più vicini al pensiero umano.

Caratteristiche principali:
- Indipendenza dall'hardware
- Utilizzo di strutture di controllo come cicli e condizioni
- Supporto per tipi di dati complessi e astrazioni come funzioni e oggetti

Esempi di linguaggi 3GL:

1. **C**:
   - Linguaggio di programmazione procedurale
   - Offre un buon equilibrio tra alto livello e controllo di basso livello

```c
#include <stdio.h>

int main() {
    int a = 5, b = 3;
    int somma = a + b;
    printf("La somma di %d e %d è %d\n", a, b, somma);
    return 0;
}
```

2. **Java**:
   - Linguaggio orientato agli oggetti
   - Enfasi sulla portabilità ("write once, run anywhere")

```java
public class Esempio {
    public static void main(String[] args) {
        int a = 5, b = 3;
        int somma = a + b;
        System.out.println("La somma di " + a + " e " + b + " è " + somma);
    }
}
```

3. **Python**:
   - Linguaggio di alto livello con sintassi semplice
   - Supporta paradigmi multipli (procedurale, orientato agli oggetti, funzionale)

```python
a, b = 5, 3
somma = a + b
print(f"La somma di {a} e {b} è {somma}")
```

#### Linguaggi di quarta generazione (4GL)

I linguaggi 4GL sono progettati per aumentare ulteriormente la produttività del programmatore, focalizzandosi sul "cosa" fare piuttosto che sul "come" farlo.

Caratteristiche principali:
- Orientati a domini specifici
- Spesso non procedurali
- Richiedono meno righe di codice rispetto ai 3GL per compiti simili

Esempi di linguaggi 4GL:

1. **SQL (Structured Query Language)**:
   - Linguaggio per la gestione e l'interrogazione di database relazionali

```sql
SELECT nome, cognome
FROM studenti
WHERE anno_iscrizione = 2023 AND media_voti > 27;
```

2. **MATLAB**:
   - Ambiente di programmazione per calcolo numerico e visualizzazione

```matlab
% Creazione e visualizzazione di un grafico
x = 0:0.1:2*pi;
y = sin(x);
plot(x, y);
title('Funzione Seno');
xlabel('x');
ylabel('sin(x)');
```

3. **R**:
   - Linguaggio per analisi statistiche e visualizzazione dati

```r
# Creazione di un grafico a dispersione
x <- rnorm(100)
y <- 2*x + rnorm(100)
plot(x, y, main="Grafico a dispersione", xlab="X", ylab="Y")
abline(lm(y~x), col="red")
```

#### Linguaggi di quinta generazione (5GL)

I linguaggi 5GL rappresentano il più alto livello di astrazione, mirando a risolvere problemi specificando solo gli obiettivi o i vincoli, lasciando al sistema il compito di determinare come raggiungere tali obiettivi.

Caratteristiche principali:
- Basati su vincoli e logica
- Utilizzano tecniche di intelligenza artificiale
- Richiedono una specifica minima del problema

Esempi di linguaggi 5GL:

1. **Prolog**:
   - Linguaggio di programmazione logica
   - Basato su fatti e regole

```prolog
% Definizione di fatti
genitore(anna, mario).
genitore(luigi, mario).
genitore(mario, giovanni).

% Definizione di una regola
nonno(X, Z) :- genitore(X, Y), genitore(Y, Z).

% Query
?- nonno(anna, giovanni).
% Output: true
```

2. **LISP**:
   - Linguaggio funzionale basato su liste
   - Ampiamente utilizzato nell'intelligenza artificiale

Questi esempi illustrano come i linguaggi di più alto livello (4GL e 5GL) permettano di esprimere concetti complessi con meno codice e in modo più vicino al linguaggio naturale o al dominio specifico del problema, rispetto ai linguaggi 3GL. Tuttavia, questa maggiore astrazione spesso comporta una minore flessibilità e un minor controllo sui dettagli di basso livello dell'esecuzione.


### Confronto tra linguaggi di basso e alto livello

| Caratteristica | Linguaggi di basso livello | Linguaggi di alto livello |
| -------------- | -------------------------- | ------------------------- |
| Leggibilità    | Bassa                      | Alta                      |
| Portabilità    | Bassa                      | Alta                      |
| Efficienza     | Alta                       | Variabile                 |
| Sviluppo       | Lento                      | Rapido                    |
| Controllo HW   | Diretto                    | Limitato                  |
| Debugging      | Complesso                  | Più semplice              |

### Linguaggi intermedi e compilazione

Tra i linguaggi di alto livello e il linguaggio macchina, esistono spesso linguaggi intermedi che fungono da ponte nel processo di compilazione come il **Bytecode**, un formato intermedio utilizzato da linguaggi come Java e Python

Questi linguaggi intermedi permettono una maggiore portabilità e ottimizzazione del codice.

### Scelta del livello di astrazione appropriato

La scelta del livello di astrazione dipende da vari fattori:

1. **Tipo di progetto**: Applicazioni di sistema vs applicazioni utente
2. **Requisiti di prestazioni**: Necessità di controllo fine sull'hardware
3. **Tempi di sviluppo**: Rapidità richiesta nello sviluppo
4. **Competenze del team**: Familiarità con linguaggi specifici
5. **Manutenibilità**: Facilità di aggiornamento e debug del codice

> **Nota**: Non esiste un "livello migliore" universale. La scelta ottimale dipende sempre dal contesto specifico del progetto e dalle sue esigenze.

La comprensione dei diversi livelli di astrazione nei linguaggi di programmazione è fondamentale per i programmatori, in quanto permette di scegliere lo strumento più adatto per ogni compito, bilanciando efficienza, produttività e manutenibilità del codice.
