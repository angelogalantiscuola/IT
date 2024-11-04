"""
This module defines a `Persona` class that represents a person with a name, age, and city.

Classes:
    Persona: A class to represent a person.

Usage example:
    persona = Persona("Mario", 30, "Roma")
    print(persona.saluta())  # Output: Ciao, mi chiamo Mario.
    print(persona.descrizione())  # Output: Ho 30 anni e vivo a Roma.
"""

import os


class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta

    def saluta(self):
        """
        Greet with a message that includes the name of the person.

        Returns:
            str: A greeting message with the person's name.
        """
        return f"Ciao, mi chiamo {self.nome}."

    def descrizione(self):
        """
        Describe the person with age and city.

        Returns:
            str: A description of the person with age and city.
        """
        return f"Ho {self.eta} anni e vivo a {self.citta}."


if __name__ == "__main__":
    # Esempio di utilizzo
    persona = Persona("Mario", 30, "Roma")
    print("Executing file:", os.path.basename(__file__))
    print(persona.saluta())  # Output: Ciao, mi chiamo Mario.
    print(persona.descrizione())  # Output: Ho 30 anni e vivo a Roma.
