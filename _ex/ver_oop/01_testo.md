### Esercizio di Verifica: Programmazione Orientata agli Oggetti in Python

#### Obiettivo
Creare una gerarchia di classi che rappresenti diversi tipi di dispositivi elettronici in un sistema di gestione di un negozio di elettronica. Utilizzare l'ereditarietà per definire una classe base `Dispositivo` e classi derivate `Smartphone`, `Laptop` e `Tablet` che ereditano dalla classe base. Implementare metodi specifici per ogni tipo di dispositivo e aggiungere funzionalità avanzate come la gestione delle vendite, la ricerca di dispositivi, il calcolo del costo totale di acquisto e la stampa dell'inventario.

#### Fase 1
1. **Diagramma UML**: Realizza il diagramma delle classi UML utilizzando PlantUML. Il diagramma deve includere le classi `Dispositivo`, `Smartphone`, `Laptop` e `Tablet` con i rispettivi attributi e metodi.
2. **Implementazione**:
    - Definisci una classe base chiamata `Dispositivo` con attributi di istanza `marca`, `modello`, `prezzo` e `disponibile`.
    - Implementa metodi di istanza nella classe `Dispositivo` per accedere e modificare questi attributi.
    - Aggiungi un metodo `vendi` che imposta l'attributo `disponibile` a `False` e un metodo `rifornisci` che lo imposta a `True`.
    - Definisci le classi derivate `Smartphone`, `Laptop` e `Tablet` che ereditano dalla classe `Dispositivo`. 
    - Aggiungi attributi di istanza specifici per ogni classe derivata.

#### Fase 2
1. **Diagramma UML**: Aggiorna il diagramma UML per includere i metodi getter e setter per gli attributi delle classi.
2. **Implementazione**:
    - Implementa metodi getter e setter per gli attributi delle classi `Dispositivo`, `Smartphone`, `Laptop` e `Tablet`.
    - Implementa il polimorfismo creando un metodo `descrizione` nella classe base `Dispositivo` e sovrascrivilo nelle classi derivate per fornire una descrizione specifica di ogni tipo di dispositivo.

#### Fase 3
1. **Diagramma UML**: Aggiorna il diagramma UML per includere attributi e metodi di classe, nonché metodi statici.
2. **Implementazione**:
    - Aggiungi un attributo di classe `numero_dispositivi` nella classe `Dispositivo` che tiene traccia del numero totale di dispositivi creati.
    - Implementa un metodo di classe `conta_dispositivi` che restituisce il valore di `numero_dispositivi`.
    - Aggiungi un metodo statico `calcola_sconto` che calcola uno sconto sul prezzo di un dispositivo dato un valore percentuale.

#### Fase 4
Aggiungere funzionalità avanzate per la gestione dell'inventario in una nuova classe `Inventario`.

1. **Diagramma UML**: Aggiorna il diagramma UML per includere una nuova classe per la gestione dell'inventario.
2. **Implementazione**:
    - Implementa un metodo per cercare dispositivi con prezzo inferiore a un valore specificato.
    - Implementa un metodo per cercare solo dispositivi disponibili.

#### Esempio di Implementazione

```python
# Esempio di utilizzo
# Fase 1
smartphone = Smartphone("Apple", "iPhone 12", 999, 128)
print(smartphone.get_marca())  # Output: Apple
smartphone.vendi()
print(smartphone.disponibile)  # Output: False

# Fase 2
laptop = Laptop("Dell", "XPS 13", 1200, 16)
tablet = Tablet("Samsung", "Galaxy Tab S7", 650, 11)

print(smartphone.descrizione())  # Output: Smartphone Apple iPhone 12 con 128GB di memoria
print(laptop.descrizione())  # Output: Laptop Dell XPS 13 con 16GB di RAM
print(tablet.descrizione())  # Output: Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Fase 3
print(Dispositivo.conta_dispositivi())  # Output: 3
print(Dispositivo.calcola_sconto(1000, 10))  # Output: 900.0

# Fase 4
inventario = Inventario()
inventario.aggiungi_dispositivo(smartphone)
inventario.aggiungi_dispositivo(laptop)
inventario.aggiungi_dispositivo(tablet)

inventario.stampa_inventario()
# Output: 
# Smartphone Apple iPhone 12 con 128GB di memoria
# Laptop Dell XPS 13 con 16GB di RAM
# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Cerca dispositivi per prezzo
dispositivi_economici = inventario.cerca_per_prezzo(1000)
print("Dispositivi con prezzo inferiore a 1000€:")
for dispositivo in dispositivi_economici:
    print(dispositivo.descrizione())
# Output:
# # Dispositivi con prezzo inferiore a 1000€:
# Smartphone Apple iPhone 12 con 128GB di memoria
# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Cerca dispositivi disponibili
dispositivi_disponibili = inventario.cerca_disponibili()
print("Dispositivi disponibili:")
for dispositivo in dispositivi_disponibili:
    print(dispositivo.descrizione())
# Output:
# # Dispositivi disponibili:
# Laptop Dell XPS 13 con 16GB di RAM
# Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici
