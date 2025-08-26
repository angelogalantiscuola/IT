# Introduzione alla Programmazione

## 1. Che cos'è la Programmazione?

La programmazione è l'arte di dare istruzioni a un computer per fargli svolgere un compito. Possiamo pensarla come una ricetta di cucina: una serie di passaggi chiari e sequenziali che, se seguiti correttamente, portano a un risultato desiderato.

Queste istruzioni sono scritte in un **linguaggio di programmazione** (come Python), una lingua speciale che sia noi umani che i computer possiamo capire.

---

## 2. I Blocchi Fondamentali del Codice

Ogni programma si costruisce a partire da tre elementi fondamentali. Capire questi tre blocchi significa capire il cuore della programmazione.

### a) Le Variabili: Contenitori di Dati

Una variabile è come una scatola con un'etichetta. L'etichetta è il **nome** della variabile e il contenuto è il suo **valore**. Le usiamo per memorizzare le informazioni che il nostro programma deve ricordare.

```python
# Una variabile di tipo stringa (testo)
nome = "Marco"

# Una variabile di tipo intero (numero)
eta = 16
```

### b) Le Istruzioni: Le Azioni

Un'istruzione è un singolo comando che il computer esegue. Può essere un calcolo, la visualizzazione di un messaggio o la modifica del valore di una variabile.

```python
# L'istruzione 'print' mostra un messaggio sullo schermo
print("Ciao mondo!")

# Un'istruzione di assegnazione che modifica il valore della variabile 'eta'
eta = eta + 1  # Ora 'eta' contiene 17
```

### c) Il Controllo del Flusso: Decisioni e Ripetizioni

Il controllo del flusso ci permette di decidere **quali** istruzioni eseguire e **quante volte**.

*   **Selezione (Decisioni)**: Esegue un blocco di codice solo se una certa condizione è vera. Si usa `if/else`.

    ```python
    if eta >= 18:
        print("Sei maggiorenne.")
    else:
        print("Sei minorenne.")
    ```

*   **Iterazione (Cicli)**: Ripete un blocco di codice più volte. Il ciclo `for` è il più comune per questo scopo.

    ```python
    # Stampa i numeri da 0 a 4
    for i in range(5):
        print(i)
    ```

---

## 3. Il Tuo Primo Programma Interattivo

Un programma diventa davvero utile quando può interagire con l'utente. Scriviamo un piccolo programma che combina tutto ciò che abbiamo visto.

```python
# Programma che saluta l'utente e valuta la sua età

# 1. Input: Chiediamo all'utente il suo nome e lo salviamo nella variabile 'nome'
nome = input("Come ti chiami? ")

# 2. Output: Usiamo il nome per creare un saluto personalizzato
print(f"Ciao {nome}! Benvenuto nel mondo della programmazione!")

# 3. Input e Conversione: Chiediamo l'età e la convertiamo in un numero intero
eta_testuale = input("Quanti anni hai? ")
eta_numerica = int(eta_testuale)

# 4. Selezione: Eseguiamo un controllo sull'età
if eta_numerica < 18:
    print("Sei giovane! L'avventura è appena iniziata.")
else:
    print("Sei un adulto! Non si smette mai di imparare.")
```

---

## 4. I Grandi Concetti: Paradigmi e Livelli di Astrazione

Per capire meglio il mondo della programmazione, è utile conoscere due concetti che ne definiscono l'architettura: lo stile di scrittura (paradigma) e la "lingua" che si usa (livello di astrazione).

### a) Paradigmi di Programmazione: Gli Stili

Un **paradigma** è uno "stile" fondamentale con cui si progetta e si scrive il codice.

*   **Paradigma Imperativo**: Si concentra sul **"COME"** il computer deve risolvere un problema. Si scrivono istruzioni passo-passo che modificano lo stato del programma.
    *   **Analogia**: Scrivere una ricetta dettagliata. "Primo, prendi le uova. Secondo, rompile in una ciotola. Terzo, aggiungi lo zucchero..."
    *   **Esempio (Python)**: Calcolare la somma di una lista di numeri. Diciamo al computer esattamente come fare: crea una variabile per la somma, scorri ogni numero e aggiungilo alla somma.
        ```python
        numeri =
        somma = 0
        for numero in numeri:
            somma = somma + numero
        print(somma) # Output: 60
        ```

*   **Paradigma Dichiarativo**: Si concentra sul **"COSA"** si vuole ottenere, lasciando al linguaggio il compito di capire come farlo.
    *   **Analogia**: Ordinare una pizza. Dici al cameriere "Voglio una margherita", senza specificare come il pizzaiolo debba impastare, stendere il pomodoro e cuocere. Dichiari solo il risultato finale.
    *   **Esempio (SQL)**: Selezionare tutti gli studenti con un voto superiore a 8 da una tabella.
        ```sql
        SELECT nome FROM studenti WHERE voto > 8;
        ```
        Non diciamo al database *come* cercare, ma solo *cosa* vogliamo.

Noi inizieremo con il paradigma **imperativo**, perché ci aiuta a capire la logica fondamentale del computer. Più avanti, incontrerete altri paradigmi come la **Programmazione Orientata agli Oggetti (OOP)**.

### b) Livelli di Astrazione: La Distanza dalla Macchina

L'**astrazione** indica quanto un linguaggio di programmazione sia "lontano" dal linguaggio nativo del processore (fatto di 0 e 1) e "vicino" al linguaggio umano. Vediamo un esempio pratico per rendere la differenza chiarissima: sommare due numeri.

*   **Linguaggi di Basso Livello (es. Assembly)**
    Sono molto vicini all'hardware. Per eseguire una semplice addizione, dobbiamo comunicare direttamente con il processore (la CPU), spostando i dati nei suoi "cassetti" interni chiamati registri.
    
    *   **Analogia**: Parlare con un meccanico usando il gergo tecnico dei singoli componenti del motore. È un linguaggio potente ma comprensibile solo a pochi esperti.

    *   **Esempio (sommare 5 + 3 in Assembly)**:
        ```assembly
        MOV EAX, 5  ; Metti il numero 5 nel registro EAX
        MOV EBX, 3  ; Metti il numero 3 nel registro EBX
        ADD EAX, EBX ; Somma EBX a EAX (il risultato, 8, rimane in EAX)
        ```
        Come puoi vedere, una singola idea (5 + 3) richiede **multiple istruzioni** specifiche per un certo tipo di processore.

*   **Linguaggi di Alto Livello (es. Python)**
    Sono più simili al linguaggio umano. Nascondono tutta la complessità dell'hardware, permettendoci di esprimerci in modo più naturale.

    *   **Analogia**: Guidare un'automobile. Usi comandi semplici (volante, pedali) che funzionano su quasi tutte le auto, senza bisogno di sapere come funziona il motore.

    *   **Esempio (sommare 5 + 3 in Python)**:
        ```python
        somma = 5 + 3
        ```
        Questa singola riga è tutto ciò che serve. Python si occupa di tradurre questa semplice istruzione in tutte le complesse operazioni di basso livello necessarie per eseguirla. Il grande vantaggio è che questo codice funzionerà su qualsiasi computer.

Noi utilizzeremo **Python**, un linguaggio di altissimo livello, che ci permette di concentrarci sulla **logica** per risolvere problemi, invece che sui dettagli tecnici della macchina.