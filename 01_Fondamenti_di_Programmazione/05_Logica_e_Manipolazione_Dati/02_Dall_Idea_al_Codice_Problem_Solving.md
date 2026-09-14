# Dall'Idea al Codice: Un Metodo Strutturato per il Problem Solving

Sapere la sintassi di `for`, `if`, liste e dizionari equivale a conoscere le singole lettere dell'alfabeto. Risolvere un problema di business reale significa **saper scrivere un intero racconto**.

Questo processo segue 4 passi logici sequenziali che evitano di rimanere bloccati davanti allo schermo vuoto.

---

## Il Problema Guida
> *"Data una lista di studenti con nome, classe e voto, trovare il nome dello studente con il voto più alto e verificare se appartiene alla classe '3A'."*

---

### Passo 1: Capire e Scomporre i Requisiti
Prima di toccare la tastiera, si analizza il testo:
1. Ci serve una collezione di studenti.
2. Ogni studente ha 3 informazioni: `nome`, `classe`, `voto`.
3. Dobbiamo scorrere tutti i record e tenere traccia del migliore trovato fino a quel momento.
4. Una volta trovato il record migliore, dobbiamo verificare una condizione sulla sua classe.

---

### Passo 2: Scegliere le Strutture Dati
Come modelliamo i dati in memoria?
* Per descrivere il **singolo studente**: un **dizionario** `{"nome": str, "classe": str, "voto": float}`.
* Per rappresentare l'**intera classe**: una **lista di dizionari** `list[dict]`.

```python
studenti: list[dict] = [
    {"nome": "Alice", "classe": "3A", "voto": 8.5},
    {"nome": "Bob", "classe": "3B", "voto": 9.2},
    {"nome": "Carla", "classe": "3A", "voto": 7.8},
]
```

---

### Passo 3: Definire il Contratto della Funzione (Lo Scheletro)
Definiamo la firma prima della logica interna:

```python
def trova_miglior_studente(studenti: list[dict]) -> dict | None:
    """
    Individua lo studente con il voto più alto.
    Restituisce il dizionario dello studente o None se la lista è vuota.
    """
    pass
```

---

### Passo 4: Implementazione Pulita e Rispetto dei Dati

```python
def trova_miglior_studente(studenti: list[dict]) -> dict | None:
    # Gestione del caso limite: lista vuota
    if not studenti:
        return None

    migliore = studenti[0]
    for studente in studenti:
        if studente["voto"] > migliore["voto"]:
            migliore = studente

    return migliore


# --- Utilizzo nel programma principale ---
def main():
    classe: list[dict] = [
        {"nome": "Alice", "classe": "3A", "voto": 8.5},
        {"nome": "Bob", "classe": "3B", "voto": 9.2},
        {"nome": "Carla", "classe": "3A", "voto": 7.8},
    ]

    top_student = trova_miglior_studente(classe)

    if top_student:
        print(f"Miglior studente: {top_student['nome']} con voto {top_student['voto']}")
        if top_student["classe"] == "3A":
            print("Appartiene alla classe 3A!")
        else:
            print(f"Appartiene alla classe {top_student['classe']}.")


if __name__ == "__main__":
    main()
```