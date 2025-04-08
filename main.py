import os
from datetime import datetime
import shutil

contatti = {}

# MENU
path_rubrica = "rubrica_telefonica.txt"
if os.path.exists(path_rubrica):
    pass
else:
    with open(path_rubrica, "w", encoding='utf-8') as file:
        pass

with open(path_rubrica, "r", encoding='utf-8') as file:
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
while True:
    print("MENU")
    print("1. Visualizza rubrica")
    print("2. Aggiugi un contatto")
    print("3. Modifica un contatto")
    print("4. Elimina un contatto")
    print("5. Cerca rubrica")
    print("6. Backup rubrica")
    print("7. Esci")

    scelta_user = input("Fai una scelta: ").strip()

    if scelta_user == "1":
        if contatti:
            print(f"RUBRICA: \n ")
            print(f"Codice \t Nome  \t Cognome \t Numero  \t Mail  ")
            print(f" {"-"*30} \n")
            for codice, contatto in contatti.items():
                print(f"{codice} \t {contatto["Nome" ]} \t {contatto["Cognome"]} \t{contatto["Numero"]} \t{contatto["Mail"]} ")
        else:
            print("Rubrica vuota")

    elif scelta_user == "2":

        nuovo_nome = input("Inserisci il nome: ").strip().capitalize()
        while len(nuovo_nome) < 3:
            print("Il nome deve essere almeno di 3 caratteri.")
            nuovo_nome = input("Inserisci il nome: ").strip().capitalize()

        nuovo_cognome = input("Inserisci il cognome: ").strip().capitalize()
        while len(nuovo_cognome) < 3:
            print("Il cognome deve essere almeno di 3 caratteri.")
            nuovo_cognome = input("Inserisci il cognome: ").strip().capitalize()

        nuovo_numero = input("Inserisci il numero: ").strip()
        while len(nuovo_numero) != 10 and not nuovo_numero.isdigit():
            print("Il numero deve essere di 10 caratteri.")
            nuovo_numero = input("Inserisci il numero: ").strip()

        nuova_mail = input("Inserisci la mail: ").strip()
        while '@' not in nuova_mail:
            print("La mail deve contenere @.")
            nuovo_numero = input("Inserisci la mail: ").strip()
        
        codice = nuovo_nome[:2].upper() + nuovo_cognome[:2].upper() + nuovo_numero[-4: ]

        if codice in contatti.keys():
            scelta_modifica = input("Contatto esistente. Vuoi sovrascrivere?(s/n): ")
            if scelta_modifica == "s":
                with open(path_rubrica, "w") as file:
                    contatti.values()

        print(codice)
        
        #nuova_data
     



    elif scelta_user == "3":
        print("3")

    elif scelta_user == "4":
        print("4")

    elif scelta_user == "5":
        print("5")

    elif scelta_user == "6":
        print("6")

    elif scelta_user == "7":
        print("7")

    else:
        print("666")





