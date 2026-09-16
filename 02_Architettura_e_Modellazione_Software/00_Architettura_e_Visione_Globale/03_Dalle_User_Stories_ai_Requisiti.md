# Dalle User Stories ai Requisiti Funzionali

Prima di modellare classi e tabelle, dobbiamo rispondere a una domanda fondamentale: **Cosa deve saper fare concretamente il nostro sistema?**

Nel passato si usavano diagrammi complessi e burocratici (come i vecchi casi d'uso con decine di ovali e frecce `<<include>>`). Nel software moderno si preferisce un formato agile, chiaro e condiviso: le **User Stories**.

---

## 1. La Formula della User Story

Una User Story è una frase semplice scritta dal punto di vista dell'utilizzatore finale:

$$\text{Come } \textbf{[Ruolo/Attore]} \text{ voglio } \textbf{[Azione/Funzionalità]} \text{ per } \textbf{[Beneficio/Scopo]}$$

### I 3 Elementi Chiave:
1. **Come [Chi?]:** Identifica chi esegue l'azione (es. *Cliente*, *Amministratore*, *Giocatore*).
2. **Voglio [Cosa?]:** Descrive l'azione specifica che l'utente desidera compiere.
3. **Per [Perché?]:** Spiega il reale valore aggiunto o il beneficio atteso.

---

## 2. Esempi Pratici (Dal Gioco RPG all'E-commerce)

### Esempio A: Il Gioco di Ruolo (RPG)
* *"Come **Giocatore**, voglio **equipaggiare una pozione dall'inventario**, per **recuperare punti vita durante il combattimento**."*
* *"Come **Mago**, voglio **lanciare un incantesimo di fuoco**, per **infliggere danni magici consumando punti mana**."*

### Esempio B: Piattaforma E-commerce
* *"Come **Cliente**, voglio **filtrare i prodotti per categoria di prezzo**, per **trovare rapidamente articoli nel mio budget**."*
* *"Come **Gestore del Magazzino**, voglio **aggiornare la disponibilità dei pezzi**, per **evitare che i clienti acquistino prodotti esauriti**."*

---

## 3. I Criteri di Accettazione: Il Ponte verso i Test

Una User Story da sola può essere vaga. Per renderla inequivocabile aggiungiamo sempre i **Criteri di Accettazione** (le condizioni che devono essere vere affinché la funzionalità sia considerata finita e corretta).

> **User Story:** 
> *"Come Giocatore, voglio bere una pozione curativa per ripristinare i punti vita."*
>
> **Criteri di Accettazione (Definition of Done):**
> - [ ] Se i punti vita attuali sono < 100, la pozione aggiunge 30 PV.
> - [ ] I punti vita non possono mai superare il valore massimo di 100 (nessun overflow).
> - [ ] Dopo l'uso, la pozione deve essere rimossa dall'inventario (quantità - 1).
> - [ ] Se l'inventario ha 0 pozioni, il comando deve restituire un messaggio di errore chiaro.

---

## 4. Dalla User Story alla Modellazione del Software

Guarda come dai criteri di accettazione emergono spontaneamente gli elementi che modelleremo nei prossimi moduli:

1. **I Sostantivi $\longrightarrow$ Le Entità / Tabelle (Modulo 01):** `Giocatore`, `Pozione`, `Inventario`.
2. **Le Azioni $\longrightarrow$ I Metodi e la Sequenza (Modulo 02):** `bevi_pozione()`, `rimuovi()`.
3. **I Vincoli $\longrightarrow$ I Test Pytest e l'Incapsulamento (Moduli 03 e 05):** `assert punti_vita <= 100`.

---

## 🎯 Regola Aurea dell'Architetto Software:
> *"Non si scrive mai un diagramma o una riga di codice senza sapere a quale User Story e a quale Criterio di Accettazione sta rispondendo."*