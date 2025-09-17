## Nozioni di Sicurezza dei Database <!-- omit in toc -->

- [Principi Chiave della Sicurezza](#principi-chiave-della-sicurezza)
- [Principali Vettori di Attacco](#principali-vettori-di-attacco)

La sicurezza dei database è un aspetto fondamentale per garantire l'**integrità**, la **riservatezza** e la **disponibilità** dei dati (principio "CIA" - Confidentiality, Integrity, Availability). Senza adeguate misure di protezione, un database può essere vulnerabile ad accessi non autorizzati, furti di dati e attacchi malevoli.

### Principi Chiave della Sicurezza

1.  **Autenticazione**: È il processo di verifica dell'identità di un utente. È la prima linea di difesa e si basa tipicamente su username e password, ma può includere metodi più robusti come l'autenticazione a più fattori.

2.  **Autorizzazione**: Una volta che un utente è autenticato, l'autorizzazione definisce _cosa_ quell'utente può fare. Questo si gestisce tramite **permessi** e **ruoli**. Il **Principio del Minimo Privilegio** è fondamentale: ogni utente dovrebbe avere solo i permessi strettamente necessari per svolgere le proprie mansioni.

3.  **Audit**: Consiste nel tenere traccia di chi fa cosa e quando. I log del database sono essenziali per monitorare le attività, individuare comportamenti sospetti e analizzare incidenti di sicurezza.

4.  **Crittografia**: Protegge i dati rendendoli illeggibili a chi non possiede la chiave di decifrazione. Si applica a:
    - **Dati in transito**: Dati che viaggiano sulla rete tra l'applicazione e il database (protetti con protocolli come SSL/TLS).
    - **Dati a riposo**: Dati memorizzati fisicamente su disco.

### Principali Vettori di Attacco

- **SQL Injection**: L'iniezione di codice SQL malevolo tramite gli input dell'utente per manipolare le query del database.
- **Credenziali Deboli o Rubate**: L'uso di password semplici o la loro esposizione permette un facile accesso non autorizzato.
- **Configurazioni Errate**: Un DBMS con impostazioni di sicurezza di default o non correttamente configurato (es. porte aperte inutilmente) può esporre a rischi.
- **Mancanza di Aggiornamenti**: Non applicare le patch di sicurezza rilasciate dai produttori del DBMS lascia il sistema vulnerabile a exploit noti.
