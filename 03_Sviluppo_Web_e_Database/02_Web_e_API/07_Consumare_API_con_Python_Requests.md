# Consumare API con Python e la Libreria `requests`

Abbiamo imparato la teoria dietro le API REST. Ora è il momento di passare alla pratica e vedere come un'applicazione (in questo caso, un semplice script Python) può "consumare" un'API per ottenere e inviare dati.

Lo strumento standard per fare questo in Python è la libreria `requests`, che semplifica enormemente l'invio di richieste HTTP.

### 1. Preparazione

Prima di tutto, dobbiamo installare la libreria. Assicurati che il tuo ambiente virtuale sia attivo e poi esegui:

```bash
pip install requests
```

Per i nostri esempi, useremo **JSONPlaceholder**, un'API finta e gratuita perfetta per fare test.

### 2. Esempio 1: Richiesta `GET` per Leggere Dati

Il nostro primo obiettivo è recuperare le informazioni di un utente specifico. L'endpoint per un singolo utente è `https://jsonplaceholder.typicode.com/users/USER_ID`.

**Obiettivo:** Leggere i dati dell'utente con ID = 1.

```python
import requests
import json

# Definiamo l'URL dell'endpoint a cui vogliamo fare la richiesta
user_id = 1
url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

try:
    # 1. Eseguiamo la richiesta GET
    response = requests.get(url)

    # 2. Controlliamo se la richiesta è andata a buon fine (status code 200 OK)
    response.raise_for_status()  # Solleva un'eccezione per status code 4xx o 5xx

    # 3. Estraiamo i dati JSON dalla risposta
    # Il metodo .json() converte automaticamente il corpo della risposta da stringa JSON a dizionario Python
    dati_utente = response.json()

    # 4. Usiamo i dati
    print("--- Dati Utente Ricevuti ---")
    # Usiamo json.dumps per una stampa "bella" (pretty-print) del dizionario
    print(json.dumps(dati_utente, indent=4))

    print("\n--- Informazioni Specifiche ---")
    print(f"Nome: {dati_utente['name']}")
    print(f"Email: {dati_utente['email']}")
    print(f"Città: {dati_utente['address']['city']}")

except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")
```

### 3. Esempio 2: Richiesta `POST` per Creare Dati

Ora proviamo a creare una nuova risorsa. Useremo l'endpoint `https://jsonplaceholder.typicode.com/posts` per creare un nuovo "post".

**Obiettivo:** Creare un nuovo post con un titolo e un corpo del testo.

```python
import requests
import json

# L'URL dell'endpoint per la creazione dei post
url = "https://jsonplaceholder.typicode.com/posts"

# 1. Prepariamo i dati da inviare nel corpo della richiesta.
# Deve essere un dizionario Python che verrà convertito in JSON.
nuovo_post = {
    'title': 'Il Mio Nuovo Post',
    'body': 'Questo è il contenuto del mio primo post creato tramite API!',
    'userId': 1
}

try:
    # 2. Eseguiamo la richiesta POST, passando i dati con il parametro `json`
    response = requests.post(url, json=nuovo_post)

    # 3. Controlliamo lo status code
    # Per una creazione, ci aspettiamo uno status code 201 (Created)
    response.raise_for_status()

    # 4. Analizziamo la risposta del server
    # Di solito, l'API restituisce l'oggetto che abbiamo creato, con l'ID assegnato dal server
    post_creato = response.json()

    print("--- Risposta dal Server ---")
    print(f"Status Code: {response.status_code} (Created!)")
    print(json.dumps(post_creato, indent=4))
    print(f"\nIl nostro post è stato creato con ID: {post_creato['id']}")

except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")
```

Scrivere un client API con `requests` è così semplice. Questa abilità è fondamentale per costruire applicazioni che interagiscono con servizi esterni o per testare le API che costruiremo noi stessi.````