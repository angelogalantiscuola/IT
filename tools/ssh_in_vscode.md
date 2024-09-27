# SSH in VSCode <!-- omit in toc -->

- [Usare SSH per connettersi ad un server remoto in VSCode](#usare-ssh-per-connettersi-ad-un-server-remoto-in-vscode)
- [Prerequisiti](#prerequisiti)
- [Installazione dell'estensione Remote - SSH](#installazione-dellestensione-remote---ssh)
- [Configurazione della connessione SSH](#configurazione-della-connessione-ssh)
- [Connessione al server remoto](#connessione-al-server-remoto)
- [Gestione delle connessioni SSH](#gestione-delle-connessioni-ssh)

### Usare SSH per connettersi ad un server remoto in VSCode

Visual Studio Code (VSCode) offre una potente estensione chiamata **Remote - SSH** che permette di connettersi a un server remoto utilizzando SSH. Questa funzionalità è particolarmente utile per sviluppare e testare codice direttamente su un server remoto, mantenendo l'ambiente di sviluppo locale.

### Prerequisiti

Prima di iniziare, assicurati di avere i seguenti prerequisiti:

- **VSCode** installato sul tuo computer.
- **Accesso SSH** al server remoto con le credenziali appropriate.
- **OpenSSH client** installato sul tuo sistema locale (disponibile nativamente su Linux e macOS, su Windows può essere installato tramite le funzionalità opzionali).
- 
### Installazione dell'estensione Remote - SSH

1. **Apri VSCode**.
2. **Vai alla sezione delle estensioni** cliccando sull'icona delle estensioni nella barra laterale sinistra o premendo `Ctrl+Shift+X`.
3. **Cerca "Remote - SSH"** nella barra di ricerca.
4. **Installa l'estensione** cliccando sul pulsante "Installa".

### Configurazione della connessione SSH

1. **Apri il comando "Remote-SSH: Connect to Host..."**:
   - Premi `F1` per aprire la palette dei comandi.
   - Digita `Remote-SSH: Connect to Host...` e seleziona l'opzione.

2. **Aggiungi una nuova configurazione SSH**:
   - Seleziona `Add New SSH Host...`.
   - Inserisci il comando SSH per connetterti al server remoto (ad esempio, `ssh user@hostname`).
   - Scegli il file di configurazione SSH in cui salvare questa configurazione (di solito `~/.ssh/config`).

3. **Modifica il file di configurazione SSH** (opzionale):
   - Apri il file `~/.ssh/config` e verifica che la configurazione sia corretta. Puoi aggiungere opzioni come la chiave privata, il port forwarding, ecc.
     ```plaintext
     Host myserver
         HostName hostname
         User user
         IdentityFile ~/.ssh/id_rsa
     ```

### Connessione al server remoto

1. **Apri il comando "Remote-SSH: Connect to Host..."**:
   - Premi `F1` per aprire la palette dei comandi.
   - Digita `Remote-SSH: Connect to Host...` e seleziona l'opzione.

2. **Seleziona il server remoto**:
   - Scegli il server remoto dalla lista delle configurazioni SSH salvate.

3. **Autenticazione**:
   - Inserisci la password o utilizza la chiave privata per autenticarti sul server remoto.

4. **Apri una nuova finestra di VSCode**:
   - Una volta connesso, VSCode aprirà una nuova finestra connessa al server remoto. Potrai navigare e modificare i file come se fossero locali.

### Gestione delle connessioni SSH

- **Visualizzare le connessioni attive**:
  - Puoi visualizzare le connessioni SSH attive e gestirle tramite la sezione "Remote Explorer" nella barra laterale sinistra di VSCode.

- **Chiudere una connessione SSH**:
  - Per chiudere una connessione SSH, basta chiudere la finestra di VSCode connessa al server remoto.

Utilizzando l'estensione Remote - SSH di VSCode, puoi facilmente connetterti a server remoti e lavorare direttamente sui file e progetti ospitati su di essi, migliorando la tua produttività e flessibilità nello sviluppo software.