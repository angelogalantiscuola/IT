import os
from flask import Flask

def create_app():
    # 1. Creiamo l'istanza di Flask
    # instance_relative_config=True dice a Flask: 
    # "Cerca la cartella 'instance' fuori da 'app', non dentro."
    app = Flask(__name__, instance_relative_config=True)

    # 2. Configurazione di base
    # Qui impostiamo le variabili fondamentali.
    app.config.from_mapping(
        # SECRET_KEY serve a Flask per firmare i dati sicuri (es. sessioni).
        # 'dev' va bene per sviluppare, ma in produzione andrà cambiata.
        SECRET_KEY='dev',
        # Diciamo a Flask dove salvare il file del database SQLite
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )

    # --- AGGIUNGI QUESTO ---
    from . import db
    db.init_app(app)
    # -----------------------

    # --- REGISTRAZIONE BLUEPRINTS ---
    from . import main
    app.register_blueprint(main.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)
    # --------------------------------

    return app