import hashlib
 
def menu_visual_hash():
    print("**************************************")
    print("*                                    *")
    print("*            MENU HASH               *")
    print("*                                    *")
    print("**************************************")
    print("*                                    *")
    print("*      1. Crear compte hash          *")
    print("*                                    *")
    print("*  2. Associar arxiu al meu compte   *")
    print("*                                    *")
    print("*    3. Verificar arxiu modificat    *")
    print("*                                    *")
    print("*            4. Sortir               *")
    print("*                                    *")
    print("**************************************")
 
def normes_contrasenya():
    print("**************************************")
    print("*                                    *")
    print("*       NORMES DE LA CONTRASENYA     *")
    print("*                                    *")
    print("**************************************")
    print("*                                    *")
    print("* - Ha de tenir mínim una majúscula  *")
    print("* - Ha de tenir mínim una minúscula  *")
    print("* - Ha de tenir mínim un número      *")
    print("* - Ha de tenir mínim un símbol      *")
    print("* - Mínim ha d'haver 8 caràcters     *")
    print("*                                    *")
    print("**************************************")
 
def menu_opcions(resposta):
    if resposta == 1:
        crear_compte_hash()
    elif resposta == 2:
        print("Associar arxiu")
    elif resposta == 3:
        print("Verificar arxiu")
    elif resposta == 4:
        sortir_hash()
 
def opcio_usuari():
    opcions_valides = [1,2,3,4]
 
    try:
        while True:
            usuari = int(input("\nESCULL L'OPCIO QUE VOLS: "))
            if usuari in opcions_valides:
                menu_opcions(usuari)
                break
            else:
                print("\n[ERROR] Has d'escullir una opcion entre el 1-4\n")
                menu_visual_hash()
                continue
    except ValueError:
        print("\n[ERROR] El valor afegit no es correcte ha de ser entre el 1-4 \n")
        
def crear_compte_hash():

    abcedari = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbols = "!@#$%^&*()-_=+[];:',.<>/?|~`"

    while True:
        contador_majusculas = 0
        contador_minuscules = 0
        contador_numeros = 0
        contador_simbols = 0

        usuari = input("\nEscriu un nom per l'usuari: ")
        if usuari == "":
            print("[ERROR] El nom no pot estar buit")
            continue

        normes_contrasenya()
        contrasenya = input("\nEscriu una contrasenya per l'usuari: ")

        for caracter in contrasenya:
            if caracter in abcedari:
                contador_minuscules += 1
            elif caracter in abcedari.upper():
                contador_majusculas += 1
            elif caracter in numeros:
                contador_numeros += 1
            elif caracter in simbols:
                contador_simbols += 1

        if contador_minuscules >= 1 and contador_majusculas >= 1 and contador_numeros >= 1 and contador_simbols >= 1 and len(contrasenya) >= 8:
            print("[OK] Usuari registrat correctament")
            break
        else:
            if contador_minuscules < 1:
                print("[ERROR] Et falta una minúscula")
            elif contador_majusculas < 1:
                print("[ERROR] Et falta una majúscula")
            elif contador_numeros < 1:
                print("[ERROR] Et falta un número")
            elif contador_simbols < 1:
                print("[ERROR] Et falta un símbol")
            elif len(contrasenya) < 8:
                print("[ERROR] La contrasenya ha de tenir mínim 8 caràcters")

def sortir_hash():
    exit()
 
menu_visual_hash()
opcio_usuari()
 