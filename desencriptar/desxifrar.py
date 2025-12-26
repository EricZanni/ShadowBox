
def desxifrar():
    from desencriptar.file_system import llegir_arxiu_xifrat
    from desencriptar.Funcions_desencriptar import afegeix_clau, moure_dreta, invertir_substitució_nums

    # Pas 1: Demanar la clau
    clau_usuari = input("Introdueix la clau de desxifratge: ")
    
    # CORRECCIÓ 1: Convertim la clau de text a números ASCII
    clau_numerica = [ord(c) for c in clau_usuari] 

    # Pas 2: Llegir fitxer
    dades = llegir_arxiu_xifrat("xifratge_secret.txt")
    
    if dades == "":
        print("ERROR: L'arxiu està buit o no existeix.")
        return

    print(f"Dades xifrades inicials: {dades}")

    # Pas 3: El Bucle Invers de 3 rondes
    for ronda in range(3):
        # 1r: Desfem l'XOR de la clau (fent servir la clau numèrica)
        dades = afegeix_clau(dades, clau_numerica)
        
        # 2n: Desfem el moviment (moure a la dreta)
        dades = moure_dreta(dades)
        
        # 3r: Desfem la substitució (S-Box inversa)
        dades = invertir_substitució_nums(dades)
        
        print(f"Estat despres de la ronda {ronda + 1}: {dades}")

    # CORRECCIÓ 2: Convertim els números finals a text llegible
    missatge_desxifrat = ""
    for n in dades:
        missatge_desxifrat += chr(n)

    print("MISSATGE SECRET REVELAT:")
    print(missatge_desxifrat)


desxifrar()