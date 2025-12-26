from file_system import llegir_arxiu_xifrat
from Funcions_desencriptar import afegeix_clau, moure_dreta, invertir_substitució_nums


def desxifrar():
 
    # Pas 1: Demanar la clau 
    clau_usuari = input("Introdueix la clau de desxifratge: ")

    # Pas 2: Llegir fitxer 
    dades = llegir_arxiu_xifrat("xifratge_secret.txt")
    
    if not dades:
        print("Error: L'arxiu està buit o no existeix.")
        return

    # Pas 3: El Bucle Invers de 3 rondes 

    for ronda in range(3):
        # 1r: Desfem l'XOR de la clau 
        dades = afegeix_clau(dades, clau_usuari)
        
        # 2n: Desfem el moviment (moure a la dreta) 
        dades = moure_dreta(dades)
        
        # 3r: Desfem la substitució (S-Box inversa) 
        dades = invertir_substitució_nums(dades)
