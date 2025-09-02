# Mappa Concettuale: Qualità e Testing per il Web

Questa mappa mostra come i principi del testing automatico vengono applicati al dominio specifico delle applicazioni web, concentrandosi sulla simulazione delle interazioni utente e sulla verifica dei flussi di lavoro completi.

```mermaid
graph TD
    A[Testing per il Web] --> B[Perché Testare un'App Web?];
    A --> C[Setup dell'Ambiente];
    A --> D[Come si Testa?];

    subgraph  Obiettivi 
        B --> B1[Prevenire Regressioni<br>  Una nuova feature non deve rompere le vecchie  ];
        B1 --> B2[Garantire la Sicurezza<br>  Le pagine protette sono davvero protette?  ];
        B2 --> B3[Validare la Logica di Business<br>  Il CRUD funziona come previsto?  ];
    end

    subgraph  Preparazione 
        C --> C1[Installazione di<br><code>pytest-flask</code>];
        C1 --> C2[Configurazione di Test<br> Database separato ];
        C2 --> C3[La Fixture <code>client</code><br>Il nostro  browser virtuale ];
    end

    subgraph  Tecniche di Test 
        D --> D1[Simulare Richieste HTTP<br><code>client.get  </code>, <code>client.post  </code>];
        D1 --> D2[Verificare le Risposte<br>Assert su Status Code, Contenuto HTML];
        D2 --> D3[Testare i Flussi Utente];
        D3 --> D4[**Autenticazione**<br> Login, Logout, Pagine Protette ];
        D3 --> D5[**Operazioni CRUD**<br> Creazione, Modifica, Cancellazione ];
        D5 --> D6[Verifica dello Stato del Database<br>  L'operazione ha avuto l'effetto atteso sui dati?  ];
    end