# Esercizio 07: Testiamo il nostro Eroe

**Obiettivo:** Scrivere una suite di test completa per la classe `Personaggio` utilizzando `pytest`, applicando i principi del testing a oggetti.

---

### Setup Iniziale

Assicurati di avere la tua classe `Personaggio` (e le sue sottoclassi `Guerriero` e `Mago`) in una cartella `src/`. Crea una cartella `tests/` con un file `test_personaggio.py`.

La tua classe `Personaggio` dovrebbe avere almeno:
*   Un `__init__` che imposta `nome` e `punti_vita`.
*   Una `@property` per leggere `punti_vita`.
*   Un `@punti_vita.setter` che impedisce ai PV di scendere sotto 0.
*   Un metodo `is_sconfitto()` che restituisce `True` se i PV sono 0.
*   Un metodo `subisci_danno(danno)`.

---

### Tuo Compito

Scrivi i seguenti test nel file `test_personaggio.py`.

#### 1. Test del Costruttore
*   Scrivi una funzione `test_creazione_personaggio()` che crei un `Personaggio` e verifichi con degli `assert` che i suoi attributi iniziali (nome, punti_vita, livello) siano impostati correttamente.

#### 2. Test del Danno e dello Stato
*   Scrivi una funzione `test_danno_normale()`:
    *   Crea un personaggio.
    *   Chiama `subisci_danno(30)`.
    *   Verifica che i `punti_vita` siano scesi a 70.
    *   Verifica che `is_sconfitto()` restituisca `False`.

*   Scrivi una funzione `test_danno_eccessivo_e_sconfitta()`:
    *   Crea un personaggio.
    *   Chiama `subisci_danno(150)`.
    *   Verifica che i `punti_vita` siano esattamente `0` (grazie alla logica del setter).
    *   Verifica che `is_sconfitto()` restituisca `True`.

#### 3. (Bonus) Test dell'Ereditarietà e Polimorfismo
*   Scrivi una funzione `test_creazione_guerriero()`:
    *   Crea un `Guerriero` e verifica che i suoi attributi base (ereditati) e quelli specifici (`forza`) siano corretti.

*   Scrivi una funzione `test_attacco_polimorfico()`:
    *   Questo test è più concettuale. Come potresti verificare che il metodo `attacca` di un `Mago` consumi effettivamente `mana`, mentre quello di un `Guerriero` no?
    *   *Suggerimento:* Crea un `Mago`, controlla il suo `mana` iniziale, chiama `attacca()`, e poi controlla di nuovo il `mana` per vedere se è diminuito.

---

### Esecuzione
Una volta scritti i test, esegui `pytest` dalla cartella principale del tuo progetto e assicurati che tutti i test passino. Se qualcuno fallisce, fai debug sul codice delle tue classi fino a quando la suite di test non sarà completamente "verde".