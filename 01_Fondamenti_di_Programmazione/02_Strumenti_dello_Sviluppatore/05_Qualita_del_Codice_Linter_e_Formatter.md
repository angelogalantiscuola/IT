# Qualità del Codice: Linter e Formatter (con Ruff)

Scrivere codice che "funziona" è solo metà del lavoro. Scrivere codice **pulito, ordinato e leggibile** è ciò che rende il nostro lavoro professionale.

Invece di perdere tempo a sistemare a mano gli spazi, i rientri o a cercare variabili dimenticate, usiamo due assistenti automatici invisibili dentro VS Code: il **Linter** e il **Formatter**.

---

## 1. Il Linter: Il Correttore Ortografico del Codice

Un **linter** analizza il tuo codice *mentre lo scrivi*, alla ricerca di errori, dimenticanze o costrutti sospetti.

* **L'Analogia:** È come la **sottolineatura rossa o gialla di Word**: ti avvisa subito se hai scritto qualcosa di sbagliato prima ancora di eseguire il programma.

### Cosa ti segnala in tempo reale:
* Variabili create ma **mai utilizzate** (che occupano spazio per nulla).
* Nomi di variabili o funzioni scritti male.
* Errori di sintassi evidenti prima del lancio.

---

## 2. Il Formatter: L'Impaginatore Automatico

Un **formatter** prende il tuo codice e lo **riscrive automaticamente** secondo lo standard visivo ufficiale di Python (**PEP 8**).

* **L'Analogia:** È come la funzione *"Giustifica e allinea testo"*: non cambia ciò che hai scritto, ma sistema i margini, l'interlinea e gli spazi per renderlo elegante e ordinato.

### Cosa fa in automatico:
* Aggiunge gli spazi corretti intorno agli operatori (trasforma `totale=prezzo+iva` in `totale = prezzo + iva`).
* Raddrizza l'indentazione e i rientri dei blocchi `if` e `for`.
* Riorganizza le righe vuote e manda a capo le frasi troppo lunghe.

---

## 3. Lo Strumento Moderno: Ruff

Utilizziamo **Ruff**, lo strumento più moderno e veloce al mondo per Python, integrato direttamente dentro Visual Studio Code.

---

## 4. Configurazione in VS Code (Si fa una volta sola!)

### Passo 1: Installare l'estensione
1. Apri la scheda **Estensioni** in VS Code (`Ctrl+Shift+X`).
2. Cerca **"Ruff"** (di *Astral Software*) e clicca su **Installa**.

---

### Passo 2: Attivare la Formattazione Automatica
Vogliamo che ogni volta che premiamo **Salva (`Ctrl+S`)**, VS Code pulisca e formatti il codice all'istante.

1. Premi `F1` (oppure `Ctrl+Shift+P`).
2. Digita `Preferences: Open User Settings (JSON)` e premi Invio.
3. Incolla questo blocco di configurazione:

```json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        }
    }
}
```

---

## 🎯 Il Tuo Flusso di Lavoro da Oggi:
Non dovrai mai più preoccuparti di spazi, indentazioni sballate o importazioni disordinate:
1. **Scrivi la tua logica.**
2. **Premi `Ctrl+S` (Salva).**
3. **Ruff sistema tutto da solo in un millisecondo.**