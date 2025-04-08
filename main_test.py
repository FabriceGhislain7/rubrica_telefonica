import os
from datetime import datetime
import shutil

contatti = {}

# MENU
path_rubrica = "rubrica_telefonica.txt"
if os.path.exists(path_rubrica):
    pass
else:
    with open(path_rubrica, "w") as file:
        pass

with open(path_rubrica, "r") as file:
    for line in file:
        codice, nome, cognome, numero, mail, data_creazione = line.split(",")
        contatti[codice] = {
            "Nome" : nome,
            "Cognome" : cognome,
            "Numero" : numero,
            "Mail": mail,
            "Data di creazione": data_creazione
            } 

# MENU 
for codice, contatto in contatti:
    print(f"{codice}: {contatto}")