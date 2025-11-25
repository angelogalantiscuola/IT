# Piano di Lavoro: Modulo 05 - Sviluppo Applicativo CRUD Completo

## 1. Obiettivi di Apprendimento

### Prerequisiti
*   Sistema di autenticazione funzionante (Modulo 04).
*   Comprensione del Repository Pattern.

### Competenze in Uscita
Al termine di questo modulo, lo studente sarà in grado di:
*   Implementare un **Repository** completo per un'entità complessa (Post).
*   Gestire le **relazioni** tra tabelle (Foreign Key tra Utenti e Post) a livello SQL.
*   Creare route per operazioni **CRUD** (Create, Read, Update, Delete).
*   Utilizzare **Decoratori personalizzati** (`@login_required`) per proteggere le route.
*   Gestire i permessi (es. solo l'autore può modificare il proprio post).
*   Utilizzare i **Flash Messages** per il feedback utente.

## 2. Contenuti Teorici e Pratici

In questo modulo consolideremo l'architettura applicandola al "core business" della nostra applicazione: i post del blog.

*   **Lezione 01: Il Repository dei Post**
    *   **Teoria:** Relazioni 1-a-N in SQL. Join e chiavi esterne.
    *   **Pratica:** Creazione di `app/repositories/post_repo.py`. Scrittura delle funzioni `get_all_posts` (con JOIN per avere il nome dell'autore), `create_post`, `update_post`, `delete_post`.

*   **Lezione 02: Creazione e Visualizzazione (Create & Read)**
    *   **Teoria:** Passaggio di oggetti complessi ai template. Loop nei template (`{% for %}`).
    *   **Pratica:** Creazione del Blueprint `posts.py`. Implementazione della route Homepage (lista post) e della route `create` (protetta da login). Visualizzazione dinamica dei post.

*   **Lezione 03: Modifica, Cancellazione e Protezione (Update & Delete)**
    *   **Teoria:** Autorizzazione vs Autenticazione (chi può fare cosa?). URL parametrici (`/post/<id>/edit`). Pattern PRG (Post/Redirect/Get).
    *   **Pratica:** Implementazione delle route `edit` e `delete`. Controllo lato server: `if post['author_id'] != current_user['id']: abort(403)`. Uso di `flash()` per messaggi di successo/errore.

## 3. Attività Principale: Blog Completo
Gli studenti completeranno il blog. Gli utenti potranno scrivere post, vederli in homepage, e modificare/cancellare solo i propri.
Il progetto finale di questo modulo sarà un'applicazione web completa, sicura e ben architettata, pronta per il deployment.

## 4. Metodologie di Valutazione
*   Verifica funzionale: Il CRUD funziona?
*   Verifica di sicurezza: Un utente può cancellare il post di un altro utente "indovinando" l'URL? (Test manuale).
*   Code Review: Qualità del codice nel `post_repository.py`.