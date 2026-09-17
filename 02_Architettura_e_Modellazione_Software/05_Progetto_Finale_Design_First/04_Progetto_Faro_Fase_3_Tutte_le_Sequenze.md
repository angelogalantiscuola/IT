# Progetto Faro - Fase 3: Modellazione Dinamica (Tutte le Sequenze)

Per garantire la massima chiarezza e non lasciare nulla al caso, disegniamo il **Diagramma di Sequenza per ciascuna delle nostre 4 User Stories**.

Ricordiamo la **Regola Aurea**: ogni freccia che arriva a un oggetto definisce il metodo da scrivere nella classe corrispondente.

---

## 🎬 Sequenza 1: Raccolta Oggetto nell'Inventario (US-01)

Mostra l'interazione tra l'Eroe e il suo Zaino per raccogliere una pozione:

```mermaid
sequenceDiagram
    autonumber
    actor Giocatore as 👤 Giocatore (main)
    participant Eroe as eroe :Personaggio
    participant Zaino as zaino :Inventario
    participant Pozione as pozione :Oggetto

    Giocatore->>Eroe: raccogli_oggetto(pozione)
    activate Eroe
    
    Eroe->>Zaino: aggiungi(pozione)
    activate Zaino
    Note over Zaino: Verifica se len(oggetti) < capacita_slot
    
    Zaino-->>Eroe: True (Aggiunto con successo)
    deactivate Zaino
    
    Eroe-->>Giocatore: "Pozione raccolta nello zaino!"
    deactivate Eroe
```

* **Metodi ricavati:**
  * `Personaggio.raccogli_oggetto(ogg: Oggetto) -> bool`
  * `Inventario.aggiungi(ogg: Oggetto) -> bool`

---

## 🎬 Sequenza 2: Combattimento e Attacco del Guerriero (US-02)

Mostra il flusso del calcolo del danno fisico con polimorfismo:

```mermaid
sequenceDiagram
    autonumber
    actor Giocatore as 👤 Giocatore (main)
    participant Guerriero as conan :Guerriero
    participant Bersaglio as orco :Personaggio

    Giocatore->>Guerriero: attacca(orco)
    activate Guerriero
    Note over Guerriero: Calcola danno = 10 (base) + self.forza
    
    Guerriero->>Bersaglio: subisci_danno(danno_calcolato)
    activate Bersaglio
    Note over Bersaglio: self.punti_vita = max(0, self.punti_vita - danno)
    Bersaglio-->>Guerriero: danno applicato
    deactivate Bersaglio
    
    Guerriero-->>Giocatore: "⚔️ Conan infligge 18 danni a Orco!"
    deactivate Guerriero
```

* **Metodi ricavati:**
  * `Guerriero.attacca(bersaglio: Personaggio) -> str`
  * `Personaggio.subisci_danno(danno: int) -> None`

---

## 🎬 Sequenza 3: Apprendimento e Potenziamento Abilità (US-03)

Mostra la gestione dell'entità di raccordo per le relazioni N:N:

```mermaid
sequenceDiagram
    autonumber
    actor Giocatore as 👤 Giocatore (main)
    participant Legame as legame :AbilitaAppresa

    Giocatore->>Legame: potenzia()
    activate Legame
    Note over Legame: if self.livello_maestria < 5: self.livello_maestria += 1
    Legame-->>Giocatore: maestria aumentata
    deactivate Legame
```

* **Metodi ricavati:**
  * `AbilitaAppresa.potenzia() -> None`

---

## 🎬 Sequenza 4: Salvataggio e Ripristino Partita su JSON (US-04)

Mostra come il gestore di persistenza interagisce con il file system:

```mermaid
sequenceDiagram
    autonumber
    actor Giocatore as 👤 Giocatore (main)
    participant Gestore as gestore_salvataggi
    participant Eroe as eroe :Personaggio
    participant FileSystem as 💾 File 'salvataggio.json'

    Note over Giocatore,FileSystem: --- FASE DI SALVATAGGIO ---
    Giocatore->>Gestore: salva_partita(eroe, "salvataggio.json")
    activate Gestore
    Gestore->>Eroe: estrae dati tramite asdict()
    Eroe-->>Gestore: dizionario dati completo
    Gestore->>FileSystem: json.dump(dati)
    Gestore-->>Giocatore: "Partita salvata con successo!"
    deactivate Gestore

    Note over Giocatore,FileSystem: --- FASE DI CARICAMENTO ---
    Giocatore->>Gestore: carica_partita("salvataggio.json")
    activate Gestore
    Gestore->>FileSystem: json.load()
    FileSystem-->>Gestore: dati dizionario
    Note over Gestore: Ricostruisce Oggetto, Inventario e Guerriero
    Gestore-->>Giocatore: restituisce nuova istanza eroe vivo
    deactivate Gestore
```