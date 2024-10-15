class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome}."

    def descrizione(self):
        return f"Ho {self.eta} anni e vivo a {self.citta}."


# Esempio di utilizzo
persona = Persona("Mario", 30, "Roma")
print(persona.saluta())  # Output: Ciao, mi chiamo Mario.
print(persona.descrizione())  # Output: Ho 30 anni e vivo a Roma.
