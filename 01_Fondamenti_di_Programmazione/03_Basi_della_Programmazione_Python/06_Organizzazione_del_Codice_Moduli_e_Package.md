# Organizzazione del Codice: Moduli e Package

Quando un programma cresce, tenere tutto il codice in un unico file diventa confusionario e insostenibile. Per questo motivo, Python ci offre due strumenti per organizzare il codice in modo logico e riutilizzabile: i **moduli** e i **package**.

## 1. Moduli: File di Codice Riutilizzabili

Un **modulo** non è altro che un singolo file Python (`.py`).

**A cosa serve?**
-   **Organizzazione**: Invece di avere un file di 2000 righe, puoi dividere la logica in file più piccoli e tematici. Ad esempio, `calcoli.py` per le funzioni matematiche e `grafica.py` per quelle di disegno.
-   **Riusabilità**: Puoi importare un modulo in altri script per riutilizzarne le funzioni e le classi senza doverle riscrivere.

### Come si usa un modulo?
Si usa l'istruzione **`import`**.

**Esempio Concettuale**:
*   File `matematica.py`:
    ```python
    PI_GRECO: float = 3.14159

    def area_cerchio(raggio: float) -> float:
        return PI_GRECO * (raggio ** 2)
    ```
*   File `main.py` (nella stessa cartella):
    ```python
    import matematica

    area = matematica.area_cerchio(5)
    print(f"L'area è: {area}")
    ```

## 2. Package: Cartelle di Moduli

Un **package** (o pacchetto) è una cartella che contiene più moduli correlati. Permette di creare una struttura gerarchica per progetti molto grandi.

**Come si crea un package?**
Basta creare una cartella e, al suo interno, inserire un file speciale (anche vuoto) chiamato `__init__.py`. Questo file comunica a Python che la cartella non è una cartella qualsiasi, ma un package.

### Struttura di un Package

```
mio_progetto/
├── main.py
└── geometria/              <-- Questo è un package
    ├── __init__.py
    ├── forme_piane.py      <-- Modulo
    └── solidi.py           <-- Modulo
```

### Come si usa un package?
Si usa la "dot notation" (notazione col punto) per accedere ai moduli interni.

**Esempio Concettuale**:
*   File `geometria/forme_piane.py`:
    ```python
    def area_quadrato(lato: float) -> float:
        return lato * lato
    ```
*   File `main.py`:
    ```python
    from geometria.forme_piane import area_quadrato

    area = area_quadrato(4)
    print(f"L'area del quadrato è {area}")
    ```

**In sintesi**:
-   **Modulo**: un file `.py`.
-   **Package**: una cartella di moduli (con `__init__.py`).
-   **Libreria**: un insieme di uno o più package distribuiti insieme per risolvere un problema specifico (es. `requests` o `Flask`).
