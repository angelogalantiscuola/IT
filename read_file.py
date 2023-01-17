# LEGGERE UN FILE RIGA PER RIGA

import os
file_path = './voti_alunni.txt'

# controlla se il file esiste
if os.path.exists(file_path):
    # se esiste aprilo in lettura
    f = open(file_path, "r")

    while True:
        # leggi una riga alla volta
        line  = f.readline()
        if line == "":
            break
        # *non abbiamo ancora visto le liste
        nome = line.split(" ")[0] 
        voto = line.split(" ")[1]
        print(f'alunno {nome} ha preso {voto}')
    f.close()
else:
  print("Il file non esiste")
