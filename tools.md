# Tools

### VS Code

`new` [Basic Editing](https://code.visualstudio.com/docs/editor/codebasics)

- multiple selections (multi-cursor)
- column (box) selection
- find and replace
- search and replace across files
- intellisense
- formatting
- folding
- indentation

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

### Remote VSCode coding

- Connettersi con VSCode tramite il protocollo SSH ad una macchina remota:

[Remote VSCode Coding](https://docs.google.com/document/d/1Hj421cgJWSpHDKt7EvSvzY98OCbt7lCXVqEd5uTHEic/edit?usp=sharing)

1. Premi F1 su VSCode: Seleziona Remote-SSH: Add New SSH Host
2. Inserire: `ssh cognome@10.40.71.194 # per 4M   ssh cognome@10.40.71.199 # per 3M`
3. Invio fino a che non si chiude la finestra
4. Premi F1 su VSCode
5. Seleziona Remote-SSH: Connect to Host
6. Seleziona l'host creato in precedenza
7. Seleziona sistema operativo Linux se lo chiede
8. Quando chiede la password digita x
9. Verificare di essere connesso in basso a sinistra in VSCode

- Comandi linux:
[Linux commands](https://docs.google.com/document/d/1u4588J1EoBhTUW47ElZJBVZg-SvuUbf_xVKA3qQOmyI/edit?usp=sharing)
- Eseguire il codice sulla macchina remota, creare un repository, sincronizzare i repository con Github:
[Sync a repository with Github](https://docs.google.com/document/d/1VSPMp390ovSXxyrg4O-Z2Uw_wgZ9vl-5woab78Ub05A/edit?usp=sharing)
