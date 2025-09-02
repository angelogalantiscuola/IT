# Mappa Concettuale: Costruzione delle Classi

Questa mappa illustra come trasformare una classe semplice in un componente software robusto, controllando come viene creata, come i suoi dati vengono protetti e come si presenta al mondo esterno.

```mermaid
graph TD
    A[Classe Semplice] --> B(Costruzione e Inizializzazione);
    B --> C(Protezione dei Dati);
    C --> D(Espressività dell'Oggetto);

    subgraph Costruzione
        B --> B1["Costruttore <code>__init__</code>"];
        B1 --> B2["Garantisce uno stato iniziale valido"];
    end

    subgraph Protezione
        C --> C1[Incapsulamento];
        C1 --> C2["Attributi Privati <code>__nome</code>"];
        C2 --> C3["Accesso Controllato con <code>@property</code>"];
        C3 --> C4["Logica di Validazione nel Setter"];
    end

    subgraph Espressività
        D --> D1[Metodi Speciali];
        D1 --> D2["<code>__str__</code>: Rappresentazione per l'utente"];
        D1 --> D3["<code>__repr__</code>: Rappresentazione per lo sviluppatore"];
    end

```