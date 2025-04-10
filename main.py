import os
from datetime import datetime
import shutil

contatti = {}

# Creazione della rubrica telefonica
path_rubrica = "rubrica_telefonica.txt"
if os.path.exists(path_rubrica):
    pass
else:
    with open(path_rubrica, "w", encoding='utf-8') as file:
        pass

# Lettura della rubica telefonnica
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

    # Gestione della scelta dell'utente
    if scelta_user == "1":
        if contatti:
            print(f"RUBRICA: \n ")
            print(f"Codice \t Nome  \t Cognome \t Numero  \t Mail  ")
            print(f" {"-"*30} \n")
            for codice, contatto in contatti.items():
                print(f"{codice} \t {contatto['Nome']} \t {contatto['Cognome']} \t{contatto['Numero']} \t{contatto['Mail']} ")
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
            nuova_mail = input("Inserisci la mail: ").strip()
        
        nuovo_codice = nuovo_nome[:2].upper() + nuovo_cognome[:2].upper() + nuovo_numero[-4: ]

        # Gestione della creazione o della sovrascrittura del contatto.
        print(contatti.keys())
        if nuovo_codice in contatti:
            scelta_modifica = input("Contatto esistente. Vuoi sovrascrivere?(s/n): ").strip().lower()
            if scelta_modifica != "s":
                print('no modifica')
                continue

        data_creazione = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        contatti[nuovo_codice] = {
            "Nome" : nuovo_nome,
            "Cognome" : nuovo_cognome,
            "Numero" : nuovo_numero,
            "Mail": nuova_mail,
            "Data di creazione": data_creazione
            } 
        # print(codice)

        with open(path_rubrica, "w") as file:
            # file.write(f"codice, nome, cognome, numero, mail, data_creazione\n")
            for codice, contatto in contatti.items():
                file.write(f"{codice}, {contatto['Nome']}, {contatto['Cognome']}, {contatto['Numero']}, {contatto['Mail']}, {data_creazione}")

    elif scelta_user == "3":
        codice_modifica = input("Inserisci il codice modifica: ").strip().upper()
        if codice_modifica not in contatti.keys():
            print("Nessuno contatto esistente con questo codice.")
            continue
        else:
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

            nuovo_mail = input("Inserisci la mail: ").strip()
            while '@' not in nuovo_mail:
                print("La mail deve contenere @.")
                nuovo_mail = input("Inserisci la mail: ").strip()
            
            nuovo_codice = nuovo_nome[:2].upper() + nuovo_cognome[:2].upper() + nuovo_numero[-4: ]
            cambio_codice = input(f"Cambiare il vecchio codice {codice_modifica} in {nuovo_codice}? (s/n) ")
            if cambio_codice == "s":
                codice = nuovo_codice
            else:
                codice = codice_modifica

            data_creazione = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            contatti[codice] = {
                "Nome" : nuovo_nome,
                "Cognome" : nuovo_cognome,
                "Numero" : nuovo_numero,
                "Mail": nuovo_mail,
                "Data di creazione": data_creazione
                }   

            with open(path_rubrica, "w") as file:
                for codice, contatto in contatti.items():
                    file.write(f"{codice}, {contatto['Nome']}, {contatto['Cognome']}, {contatto['Numero']}, {contatto['Mail']}, {data_creazione}")

        # DA fare: quando modifica s: contatto.pop()

    elif scelta_user == "4":
        codice_elimina = input("Inserisci il codice da eliminare: ").strip().upper()
        if codice_elimina not in contatti.keys():
            print("Nessuno contatto esistente con questo codice.")
            continue
        else:
            print(f"contatto con codice {codice_elimina} e nome {contatti[codice_elimina]["Nome"]} eliminato")
            contatti.pop(codice_elimina)

            with open(path_rubrica, "w") as file:
                for codice, contatto in contatti.items():
                    file.write(f"{codice}, {contatto['Nome']}, {contatto['Cognome']}, {contatto['Numero']}, {contatto['Mail']}, {data_creazione}")

    elif scelta_user == "5":
        print("5")

    elif scelta_user == "6":
        print("6")

    elif scelta_user == "7":
        print("7")

    else:
        print("666")