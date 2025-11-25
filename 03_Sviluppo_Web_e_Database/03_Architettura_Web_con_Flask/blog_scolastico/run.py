# Importiamo la funzione create_app dal pacchetto 'app'
# Questo è possibile perché 'app' ha un file __init__.py!
from app import create_app

# Chiamiamo la fabbrica per ottenere l'applicazione
app = create_app()

# Se questo file viene eseguito direttamente (non importato), avvia il server
if __name__ == '__main__':
    app.run(debug=True)