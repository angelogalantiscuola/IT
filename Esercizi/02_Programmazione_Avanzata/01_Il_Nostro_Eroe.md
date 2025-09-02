# Esercizio 01: Modellare e Implementare il Nemico

**Obiettivo:** Applicare il processo completo "Testo -> UML -> Codice" per creare una nuova classe per il nostro gioco di ruolo.

---

### Parte 1: Dall'Idea al Progetto (Analisi e UML)

**Requisiti:**
Vogliamo creare la classe per i nemici che il nostro eroe dovrà affrontare. La descrizione è la seguente:

> Un `Nemico` deve avere un **`tipo`** (ad esempio, "Goblin", "Drago", "Scheletro"), dei **`punti_vita`** e un **`valore_attacco`**. I `punti_vita` e il `valore_attacco` possono variare per ogni tipo di nemico. La classe deve avere anche un metodo `descrivi()` che stampa un riassunto delle caratteristiche del nemico.

**Tuo Compito:**

1.  Apri un file di testo o usa un editor markdown.
2.  Basandoti sulla descrizione, **disegna il diagramma delle classi UML** per la classe `Nemico`.
    *   Identifica il nome della classe.
    *   Identifica i 3 attributi e i loro tipi di dato (`str` o `int`).
    *   Identifica il metodo e i suoi parametri (se ce ne sono).
    *   Usa la sintassi MermaidJS per creare il diagramma.

---

### Parte 2: Dal Progetto al Codice (Implementazione Python)

**Tuo Compito:**

1.  Crea un nuovo file Python (es. `nemico.py`).
2.  **Traduci il diagramma UML** che hai appena creato in una classe Python `Nemico`.
3.  Implementa il costruttore `__init__` che accetti come parametri il `tipo`, i `punti_vita` e il `valore_attacco` e li assegni come attributi di istanza.
4.  Implementa il metodo `descrivi()`. All'interno, deve stampare una frase come: `"Un [tipo] con [punti_vita] PV e [valore_attacco] ATK."`.

---

### Parte 3: Verifica (Creazione di Oggetti)

**Tuo Compito:**

1.  Nello stesso file Python, dopo la definizione della classe, aggiungi un blocco `if __name__ == "__main__":`.
2.  All'interno di questo blocco, **crea due oggetti (istanze)** della classe `Nemico`:
    *   Un `goblin` con 50 punti vita e 10 di attacco.
    *   Un `drago` con 200 punti vita e 40 di attacco.
3.  Chiama il metodo `descrivi()` su entrambi gli oggetti per verificare che tutto funzioni correttamente.

**Output Atteso:**
```
Un Goblin con 50 PV e 10 ATK.
Un Drago con 200 PV e 40 ATK.
```