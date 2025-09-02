# Piano di Lavoro: Modulo 02 - Costruzione delle Classi

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Comprensione del concetto di classe, oggetto, attributo e metodo.
*   Capacità di creare un diagramma UML di base e una classe Python semplice.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Utilizzare il costruttore `__init__` per inizializzare correttamente lo stato di un oggetto.
*   Spiegare il principio dell'incapsulamento e applicarlo usando la convenzione Python per gli attributi privati.
*   Aggiornare un diagramma UML per indicare la visibilità (pubblica/privata) di attributi e metodi.
*   Implementare l'accesso controllato agli attributi privati tramite le `@property` (getter e setter).
*   Aggiungere logica di validazione all'interno dei setter.
*   Rendere le classi più espressive implementando i metodi speciali `__str__` e `__repr__`.

## 2. Contenuti Teorici
Le lezioni di riferimento per questo modulo sono:

*   **Lezione 01:** `02_Costruttori_e_Incapsulamento.md`
    *   **Argomenti:** Il ruolo fondamentale del costruttore `__init__`, il concetto di "nascondere i dati" (incapsulamento) e la sintassi Python (`__`) per gli attributi privati.
*   **Lezione 02:** `03_Accesso_Controllato_Properties.md`
    *   **Argomenti:** L'approccio "Pythonic" all'incapsulamento tramite i decoratori `@property` e `@*.setter` per creare getter e setter eleganti e funzionali.
*   **Lezione 03:** `04_Metodi_Speciali.md`
    *   **Argomenti:** Come personalizzare il comportamento degli oggetti definendo metodi speciali, con un focus su `__str__` per una rappresentazione leggibile dall'utente.

## 3. Attività Pratiche / Esercitazioni

Continueremo a lavorare sul nostro "progetto fil rouge" (RPG), evolvendo le classi create nel modulo precedente.

*   **Refactoring Guidato:** Modificheremo insieme la classe `Personaggio` per introdurre un costruttore robusto, rendere i suoi attributi privati e implementare l'accesso controllato tramite properties.
*   **Esercizio Individuale:** `Esercizi/02_L_Eroe_Prende_Vita.md`. Gli studenti applicheranno gli stessi concetti alla classe `Nemico`, implementando costruttori, incapsulamento, validazione dati e una rappresentazione testuale personalizzata.

## 4. Metodologie di Valutazione

*   **Correzione Esercizi:** L'esercizio `02_L_Eroe_Prende_Vita.md` sarà il principale strumento di valutazione, verificando la corretta applicazione di tutti i concetti del modulo.
*   **Domande Mirate:** Durante la lezione, verranno poste domande per verificare la comprensione della differenza tra `__init__` e un metodo normale, lo scopo dell'incapsulamento e l'utilità di `__str__`.

## 5. Strumenti Necessari

*   Tutti gli strumenti del modulo precedente.