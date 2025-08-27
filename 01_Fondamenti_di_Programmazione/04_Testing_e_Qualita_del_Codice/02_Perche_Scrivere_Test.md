# Perché Scrivere Test?

Fino ad ora, per verificare se il nostro codice funzionava, abbiamo probabilmente usato un metodo molto semplice: aggiungere delle istruzioni `print()` e lanciare lo script per vedere cosa succedeva. Questo si chiama **testing manuale**.

Il testing manuale va bene per script di poche righe, ma ha enormi limiti quando i progetti crescono:
*   **È noioso e ripetitivo:** Devi lanciare il programma e inserire gli stessi input ogni volta.
*   **È soggetto a errori:** È facile dimenticarsi di provare un caso specifico o interpretare male un risultato.
*   **Non è scalabile:** Se hai 50 funzioni, testarle tutte a mano dopo ogni modifica diventa un lavoro a tempo pieno.

Per questi motivi, gli sviluppatori professionisti si affidano al **testing automatico**.

## 1. Cos'è il Testing Automatico?

Il testing automatico consiste nello scrivere del codice il cui unico scopo è **verificare che altro codice funzioni come previsto**. Questi "script di verifica" si chiamano **test**.

*   **Analogia**: Pensa di costruire un ponte. Il testing manuale è come farci passare sopra un'auto e sperare che regga. Il testing automatico è come portare il ponte in un laboratorio e usare macchinari specializzati per applicare carichi precisi e misurare la resistenza, garantendo che rispetti le specifiche di progetto.

## 2. I Vantaggi del Testing Automatico

Scrivere test richiede tempo, ma è un investimento che ripaga enormemente.

### a) La Rete di Sicurezza (Prevenzione delle Regressioni)
Questa è la ragione più importante. Una "regressione" è un bug che si introduce in una funzionalità che prima funzionava.
Immagina di avere un'applicazione complessa. Aggiungi una nuova funzionalità e, senza accorgertene, rompi qualcos'altro in un'altra parte del programma. Con una buona suite di test, puoi lanciare un singolo comando e verificare in pochi secondi che tutto il resto dell'applicazione funzioni ancora perfettamente. I test sono la tua **rete di sicurezza** contro gli errori imprevisti.

### b) Documentazione Vivente
Un test ben scritto è una forma di documentazione. Mostra in modo inequivocabile cosa dovrebbe fare una funzione con un dato input. Un nuovo sviluppatore può leggere i test per capire come usare il tuo codice.
A differenza della documentazione tradizionale, i test non possono diventare obsoleti: se il codice cambia e il test non viene aggiornato, il test fallirà.

### c) Migliore Progettazione del Codice
Scrivere codice "testabile" ti spinge a progettarlo meglio. Incoraggia a scrivere funzioni piccole, focalizzate su un singolo compito e che non dipendano da troppe parti esterne (le cosiddette "funzioni pure"). Questo porta naturalmente a un codice più pulito, modulare e facile da mantenere.

## 3. La Piramide del Testing: Focus sugli Unit Test

Esistono diversi tipi di test. Una famosa metafora è la "piramide del testing", che li classifica in base al loro scopo e al loro numero. Alla base della piramide ci sono gli **Unit Test**.

Uno **Unit Test** verifica la più piccola unità di codice possibile in modo isolato. Nel nostro caso, l'unità perfetta è una singola **funzione**.

L'obiettivo di uno unit test è rispondere a una domanda molto semplice e precisa: "Se passo a *questa* funzione *questo* input, mi restituisce *questo* output atteso?".

Per il momento, ci concentreremo esclusivamente sugli unit test. Sono i più veloci da scrivere ed eseguire, e costituiscono la solida base di ogni strategia di testing professionale.