# Esercizio 02: L'Eroe Prende Vita - Costruttori, Incapsulamento e Properties

**Obiettivo:** Applicare i concetti di `__init__`, attributi privati e `@property` per rendere più robusta la classe `Nemico` creata nell'esercizio precedente.

---

### Setup Iniziale

Parti dal codice della classe `Nemico` che hai scritto nell'esercizio `01_Il_Nostro_Eroe`. Se non lo hai, usa questo come punto di partenza:

```python
# nemico.py

class Nemico:
    # In questo esercizio, trasformeremo questo in un vero costruttore
    pass

if __name__ == "__main__":
    # Il nostro obiettivo è rendere il codice seguente più robusto e pulito
    goblin = Nemico()
    goblin.tipo = "Goblin"
    goblin.punti_vita = 50
    goblin.valore_attacco = 10
    
    drago = Nemico()
    drago.tipo = "Drago"
    drago.punti_vita = 200
    drago.valore_attacco = 40
    
    print(f"Un {goblin.tipo} con {goblin.punti_vita} PV e {goblin.valore_attacco} ATK.")
    print(f"Un {drago.tipo} con {drago.punti_vita} PV e {drago.valore_attacco} ATK.")

```

---

### Parte 1: Implementare il Costruttore e l'Incapsulamento

**Tuo Compito:**

1.  **Aggiorna il Diagramma UML:** Modifica il diagramma UML della classe `Nemico` che hai creato nell'esercizio precedente. Rendi gli attributi `punti_vita` e `valore_attacco` **privati**. Aggiungi il costruttore `__init__` alla sezione dei metodi.

2.  **Modifica la Classe `Nemico`:**
    *   Implementa il metodo `__init__` che accetti `tipo`, `punti_vita` e `valore_attacco` come parametri.
    *   All'interno del costruttore, assegna questi valori agli attributi di istanza. Rendi `punti_vita` e `valore_attacco` privati usando il doppio underscore (es. `self.__punti_vita`). L'attributo `tipo` può rimanere pubblico.

---

### Parte 2: Aggiungere Accesso Controllato con `@property`

**Tuo Compito:**

1.  **Crea un Getter:** Implementa una `@property` per l'attributo `punti_vita`. Questo permetterà di leggere il valore dall'esterno (es. `nemico.punti_vita`).

2.  **Crea un Setter con Logica:** Implementa un `@punti_vita.setter` per l'attributo `punti_vita`. Questo setter deve contenere la seguente logica di validazione:
    *   Se il nuovo valore è **minore di 0**, i `punti_vita` del nemico devono essere impostati a **0** (un nemico non può avere vita negativa).
    *   Altrimenti, i `punti_vita` vengono impostati al nuovo valore.

3.  Crea una `@property` anche per `valore_attacco`, ma **solo in lettura** (senza definire un setter).

---

### Parte 3: Rendere l'Oggetto Espressivo con `__str__`

**Tuo Compito:**

1.  Implementa il metodo speciale `__str__(self)` nella classe `Nemico`.
2.  Questo metodo deve restituire una stringa formattata che descriva il nemico, simile a quella dell'esercizio precedente. Esempio: `"Nemico: Goblin | PV: 50 | ATK: 10"`.

---

### Parte 4: Verifica Finale

**Tuo Compito:**

1.  Aggiorna il blocco `if __name__ == "__main__":` per usare la nuova sintassi del costruttore.
2.  Crea un `goblin` e un `drago`.
3.  Stampa direttamente gli oggetti `goblin` e `drago` per testare il tuo metodo `__str__`.
4.  Prova a modificare i punti vita del goblin:
    *   Prima assegna un valore valido (es. `goblin.punti_vita = 40`).
    *   Poi assegna un valore non valido (es. `goblin.punti_vita = -20`).
5.  Stampa di nuovo il goblin dopo ogni modifica per verificare che la logica nel setter funzioni correttamente (nel secondo caso, i PV dovrebbero essere 0).
6.  (Opzionale) Prova a modificare il `valore_attacco` del drago. Cosa succede? Perché?

**Codice di Verifica di Esempio:**
```python
if __name__ == "__main__":
    goblin = Nemico(tipo="Goblin", punti_vita=50, valore_attacco=10)
    drago = Nemico(tipo="Drago", punti_vita=200, valore_attacco=40)

    print("--- Nemici Creati ---")
    print(goblin)
    print(drago)

    print("\n--- Simulazione Combattimento ---")
    print(f"Il Goblin subisce 25 danni.")
    goblin.punti_vita -= 25 # Questo chiama il setter!
    print(goblin)

    print(f"\nIl Goblin subisce un colpo critico di 100 danni!")
    goblin.punti_vita -= 100 # Questo dovrebbe portare i PV a 0, non a -65
    print(goblin)
```