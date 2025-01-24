# Diagramma delle Classi

```mermaid
classDiagram
    class User {
        +id: Integer
        +username: String
        +password: String
        +__init__(id, username, password)
        +get_by_id(user_id)$
        +get_by_username(username)$
        +save()
        +verify_password(password)
    }

    class Entry {
        +id: Integer
        +name: String
        +message: String
        +__init__(id, name, message)
        +get_all(search)$
        +get_by_id(entry_id)$
        +save()
        +delete()
    }

    class DatabaseConnection {
        +get_db_connection()$
        +init_db()$
    }

    class Auth {
        +login_required(f)
        +register()
        +login()
        +logout()
        +password_reset_request()
        +password_reset(token)
    }

    class FlaskApp {
        +config: Config
        +create_app()
    }

    User --> DatabaseConnection : utilizza
    Entry --> DatabaseConnection : utilizza
    Auth --> User : autentica
    FlaskApp --> Auth : include
    FlaskApp --> User : gestisce
    FlaskApp --> Entry : gestisce
```

## Descrizione del Diagramma

Il diagramma delle classi mostra le principali entità dell'applicazione Flask e le loro relazioni:

- **User**: Gestisce le informazioni degli utenti e l'autenticazione

  - Metodi statici per recuperare utenti
  - Verifica delle password
  - Persistenza dei dati

- **Entry**: Gestisce i messaggi o le entità dell'applicazione

  - CRUD operations
  - Ricerca e filtraggio
  - Persistenza dei dati

- **DatabaseConnection**: Gestisce le connessioni al database MySQL

  - Connessione al database
  - Inizializzazione dello schema

- **Auth**: Gestisce l'autenticazione e l'autorizzazione

  - Decoratori per proteggere le route
  - Gestione login/logout
  - Reset password

- **FlaskApp**: Classe principale dell'applicazione
  - Configurazione
  - Creazione dell'app
  - Gestione delle route
