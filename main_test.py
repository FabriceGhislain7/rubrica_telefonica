import os
from datetime import datetime
import shutil

contatti = {}

# MENU
path_libro = "libro.txt"
if os.path.exists(path_libro):
    pass
else:
    with open(path_libro, "w") as file:
        pass

with open(path_libro, "r") as file:
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
for codice, contatto in contatti.items():
    file.write(f"{codice}, {contatto["Nome" ]}, {contatto["Cognome"]}, {contatto["Numero"]}, {contatto["Mail"]}, {data_creazione}\n")
