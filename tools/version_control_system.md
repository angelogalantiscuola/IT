### Version Control System

`new` [Using Git with Visual Studio Code](https://www.youtube.com/watch?v=i_23KUAEtUM)

#### Sincronizzare repository locale e repository remoto

##### Autenticazione

- Fare il login su Github
- Fare il login su Vscode (icona in basso a destra)

1. Il primo modo non funziona
2. Il secondo modo non funziona
3. Il terzo modo (con il codice funziona)

##### Download del repository

- Clonare il repository

1. Su Github copiare l'URL del repository
2. Su Vscode cliccare la terza icona del menu a sinistra (Source Control)

##### Aggiornare il repository in locale

- Aggiornare il repository scrivendo del codice

##### Upload delle modifiche su Github

- Sincronizzare il repository locale (del PC) con Github

1. Su Vscode cliccare la terza icona del menu a sinistra (Source Control)
2. Cliccare su commit (le modifiche sono ufficiali ma ancora non sincronizzate)
3. Cliccare su Sincronizza per inviare i cambiamenti a repository Github

# version control

## useful links

- [Controllo versione - Wikipedia](https://it.wikipedia.org/wiki/Controllo_versione) (solo sezione iniziale)

- [Controllo versione distribuito - Wikipedia](https://it.wikipedia.org/wiki/Controllo_versione_distribuito)

- [Git (software) - Wikipedia](https://it.wikipedia.org/wiki/Git_(software)) (solo sezione iniziale)

- [GitHub - Wikipedia](https://it.wikipedia.org/wiki/GitHub)

## why a version control software is important

Il controllo di versione del software è uno **strumento essenziale per la gestione del codice sorgente di un progetto**, poiché consente di risolvere diversi problemi che possono sorgere durante lo sviluppo del software.

1. **Collaborazione**: Il controllo di versione consente a più sviluppatori di lavorare contemporaneamente sullo stesso progetto, senza che le loro modifiche si sovrappongano o causino conflitti.

2. **Backup e recupero**: Il controllo di versione tiene traccia di tutte le modifiche apportate al codice sorgente, in modo che sia possibile ripristinare una versione precedente del progetto in caso di necessità.

3. **Tracciabilità**: Il controllo di versione consente di sapere chi ha apportato modifiche specifiche al codice sorgente e quando sono state effettuate. Ciò consente di risalire a eventuali problemi e di risolverli più facilmente.

4. **Branching**: Il controllo di versione consente di creare diverse versioni del progetto, chiamate "branch", per lavorare su funzionalità differenti senza interferire con le modifiche degli altri sviluppatori.

5. **Integrazione**: Il controllo di versione consente di integrare facilmente le modifiche apportate da più sviluppatori in un unico progetto.

6. **Sviluppo a distanza**: Il controllo di versione consente di lavorare a distanza, condividere e scaricare le modifiche apportate al progetto.

In sintesi, il controllo di versione del software è una necessità per qualsiasi progetto di sviluppo software di medie o grandi dimensioni, poiché consente di gestire efficacemente il codice sorgente, facilitando la collaborazione, la tracciabilità e la gestione delle modifiche al codice.

### Git

Git è un **sistema di controllo versione distribuito** che consente di tenere traccia delle modifiche apportate ai file e di collaborare con altri utenti. Ci sono alcune caratteristiche chiave di Git:

1. **Repository**: ogni progetto in Git ha un repository che contiene tutti i file e la cronologia delle modifiche. I repository possono essere condivisi tra utenti tramite protocolli come HTTPS o SSH.

2. **Branching**: Git consente di creare "branch" (rami) del progetto, che consentono di lavorare su funzionalità diverse contemporaneamente senza interferire con le modifiche degli altri utenti.

3. **Merging**: quando un branch è pronto, le modifiche possono essere fuse (merge) con il branch principale (master). In caso di conflitto, è necessario risolverli manualmente prima di effettuare il merge.

4. **Commit**: ogni volta che si apportano modifiche ai file, si crea un "commit" che registra le modifiche e un messaggio di commit che descrive le modifiche effettuate.

5. **Remote**: i repository possono essere associati a un "remote" repository, che consente di scaricare e caricare i cambiamenti con altri utenti.

6. **Revert**: è possibile tornare indietro a una versione precedente del progetto in qualsiasi momento, utilizzando il comando "revert" o "reset".

In sintesi Git è un sistema flessibile e potente che consente di gestire il codice sorgente in modo efficiente, consentendo di collaborare con altri sviluppatori, mantenere la versione e rollback in caso di necessità.

### Github

GitHub è una **piattaforma web basata su Git che consente agli utenti di creare e gestire repository per i propri progetti.**  GitHub offre molte caratteristiche utili per la collaborazione e la gestione del codice, tra cui:

1. **Interfaccia web**: GitHub offre un'interfaccia web intuitiva per gestire i repository, creare branch, effettuare commit e gestire i pull request.

2. **Collaborazione**: GitHub consente a più utenti di lavorare contemporaneamente su un progetto, di creare branch e di effettuare pull request per integrare le modifiche.

3. **Hosting**: GitHub offre hosting gratuito per i repository pubblici, rendendo facile condividere e scaricare il codice.

4. **Documentazione**: GitHub offre strumenti per la creazione e la gestione della documentazione del progetto, come la possibilità di creare Wiki e pagine di documentazione.

5. **Integrazioni**: GitHub offre un'ampia gamma di integrazioni con altri strumenti di sviluppo, come Jira, Trello e Slack, consentendo di automatizzare i flussi di lavoro e di rendere più efficiente la collaborazione.

6. **Comunità**: GitHub è una grande piattaforma che consente agli utenti di condividere, scoprire e contribuire a progetti open source.

In sintesi, GitHub è una piattaforma web estremamente utile per la gestione dei progetti di sviluppo software, che offre un'interfaccia intuitiva, funzionalità di collaborazione avanzate, hosting gratuito e una grande comunità di sviluppatori.
