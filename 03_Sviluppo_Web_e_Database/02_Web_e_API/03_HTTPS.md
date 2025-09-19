## HTTPS: Sicurezza nella Comunicazione Web <!-- omit in toc -->

- [Perché HTTP non è sufficiente?](#perché-http-non-è-sufficiente)
- [Cos'è HTTPS?](#cosè-https)
- [Come Funziona HTTPS: Crittografia e Certificati](#come-funziona-https-crittografia-e-certificati)
  - [1. Il "TLS Handshake"](#1-il-tls-handshake)
  - [2. La Comunicazione Cifrata](#2-la-comunicazione-cifrata)
- [Le Certificate Authority (CA)](#le-certificate-authority-ca)

### Perché HTTP non è sufficiente?

Il protocollo HTTP, nella sua forma base, trasmette i dati in **testo in chiaro**. Questo significa che chiunque si trovi "in mezzo" alla comunicazione tra il client e il server (es. un malintenzionato sulla stessa rete Wi-Fi) può intercettare e leggere facilmente le informazioni scambiate. Questo è estremamente pericoloso, specialmente se i dati trasmessi sono sensibili, come password, numeri di carte di credito o messaggi privati.

### Cos'è HTTPS?

**HTTPS (HyperText Transfer Protocol Secure)** non è un protocollo separato, ma è semplicemente il protocollo **HTTP incapsulato all'interno di un livello di sicurezza**, chiamato **TLS (Transport Layer Security)**, o il suo predecessore, SSL (Secure Sockets Layer).

HTTPS fornisce tre garanzie di sicurezza fondamentali:

1.  **Crittografia**: I dati scambiati tra client e server sono cifrati, rendendoli incomprensibili a chiunque li intercetti.
2.  **Integrità**: Garantisce che i dati non vengano alterati durante la trasmissione.
3.  **Autenticazione**: Verifica che il server con cui si sta comunicando sia effettivamente chi dice di essere, proteggendo da attacchi "man-in-the-middle".

### Come Funziona HTTPS: Crittografia e Certificati

Il processo si basa sulla **crittografia a chiave pubblica/privata** e sui **certificati digitali**.

#### 1. Il "TLS Handshake"

Quando un client (il tuo browser) si connette a un server tramite HTTPS, avviene un processo di negoziazione chiamato "handshake":

1.  **Client Hello**: Il client invia un messaggio al server, dicendo "Ciao, voglio stabilire una connessione sicura".
2.  **Server Hello**: Il server risponde inviando il suo **certificato SSL/TLS**.
3.  **Verifica del Certificato**: Il browser controlla che il certificato sia valido e che sia stato emesso da un'autorità di certificazione (CA) attendibile. Questo certificato contiene la **chiave pubblica** del server.
4.  **Generazione Chiave di Sessione**: Se il certificato è valido, il browser genera una **chiave di sessione** simmetrica (una chiave segreta temporanea).
5.  **Invio Sicuro della Chiave**: Il browser cifra la chiave di sessione appena creata utilizzando la **chiave pubblica del server** e la invia al server.
6.  **Inizio della Sessione Sicura**: Solo il server, con la sua **chiave privata** corrispondente, può decifrare il messaggio e ottenere la chiave di sessione.

#### 2. La Comunicazione Cifrata

Da questo momento in poi, sia il client che il server possiedono la stessa **chiave di sessione simmetrica**. Tutta la comunicazione successiva viene cifrata e decifrata utilizzando questa chiave, che è molto più veloce della crittografia a chiave pubblica/privata, rendendo la connessione sicura ed efficiente.

### Le Certificate Authority (CA)

Come fa il browser a fidarsi del certificato di un server? Perché è stato firmato digitalmente da una **Certificate Authority (CA)**, un'entità di fiducia (come Let's Encrypt, DigiCert, ecc.). I sistemi operativi e i browser hanno un elenco preinstallato di CA attendibili. Se un certificato è firmato da una di queste, il browser lo considera valido, garantendo l'autenticità del server.
