import hashlib
 
def menu_visual_hash():
    print("**************************************")
    print("*                                    *")
    print("*             MENU HASH              *")
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
    print("* - Ha de tenir minim una majúscula  *")
    print("* - Ha de tenir minim una minúscula  *")
    print("* - Ha de tenir minim un número      *")
    print("* - Ha de tenir minim un simbol      *")
    print("* - Minim ha d'haver 8 caracters     *")
    print("*                                    *")
    print("**************************************")

def menu_opcions(resposta):
    #Moure al usuari a l'opcio que escollit
    if resposta == 1:
        usuari, contrasenya = crear_compte()
        hash_usuari = generar_hash_usuari(contrasenya)
        verificacio_usuari(usuari, contrasenya, hash_usuari)
    elif resposta == 2:
        print("Associar arxiu")
    elif resposta == 3:
        print("Verificar arxiu")
    elif resposta == 4:
        sortir_hash()
 
def opcio_usuari():
    #Validacio de la resposta del usuari
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
        
def crear_compte():

    #Generar usuari y contrasenya amb politiques
    abcedari = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbols = "!@#$%^&*()-_=+[];:',.<>/?|~`"

    while True:
        contador_majusculas = 0
        contador_minuscules = 0
        contador_numeros = 0
        contador_simbols = 0

        usuari = input("\nEscriu un nom per l'usuari: ").lower()
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
            return usuari, contrasenya
        else:
            if contador_minuscules < 1:
                print("[ERROR] Et falta una minuscula")
            if contador_majusculas < 1:
                print("[ERROR] Et falta una majuscula")
            if contador_numeros < 1:
                print("[ERROR] Et falta un numero")
            if contador_simbols < 1:
                print("[ERROR] Et falta un simbol")
            if len(contrasenya) < 8:
                print("[ERROR] La contrasenya ha de tenir minim 8 caracters")

def generar_hash_usuari(contrasenya): 
    #Generar hash del user per la contrasenya
    hash_usuari = hashlib.sha256(contrasenya.encode()).hexdigest()          # Fem que contrasenya pasi de str a bytes, fem us del SHA-256 i ho pasem a hexadecimal
    return hash_usuari

def verificacio_usuari(usuari, contrasenya, hash):

    #Donar registre al fitxer Usuaris.txt amb les dades donades
    contador = 0

    try:
        with open("Usuaris.txt", "r") as llegir_fitxer:
            for linea in llegir_fitxer:
                contador += 1
                if f"Usuari:{usuari}" in linea:
                    print("[ERROR] Aquest usuari ja existeix")
                    return                     
    except FileNotFoundError:
        with open("Usuaris.txt", "w") as Creacio_fitxer:
            Creacio_fitxer.write("")
            
    with open("Usuaris.txt", "a") as escriure_fitxer:
        escriure_fitxer.write(f"{contador+1}. Usuari:{usuari} Contrasenya:{contrasenya} Hash:{hash}\n")
        print("[OK] S'ha afegit el usuari nou")
                
def sortir_hash():
    #Sortir del programa
    exit()



 