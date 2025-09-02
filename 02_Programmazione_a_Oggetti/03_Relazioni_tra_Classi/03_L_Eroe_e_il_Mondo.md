# Esercizio 03: L'Eroe e il Mondo - Ereditarietà e Composizione

**Obiettivo:** Mettere in pratica i concetti di ereditarietà, polimorfismo e composizione per espandere il nostro progetto RPG, partendo sempre dalla progettazione UML.

---

### Parte 1: Ereditarietà e Specializzazione (Relazione "IS-A")

**Requisiti:**
Vogliamo specializzare i nostri personaggi. Oltre al `Personaggio` generico, avremo:
> Un **`Guerriero`** è un `Personaggio` che ha anche un attributo `forza`. Il suo attacco deve essere più potente.
> Un **`Mago`** è un `Personaggio` che ha anche un attributo `mana`. Può attaccare solo se ha abbastanza mana.

**Tuo Compito:**

1.  **Disegna il Diagramma UML:**
    *   Crea un diagramma che mostri la classe base `Personaggio` e le due classi derivate `Guerriero` e `Mago`.
    *   Usa la freccia di generalizzazione per indicare l'ereditarietà.
    *   Aggiungi gli attributi specifici a ciascuna sottoclasse.
    *   Assicurati che il metodo `attacca` sia presente in tutte e tre le classi (per indicare che verrà fatto l'override).

2.  **Implementa il Codice Python:**
    *   Parti dalla classe `Personaggio` che hai già.
    *   Crea la classe `Guerriero` che eredita da `Personaggio`.
        *   Nel `__init__`, chiama `super().__init__()` e aggiungi l'attributo `forza`.
        *   Fai l'**override** del metodo `attacca` in modo che stampi un messaggio che menzioni la sua forza.
    *   Crea la classe `Mago` che eredita da `Personaggio`.
        *   Nel `__init__`, chiama `super().__init__()` e aggiungi l'attributo `mana`.
        *   Fai l'**override** del metodo `attacca` in modo che controlli se il `mana` è sufficiente (>10). Se lo è, esegue l'attacco e riduce il mana. Altrimenti, stampa un messaggio che indica mana insufficiente.

3.  **Verifica il Polimorfismo:**
    *   Nel blocco `if __name__ == "__main__":`, crea una lista contenente un'istanza di `Guerriero` e un'istanza di `Mago`.
    *   Crea un `Nemico` generico.
    *   Scrivi un ciclo `for` che itera sulla lista e chiama il metodo `attacca()` su ogni personaggio. Osserva come ogni oggetto risponde in modo diverso alla stessa chiamata.

---

### Parte 2: Composizione (Relazione "HAS-A")

**Requisiti:**
> Un `Personaggio` deve poter portare con sé degli oggetti. Creeremo quindi un `Inventario`. L'`Inventario` contiene una lista di `Oggetti`. Un `Oggetto` ha semplicemente un `nome`.

**Tuo Compito:**

1.  **Disegna il Diagramma UML:**
    *   Disegna le tre classi: `Personaggio`, `Inventario`, `Oggetto`.
    *   Collega `Personaggio` e `Inventario` con una relazione di **composizione** (rombo pieno).
    *   Collega `Inventario` e `Oggetto` con una relazione di **aggregazione** (rombo vuoto), indicando che un inventario può contenere `*` (molti) oggetti.

2.  **Implementa il Codice Python:**
    *   Crea una classe semplice `Oggetto` con un `__init__` che accetti solo il `nome`.
    *   Crea la classe `Inventario`.
        *   Nel `__init__`, inizializza un attributo `oggetti` come una lista vuota.
        *   Crea un metodo `aggiungi(oggetto)` per aggiungere un `Oggetto` alla lista.
        *   Crea un metodo `mostra()` che stampi il contenuto dell'inventario.
    *   Modifica la classe `Personaggio`:
        *   Nel `__init__`, crea un nuovo attributo `inventario` e assegnagli un'istanza della classe `Inventario()`.

3.  **Verifica la Composizione:**
    *   Nel blocco `if __name__ == "__main__":`, crea un `Personaggio`.
    *   Crea alcuni `Oggetti` (es. `spada`, `pozione`).
    *   Usa il `Personaggio` per accedere al suo inventario e aggiungere gli oggetti. Esempio: `eroe.inventario.aggiungi(spada)`.
    *   Alla fine, chiama il metodo per mostrare l'inventario dell'eroe.