import hashlib

def associar_arxiu(arxiu):
    # Registrar al usuari un fitxer hash
    usuari = input("Introdueix el teu usuari: ").lower()
    contrasenya_usuari = input("Introdueix la contrasenya: ")
    validat = False

    try: 
        with open(arxiu, "r") as f:
            fitxer = f.readlines()
            for linea in fitxer:
                if f"Usuari:{usuari}" in linea.lower() and f"Contrasenya:{contrasenya_usuari}" in linea:
                    print("[OK] Accedit correctament")
                    registre_fitxer = input("Arrastra l'arxiu que vols registrar: ")
                    with open("Usuaris_fitxers.txt", "a") as fitxers_usu:
                        if "Hash" in linea:
                            ...
                    validat = True
                    break  

        if not validat:
                print("[ERROR] Usuari o contrasenya incorrectes")

    except FileNotFoundError:
        print("[ERROR] El fitxer usuaris.txt no existeix. Crea'l primer.")
        return

associar_arxiu("Usuaris.txt")