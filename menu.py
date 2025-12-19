import os

def menu():
    print("           ShadowBox        ")
    print("----------------------------")
    print("         1. Xifrar\n        ")
    print("       2. Desxifrar\n      ")
    print("    3. Consultar Hashes\n ")
    print(" 4. Ocultar textos en imatges\n ")

def seleccionar_opcio():
    print()
    while True:
        seleccio_funcio = input("Selecciona la funcio que vols utilitzar: ")
        if seleccio_funcio == "1":
            xifrar()
            break
        elif seleccio_funcio == "2":
            desxifrar()
            break
        elif seleccio_funcio == "3":
            consultar_hashes()
            break
        elif seleccio_funcio == "4":
            ocultar_text()
            break
        else:
            print("ERROR: Has de posar el numero corresponent de la funcio que vols utilitzar")
            

        


def xifrar():
    print("         XIFRAR          ")
    print("-------------------------")
    print("Abans de comencar asegurat que en el fitxer secret.txt hi hagi el missatge que vols xifrar ")
    while True:
        arxiu = input("Obre  el fitxer introduint --> secret.txt: ")
        if arxiu != "secret.txt":
            print("ERROR: Has d'introduir exactament --> secret.txt <-- ")
        elif arxiu == "secret.txt":
                from encriptar.main_loop_integration import xifrar
                xifrar(arxiu)
                break

def desxifrar():
    print("         DESXIFRAR          ")
    print("----------------------------")

def consultar_hashes():
    from hash.hash import menu_visual_hash, opcio_usuari
    menu_visual_hash()
    opcio_usuari()

def ocultar_text():
    print("         OCULTAR TEXT          ")
    print("-------------------------------")


menu()
seleccionar_opcio()

