# Lezione 2: Accesso Controllato con le Properties

Abbiamo incapsulato i nostri dati, ma ora come facciamo a leggerli o a modificarli in modo sicuro? La risposta in Python è elegante e potente: le **properties**.

## 1. Getter e Setter: L'Approccio Tradizionale

In molti linguaggi, per accedere a un attributo privato `__punti_vita` si creano due metodi:
*   `get_punti_vita()`: per leggere il valore.
*   `set_punti_vita(valore)`: per modificare il valore, aggiungendo della logica di controllo.

Questo funziona, ma in Python c'è un modo migliore.

## 2. Le `@property`: L'Approccio "Pythonic"

Python ci permette di creare metodi `getter` e `setter` che si comportano come se fossero dei semplici attributi. Questo si ottiene con i **decoratori** `@property` e `@*.setter`.

Vediamo come applicarlo al nostro `Personaggio`:

```python
class Personaggio:
    def __init__(self, nome: str, livello: int):
        self.nome = nome
        self.__punti_vita = 100
        self.__livello = livello

    # GETTER: Questo metodo viene eseguito quando leggiamo 'eroe.punti_vita'
    @property
    def punti_vita(self) -> int:
        print("(Accesso in lettura ai punti vita)")
        return self.__punti_vita

    # SETTER: Questo metodo viene eseguito quando scriviamo 'eroe.punti_vita = valore'
    @punti_vita.setter
    def punti_vita(self, nuovo_valore: int) -> None:
        print("(Tentativo di modifica dei punti vita)")
        if nuovo_valore < 0:
            self.__punti_vita = 0 # Logica di validazione!
            print("I punti vita non possono essere negativi. Impostati a 0.")
        else:
            self.__punti_vita = nuovo_valore

    # Property in sola lettura per il livello (non ha un setter)
    @property
    def livello(self) -> int:
        return self.__livello

# --- Esempio di utilizzo ---
eroe = Personaggio("Gandalf", 20)

# 1. Lettura tramite il GETTER (@property)
print(f"PV iniziali: {eroe.punti_vita}")

# 2. Scrittura tramite il SETTER (@punti_vita.setter)
eroe.punti_vita = 50
print(f"PV dopo attacco: {eroe.punti_vita}")

# 3. Tentativo di assegnare un valore non valido
eroe.punti_vita = -30
print(f"PV dopo colpo quasi mortale: {eroe.punti_vita}")

# 4. Tentativo di modificare un attributo in sola lettura
# eroe.livello = 21 # Questo causerebbe un AttributeError!
```

### Vantaggi delle Properties:
1.  **Sintassi Pulita:** L'utente della classe accede a `eroe.punti_vita` come se fosse un attributo normale, senza dover chiamare `get...()` o `set...()`.
2.  **Controllo Totale:** Lo sviluppatore della classe mantiene il controllo totale su cosa succede quando un attributo viene letto o modificato.
3.  **Flessibilità:** Puoi iniziare con un attributo pubblico e, se in futuro avrai bisogno di aggiungere logica, puoi trasformarlo in una property senza dover cambiare tutto il codice che lo utilizzava.