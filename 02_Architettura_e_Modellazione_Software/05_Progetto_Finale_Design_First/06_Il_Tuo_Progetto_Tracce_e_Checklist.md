# Ora Tocca a Te: Il Tuo Progetto Finale (Tracce e Checklist)

Hai visto come abbiamo costruito il nostro *Progetto Faro* (l'RPG) partendo da una semplice richiesta fino a un software funzionante e collaudato al 100%.

Ora tocca a te vestire i panni dell'**Ingegnere del Software**: sceglierai una traccia e la svilupperai applicando rigorosamente la metodologia **Design-First**.

---

## 📋 La Checklist di Progetto (Da includere nel tuo README)

Il tuo repository GitHub finale dovrà contenere tutti gli artefatti spuntati in questa checklist:

```markdown
### FASE 1: ARCHITETTURA & REQUISITI
- [ ] C4 Model Livello 1 (System Context in Mermaid)
- [ ] C4 Model Livello 2 (Container in Mermaid)
- [ ] Almeno 3-4 User Stories complete di Criteri di Accettazione (Definition of Done)

### FASE 2: MODELLAZIONE STATICA DEI DATI (ER & UML)
- [ ] Diagramma ER (Mermaid) con Primary Key (PK) e Foreign Key (FK)
- [ ] Relazione 1:1 correttamente gestita
- [ ] Relazione 1:N correttamente posizionata (FK sul lato molti)
- [ ] Relazione N:N scomposta tramite l'Entità/Tabella di Raccordo
- [ ] Diagramma delle Classi UML in parallelo (con attributi tipizzati)

### FASE 3: MODELLAZIONE DINAMICA (SEQUENZA)
- [ ] Un Diagramma di Sequenza (Mermaid) per CIASCUNA User Story definita
- [ ] Metodi pubblici del Class Diagram derivati direttamente dalle frecce di sequenza

### FASE 4: SVILUPPO IN PYTHON
- [ ] Struttura cartelle modulare (`src/` per il codice, `tests/` per i test)
- [ ] Entità implementate con `@dataclass` e Type Hinting esplicito
- [ ] Gestione delle relazioni (riferimenti singoli, liste con `field(default_factory=list)`)
- [ ] Ereditarietà a 1 livello (`super().__init__()`) e Polimorfismo con override
- [ ] Modulo di persistenza per salvare e ricaricare lo stato su file `JSON`

### FASE 5: QUALITÀ E COLLAUDO
- [ ] Suite di test Pytest nella cartella `tests/` (almeno 1 test per ogni User Story)
- [ ] Tutti i test superati al 100% (`pytest` verde)
- [ ] Codice formattato e verificato con Ruff (`ruff check .` e `ruff format .`)
- [ ] Documentazione completa nel file `README.md`
```
