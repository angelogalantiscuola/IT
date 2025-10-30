# Differenze tra Linting e Formatting in Python, e Guida a Ruff

## Differenze tra Errori di Linting e Formatting

### Errori di Linting
Problemi di qualità logica e stilistica: potenziali bug, violazioni PEP 8, codice inefficiente. Esempi: import non usati, variabili inutilizzate, confronti errati con `None`, bare except.

### Errori di Formatting
Problemi visivi: spazi, indentazione, lunghezza righe. Non influenzano funzionalità. Esempi: spazi mancanti attorno operatori, righe troppo lunghe.

### Differenze Chiave

| Aspetto       | Linting                              | Formatting                          |
|---------------|--------------------------------------|-------------------------------------|
| Focus         | Qualità logica, potenziali bug      | Aspetto visivo, consistenza         |
| Impatto       | Può causare errori runtime          | Nessun impatto funzionale           |
| Correzione    | Spesso manuale                      | Automatica                          |

## Guida a Ruff

Ruff è uno strumento veloce (Rust) per linting e formatting Python, alternativa a flake8/pylint e black.

### Installazione
```
pip install ruff
```

### Comandi Principali
- **Linting check**: `ruff check <file.py>` (segnala errori senza modificare).
- **Linting fix**: `ruff check --fix <file.py>` (correzioni automatiche).
- **Format check**: `ruff format --check <file.py>` (verifica conformità).
- **Format apply**: `ruff format <file.py>` (applica formatting).
- **Combinato**: `ruff check --fix temp.py && ruff format temp.py`.

### Opzioni
- Configurazione: `pyproject.toml` o `.ruff.toml`.
- Selezione regole: `--select F,E`.
- Esclusioni: `--exclude`.

### Integrazione IDE
Estensioni per VS Code, PyCharm, ecc., per linting/formatting automatici.

### Esempi
- Import non usato: segnalato da `ruff check`.
- Spazi mancanti: corretti da `ruff format`.</content>
<parameter name="filePath">/home/x/repo/2526_3M/differenze_linting_formatting.md