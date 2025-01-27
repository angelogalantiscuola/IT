### Piano di spiegazione struttura Flask app

1. Struttura base cartelle
2. File principali
3. Ruolo di ogni componente

### Struttura Directory Standard Flask
```
my_flask_app/
├── app/
│   ├── __init__.py          # Inizializzazione Flask app
│   ├── models/              # Definizioni database
│   │   └── __init__.py
│   ├── routes/              # Views e routing
│   │   └── __init__.py
│   ├── static/              # File statici (CSS, JS, immagini)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/           # Template HTML Jinja2
│   │   ├── base.html
│   │   └── pages/
│   └── utils/              # Funzioni di utilità
│       └── __init__.py
├── config.py               # Configurazioni
├── requirements.txt        # Dipendenze
└── run.py                 # Entry point
```

### File Principali

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app
```

```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
```

```python
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
```

```python
class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

### Ruolo Componenti:
- `models/`: Definizioni ORM database
- `routes/`: Logica view e URL routing
- 

static

: File statici (CSS, JS, immagini)
- 

templates

: Template HTML con Jinja2
- `utils/`: Funzioni helper
- `config.py`: Configurazioni app
- `run.py`: Entry point applicazione