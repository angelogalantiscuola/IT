# Diagrammi dei casi d'uso per il documento 5M

Questo documento spiega in modo semplice come descrivere i casi d'uso nel progetto 5M, con esempi in ASCII art.

## 1. Concetti chiave

- Attore: un ruolo esterno che interagisce con il sistema.
- Caso d'uso: una funzionalità o servizio offerto dal sistema.
- `<<include>>`: un caso d'uso obbligatorio riutilizzabile.
- `<<extend>>`: un caso d'uso opzionale o condizionale.
- Generalizzazione tra attori: quando un attore specializzato eredita le azioni di un altro.

## 2. Attori e generalizzazione

Nel progetto 5M spesso abbiamo due attori principali:

- `Visitatore` (utente non autenticato)
- `Utente` (autenticato)

Se l'`Utente` può fare tutto ciò che fa il `Visitatore`, allora in UML si disegna:

```
   Visitatore
       ^
       |
     Utente
```

Significa che `Utente` è una specializzazione di `Visitatore`.

## 3. Casi d'uso essenziali

Esempio di casi d'uso per un ricettario digitale:

- `Registrazione utente`
- `Login`
- `Visualizza elenco ricette`
- `Visualizza dettaglio ricetta`
- `Crea ricetta`
- `Aggiungi ai preferiti`

## 4. Relazioni `include` e `extend`

### Include

`<<include>>` si usa quando un comportamento è sempre eseguito insieme a un altro.

Esempio:

```
(Crea ricetta) .> (Verifica autenticazione) : <<include>>
```

Significa che per creare una ricetta il sistema `deve` sempre verificare l'autenticazione.

### Extend

`<<extend>>` si usa quando un comportamento è opzionale o condizionale.

Esempio:

```
(Aggiungi ai preferiti) .> (Visualizza dettaglio ricetta) : <<extend>>
```

Significa che l'azione di aggiungere ai preferiti `può` avvenire quando si visualizzano i dettagli di una ricetta.
