import hashlib
import pwinput
import os
from datetime import datetime

def menu_visual_hash():
    print("**************************************")
    print("*                                    *")
    print("*             MENU HASH              *")
    print("*                                    *")
    print("**************************************")
    print("*                                    *")
    print("*       1.Crear compte hash          *")
    print("*   2.Associar arxiu al meu compte   *")
    print("*    3.Verificar arxiu modificat     *")
    print("*      4.Historial de registres      *")
    print("*             5.Sortir               *")
    print("*                                    *")
    print("**************************************")

def normes_contrasenya():
    print("**************************************")
    print("*                                    *")
    print("*      NORMES DE LA CONTRASENYA      *")
    print("*                                    *")
    print("**************************************")
    print("*                                    *")
    print("* - Ha de tenir minim una majúscula  *")
    print("* - Ha de tenir minim una minúscula  *")
    print("* - Ha de tenir minim un número      *")
    print("* - Ha de tenir minim un simbol      *")
    print("* - Minim ha d'haver 8 caracters     *")
    print("*                                    *")
    print("**************************************")

def missatge_administrador():
    print("**************************************")
    print("*                                    *")
    print("*      HISTORIAL DELS REGISTRES      *")
    print("*       panel d'administració        *")
    print("*                                    *")
    print("**************************************")
    print("*                                    *")
    print("*         1.Iniciar Sessió           *")
    print("*             2.Sortir               *")
    print("*                                    *")
    print("**************************************")

def crear_compte():

    #Generar usuari y contrasenya amb politiques
    abcedari = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbols = "!@#$%^&*()-_=+[];:',.<>/?|~`"
    
    while True:
        contador_majuscules = 0
        contador_minuscules = 0
        contador_numeros = 0
        contador_simbols = 0

        usuari = input("\nEscriu un nom per l'usuari: ").lower()
        if usuari == "":
            print("[ERROR] El nom no pot estar buit")
            continue

        normes_contrasenya()
        contrasenya = pwinput.pwinput("\nEscriu una contrasenya per l'usuari: ", mask="*")

        for caracter in contrasenya:
            if caracter in abcedari:
                contador_minuscules += 1
            elif caracter in abcedari.upper():
                contador_majuscules += 1
            elif caracter in numeros:
                contador_numeros += 1
            elif caracter in simbols:
                contador_simbols += 1

        if contador_minuscules >= 1 and contador_majuscules >= 1 and contador_numeros >= 1 and contador_simbols >= 1 and len(contrasenya) >= 8:
            print("[OK] Usuari registrat correctament")
            return usuari, contrasenya
        else:
            if contador_minuscules < 1:
                print("[ERROR] Et falta una minuscula")
            if contador_majuscules < 1:
                print("[ERROR] Et falta una majuscula")
            if contador_numeros < 1:
                print("[ERROR] Et falta un numero")
            if contador_simbols < 1:
                print("[ERROR] Et falta un simbol")
            if len(contrasenya) < 8:
                print("[ERROR] La contrasenya ha de tenir minim 8 caracters")

def contrasenya_hash(contrasenya): 
    #Generar hash de la contrasenya del usuari
    hash_usuari = hashlib.sha256(contrasenya.encode()).hexdigest()          # Fem que contrasenya pasi de str a bytes, fem us del SHA-256 i ho pasem a hexadecimal
    return hash_usuari

def verificacio_usuari(usuari, contrasenya, hash):

    #Donar registre al fitxer Usuaris.txt amb les dades donades
    contador = 0

    try:
        with open("Usuaris.txt", "r") as llegir_fitxer:
            for linea in llegir_fitxer:
                contador += 1
                if f"usuari:{usuari}" in linea:
                    print("[ERROR] Aquest usuari ja existeix")
                    return                     
    except FileNotFoundError:
        with open("Usuaris.txt", "w") as Creacio_fitxer:
            Creacio_fitxer.write("")

    with open("Usuaris.txt", "a") as escriure_fitxer:
        escriure_fitxer.write(f"{contador+1}. usuari:{usuari} contrasenya:{contrasenya} Hash:{hash}\n")
        print("[OK] S'ha afegit el usuari nou")

def sortir_hash():
    #Sortir del programa
    exit()

def hash_fitxer(fitxer):
    #Verificacio de la existencia de l'arxiu
    if not os.path.isfile(fitxer):
        print("[ERROR] L'arxiu no existeix o no s'ha trobat")
        return None
    with open(fitxer, "rb") as f:
        fitxer_hasheat =  hashlib.sha256(f.read()).hexdigest()
        return fitxer_hasheat

def validar_usuari(fitxer):
    # Funcio per validar el usuari
    missatge_no_valid = "[ERROR] Usuari o contrasenya incorrectes"

    usuari = input("Introdueix el teu usuari: ").lower()
    contrasenya = pwinput.pwinput("Introdueix la contrasenya: ", mask="*")
    hash_input = contrasenya_hash(contrasenya)

    try:
        with open(fitxer, "r") as f:
            for linia in f:
                if f"usuari:{usuari}" in linia:
                    hash_guardat = linia.split("Hash:")[1].strip()
                    if hash_input == hash_guardat:
                        print("[OK] Accedit correctament")
                        return usuari
                    else:
                        print(missatge_no_valid)
                        return

            print(missatge_no_valid)
            return

    except FileNotFoundError:
        print("[ERROR] El fitxer Usuaris.txt no existeix.")
        return

def associar_arxiu(arxiu):
    # Funcio per registrar hash d'arxiu a nom d'un usuari
    usuari = validar_usuari(arxiu)
    if not usuari: #* Fet amb AI
        return     #*

    registre_fitxer = input("Escriu la ruta de l'arxiu que vols registrar: ")
    fitxer_hasheat = hash_fitxer(registre_fitxer)
    data = datetime.now()
    print_data = f"{data.day}-{data.month}-{data.year} {data.hour}:{data.minute}:{data.second}"

    if not fitxer_hasheat:
        print("[ERROR] El fitxer no s'ha pogut registrar")
        return

    try:
        with open("Usuaris_fitxers.txt", "a") as fitxers_usuari:
            fitxers_usuari.write(f"usuari:{usuari} fitxer:{fitxer_hasheat} data:{print_data}\n")
        
        print("[OK] S'ha registrat correctament.")

    except FileNotFoundError:
        with open("Usuaris_fitxers.txt", "w") as f:
            f.write(f"usuari:{usuari} fitxer:{fitxer_hasheat}\n")

        print("[OK] S'ha creat i registrat correctament.")
                        
def verificar_arxius(arxiu_usuaris, arxiu_registres):
    # Funcio per comparar hash origianal amb el hash del fitxer actual del usuari
    trobat = False      # Per forçar despres
    usuari = validar_usuari(arxiu_usuaris)
    if not usuari: #* Fet amb AI
        return     #*

    verificar_fitxer = input("Escriu la ruta de l'arxiu que vols verificar")
    fitxer_hasheat = hash_fitxer(verificar_fitxer)

    if not fitxer_hasheat:
        print("[ERROR] El fitxer no s'ha pogut registrar")
        return
    
    try:
        with open(arxiu_registres, "r") as registres:
            registres = registres.readlines()
            for linia in registres:
                if f"usuari:{usuari}" in linia and fitxer_hasheat in linia:
                    print("[OK] L'arxiu es correcte, no hi ha hagut, cap modificacio")
                    trobat = True
                    break

            if not trobat:
                print("[URGENCIA] L'arxiu que has passat ha sigut modificat o no esta registrat")

    except FileNotFoundError:
        print(f"[ERROR] El fitxer {arxiu_registres} no existeix.")

def validar_administrador(fitxer):
    # Validar on verificar que el administrador estigui registrat en el fitxer  
    missatge_no_valid = "[ERROR] L'administrador o contrasenya es incorrecte"

    usuari = input("Introdueix el teu usuari administrador: ").lower()
    contrasenya = pwinput.pwinput("Introdueix la contrasenya: ", mask="*")
    hash_input = contrasenya_hash(contrasenya)
    validat = False

    try:
        with open(fitxer, "r") as f:
            for linia in f:
                if f"usuari:{usuari}" in linia:
                    hash_guardat = linia.split("Hash:")[1].strip()
                    if hash_input == hash_guardat:
                        print("[OK] Accedit correctament")
                        validat = True
                        return validat
                    else:
                        print(missatge_no_valid)
                        return validat

            print(missatge_no_valid)
            return validat

    except FileNotFoundError:
        print("[ERROR] El fitxer Administradors.txt no existeix.")
        return validat

def historial_registres(fitxer):
    # Printeara el historial de registres
    with open(fitxer, "r") as f:
        fitxer_llegit =f.read()
        print(fitxer_llegit)

def menu_opcions_administrador(resposta):
    # Opcio escollida per el administrador
    funciona = True
    if resposta == 1:
        validat = validar_administrador("Administradors.txt")
        if validat == True:
            historial_registres("Usuaris_fitxers.txt")
            return funciona
        else:
            funciona = False
            return funciona
        
    elif resposta == 2:
        opcio_usuari()
        return

def opcion_administrador():
    # Misssatge per escollir la opcio al administrador
    missatge_administrador()
    opcions_valides = [1,2]
    while True:
        try:
            resposta = int(input("\nESCULL L'OPCIO QUE VOLS: "))
            if resposta in opcions_valides:
                menu_opcions_administrador(resposta)
                break
            else:
                print("\n[ERROR] Has d'escullir una opcion entre el 1-2\n")
                menu_visual_hash()
        except ValueError:
            print("\n[ERROR] El valor afegit no es correcte ha de ser entre el 1-2")

def menu_opcions(resposta):
    # Moure al usuari a l'opcio que escollit
    if resposta == 1:
        usuari, contrasenya = crear_compte()
        hash_usuari = contrasenya_hash(contrasenya)
        verificacio_usuari(usuari, contrasenya, hash_usuari)
    elif resposta == 2:
        associar_arxiu("Usuaris.txt")
    elif resposta == 3:
        verificar_arxius("Usuaris.txt", "Usuaris_fitxers.txt")
    elif resposta == 4:
        opcion_administrador()
    elif resposta == 5:
        sortir_hash()

def opcio_usuari():
    # Validacio de la resposta del usuari
    menu_visual_hash()
    opcions_valides = [1,2,3,4,5]
    while True:
        try:
            resposta = int(input("\nESCULL L'OPCIO QUE VOLS: "))
            if resposta in opcions_valides:
                menu_opcions(resposta)
                break
            else:
                print("\n[ERROR] Has d'escullir una opcion entre el 1-5\n")
                menu_visual_hash()
        except ValueError:
            print("\n[ERROR] El valor afegit no es correcte ha de ser entre el 1-5")
