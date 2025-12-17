import hashlib

def associar_arxiu(arxiu):
    usuari = input("Introdueix el teu usuari: ")
    contrasenya_usuari = input("Introdueix la contrasenya: ")
    validat = False
    
    try: 
        with open (arxiu, "r") as f:
            for linea in f: 
                if f"Usuari: {usuari}" in linea and f"contrasenya: {contrasenya_usuari}" in linea:
                    print("TOMATE")
                    validat = True
                break

    except FileNotFoundError:
        print("[ERROR] El fitxer usuaris.txt no existeix. Crea'l primer.")
        return
    
    if not validat:
        print("[ERROR] Usuari o contrasenya incorrectes.")
        return
    
associar_arxiu("usuari.txt")