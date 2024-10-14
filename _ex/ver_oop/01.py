class Dispositivo:
    numero_dispositivi = 0  # attributo di classe

    def __init__(self, marca, modello, prezzo, disponibile=True):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.disponibile = disponibile
        Dispositivo.numero_dispositivi += 1  # incremento attributo di classe
        # numero_dispositivi += 1 # errore

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def vendi(self):
        self.disponibile = False

    def rifornisci(self):
        self.disponibile = True

    @classmethod
    def conta_dispositivi(cls):
        return cls.numero_dispositivi

    @staticmethod
    def calcola_sconto(prezzo, percentuale):
        # return prezzo * (1 - percentuale / 100)
        sconto = prezzo * percentuale / 100
        prezzo_scontato = prezzo - sconto
        return prezzo_scontato


class Smartphone(Dispositivo):
    def __init__(self, marca, modello, prezzo, memoria, disponibile=True):
        super().__init__(marca, modello, prezzo, disponibile)
        self.memoria = memoria

    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self, memoria):
        if memoria < 0:
            raise ValueError("La memoria non può essere negativa")
        self._memoria = memoria

    def descrizione(self):
        return f"Smartphone {self.marca} {self.modello} con {self.memoria}GB di memoria"


class Laptop(Dispositivo):
    def __init__(self, marca, modello, prezzo, ram, disponibile=True):
        super().__init__(marca, modello, prezzo, disponibile)
        self.ram = ram

    def descrizione(self):
        return f"Laptop {self.marca} {self.modello} con {self.ram}GB di RAM"


class Tablet(Dispositivo):
    def __init__(self, marca, modello, prezzo, schermo, disponibile=True):
        super().__init__(marca, modello, prezzo, disponibile)
        self.schermo = schermo

    def descrizione(self):
        return (
            f"Tablet {self.marca} {self.modello} con schermo da {self.schermo} pollici"
        )


class Inventario:
    def __init__(self):
        self.dispositivi = []

    def aggiungi_dispositivo(self, dispositivo: Dispositivo):
        self.dispositivi.append(dispositivo)

    def vendi_dispositivo(self, marca, modello):
        for dispositivo in self.dispositivi:
            if dispositivo.marca == marca and dispositivo.modello == modello:
                dispositivo.vendi()
                return

    def cerca_per_prezzo(self, prezzo_max):
        # return [d for d in self.dispositivi if d.prezzo <= prezzo_max]

        dispositivi_con_prezzo_basso = []
        for dispositivo in self.dispositivi:
            if dispositivo.prezzo <= prezzo_max:
                dispositivi_con_prezzo_basso.append(dispositivo)

        return dispositivi_con_prezzo_basso

    def cerca_disponibili(self):
        return [d for d in self.dispositivi if d.disponibile == True]

    def stampa_inventario(self):
        for dispositivo in self.dispositivi:
            print(dispositivo.descrizione())


# Esempio di utilizzo
# Fase 1
smartphone = Smartphone("Apple", "iPhone 12", 999, 128)
print(smartphone.get_marca())  # Output: Apple
smartphone.vendi()
print(smartphone.disponibile)  # Output: False

# Fase 2
laptop = Laptop("Dell", "XPS 13", 1200, 16)
tablet = Tablet("Samsung", "Galaxy Tab S7", 650, 11)

print(
    smartphone.descrizione()
)  # Output: Smartphone Apple iPhone 12 con 128GB di memoria
print(laptop.descrizione())  # Output: Laptop Dell XPS 13 con 16GB di RAM
print(
    tablet.descrizione()
)  # Output: Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

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
