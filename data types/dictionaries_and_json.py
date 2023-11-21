import json

# info di una persona
# nome, cognome, eta, sesso
nome = "Pippo"
cognome = "Pippi"
eta = 20
sesso = "M"
nome_classe = "4M"
# dizionario
persona = {"nome": nome, "cognome": cognome, "eta": eta, "sesso": sesso}
# classe
# classe = [persona, persona, persona]
classe = {"nome della classe": nome_classe, "alunni": [persona, persona, persona]}
# classi di tutta la scuola
scuola = [classe, classe, classe]


# json.dumps() -> dizionario -> stringa
# salvare la scuola in un file json
file_json = "scuola.json"
with open(file_json, "w") as f:
    json.dump(scuola, f)
f.close()

# json.loads() -> stringa -> dizionario
# leggere la scuola dal file json
file_json = "scuola.json"
with open(file_json, "r") as f:
    scuola = json.load(f)
f.close()

print(scuola[0])  # prima classe
print(scuola[0]["nome della classe"])  # nome prima classe
print(scuola[0]["alunni"][0])  # primo alunno prima classe
print(scuola[0]["alunni"][0]["nome"])  # nome primo alunno prima classe
