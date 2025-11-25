# Piano di Lavoro: Modulo 03 - Architettura Web Professionale con Flask

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Conoscenza base di Python (funzioni, moduli, importazioni).
*   Basi di HTML e CSS.
*   Concetti teorici del Modulo 02 (HTTP, Request/Response).

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Configurare un ambiente di sviluppo professionale per Python (`venv`).
*   Strutturare un'applicazione web come **pacchetto Python** (`__init__.py`).
*   Implementare il pattern **Application Factory** per creare e configurare l'istanza dell'app.
*   Utilizzare i **Blueprints** per organizzare le route in moduli logici separati fin dal primo giorno.
*   Creare pagine HTML dinamiche utilizzando il motore di template **Jinja2** e l'ereditarietà dei template.
*   Comprendere la separazione tra la logica di routing (Python) e la presentazione (HTML).

## 2. Contenuti Teorici e Pratici

In questo modulo non scriveremo codice "usa e getta". Imposteremo fin da subito la struttura che useremo fino alla fine dell'anno e nel progetto d'esame.

*   **Lezione 01: Setup del Progetto e Application Factory**
    *   **Teoria:** Perché strutturare un'app come pacchetto. Il ruolo di `__init__.py`. Il pattern Factory (`create_app`) per una configurazione flessibile e scalabile.
    *   **Pratica:** Creazione delle cartelle `app/`, `instance/`. Scrittura di `run.py` (entry point esterno) e della factory in `app/__init__.py`. Avvio del server di sviluppo.

*   **Lezione 02: Routing Modulare con i Blueprints**
    *   **Teoria:** Il problema del file unico. Cos'è un Blueprint. Come registrare i Blueprint nella factory.
    *   **Pratica:** Creazione del primo modulo `app/main.py` (o `pages.py`) come Blueprint. Definizione delle route per la Homepage (`/`) e per la pagina About (`/about`). Collegamento del Blueprint all'app principale.

*   **Lezione 03: Il Motore di Template Jinja2**
    *   **Teoria:** Server-Side Rendering. Separazione tra logica e vista. Sintassi base di Jinja2 (`{{ }}`, `{% %}`).
    *   **Pratica:** Creazione della struttura `app/templates/`. Implementazione del layout base (`base.html`) e delle pagine figlie (`home.html`, `about.html`) usando l'ereditarietà (`{% extends %}`). Passaggio di dati semplici (stringhe, liste) dal Python all'HTML.

## 3. Attività Principale: Lo Scheletro del Blog
Gli studenti creeranno la struttura di base del progetto "Blog Scolastico".
Alla fine del modulo, l'applicazione sarà navigabile (Home, About) e avrà un layout grafico coerente, ma i contenuti saranno ancora statici o passati manualmente dalle route. Non ci sarà ancora nessun database.

## 4. Metodologie di Valutazione
*   Verifica della corretta alberatura delle cartelle e dei file (presenza di `__init__.py`, cartelle separate).
*   Capacità di aggiungere una nuova pagina statica (nuova route nel Blueprint + nuovo template HTML) senza rompere l'applicazione.