## Ambiente Virtuale in Python

Un **ambiente virtuale** in Python è un modo per isolare le dipendenze di un progetto dagli altri progetti presenti sul sistema. Questo è utile per evitare conflitti tra versioni di librerie e strumenti usati da differenti progetti.

### Perché usare un ambiente virtuale?
Quando lavori su diversi progetti Python, è possibile che ciascuno utilizzi versioni differenti delle stesse librerie. Senza un ambiente virtuale, potresti ritrovarti a sovrascrivere o a compromettere le dipendenze di un progetto con quelle di un altro. Un ambiente virtuale ti consente di creare uno spazio isolato per installare le dipendenze specifiche del progetto, garantendo che i pacchetti installati non interferiscano tra loro.

### Creare un ambiente virtuale
In Python, puoi creare un ambiente virtuale utilizzando il modulo integrato `venv`. Ecco i passaggi per creare e attivare un ambiente virtuale:

1. **Apri il terminale** (o la shell di comando).
2. Vai alla directory del tuo progetto:
   ```bash
   cd /percorso/del/progetto
   ```
3. Crea un nuovo ambiente virtuale:
   ```bash
   python -m venv nome_ambiente
   ```
   Qui, `nome_ambiente` è il nome della cartella in cui verranno memorizzati i file dell’ambiente virtuale. Puoi scegliere un nome a tua scelta, come `.venv` o `venv`.

4. **Attiva l'ambiente virtuale**:
   - Su Windows:
     ```bash
     nome_ambiente\Scripts\activate
     ```
   - Su macOS/Linux:
     ```bash
     source nome_ambiente/bin/activate
     ```

   Dopo aver attivato l'ambiente virtuale, noterai che il nome dell'ambiente appare a sinistra della linea di comando. Questo indica che stai lavorando all'interno dell'ambiente virtuale.

### Installare librerie nell’ambiente virtuale
Una volta attivato l’ambiente virtuale, puoi installare librerie usando `pip`, lo strumento di gestione dei pacchetti di Python:

```bash
pip install nome_pacchetto
```

Tutte le librerie installate saranno disponibili solo all’interno di quell’ambiente virtuale.

### Installare dipendenze da requirements.txt
Se hai un file `requirements.txt` che elenca tutte le dipendenze del progetto, puoi installarle tutte in una volta utilizzando il seguente comando:

```bash
pip install -r requirements.txt
```

Questo comando leggerà il file `requirements.txt` e installerà tutte le librerie elencate al suo interno.


### Disattivare l’ambiente virtuale
Per uscire dall'ambiente virtuale e tornare al contesto globale del sistema, esegui il comando:

```bash
deactivate
```

### Vantaggi dell’uso degli ambienti virtuali
1. **Isolamento delle dipendenze**: Ogni progetto ha il proprio ambiente virtuale con le sue librerie, prevenendo conflitti tra versioni.
2. **Facile riproduzione**: Puoi condividere il file `requirements.txt` (che elenca le dipendenze del progetto) per consentire ad altri di ricreare lo stesso ambiente virtuale. Per generarlo, esegui:
   ```bash
   pip freeze > requirements.txt
   ```
3. **Pulizia del sistema**: Non è necessario installare pacchetti Python globalmente, riducendo il rischio di conflitti tra librerie.

#### Integrare l'ambiente virtuale con VSCode
In Visual Studio Code, puoi facilmente gestire l'ambiente virtuale per il tuo progetto:

1. Dopo aver creato e attivato l’ambiente virtuale, apri la tua cartella di progetto in VSCode.
2. Vai su **Visualizza > Terminale** per aprire il terminale integrato di VSCode.
3. Una volta attivato l'ambiente, VSCode potrebbe riconoscerlo automaticamente. In caso contrario, seleziona l'interprete Python associato all'ambiente virtuale andando su:
   **CTRL+Shift+P** → Digita "Python: Select Interpreter" → Seleziona l’interprete dell’ambiente virtuale.

Con questi passaggi, sarai in grado di utilizzare e gestire gli ambienti virtuali in modo efficiente all'interno dei tuoi progetti Python.

