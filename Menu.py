
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
        seleccio_funcio = int(input("Selecciona la funcio que vols utilitzar: "))
        if seleccio_funcio == 1:
            xifrar()
            break
        elif seleccio_funcio == 2:
            desxifrar()
            break
        elif seleccio_funcio == 3:
            consultar_hashes()
            break
        elif seleccio_funcio == 4:
            ocultar_text()
            break
        else:
            print("ERROR: Has de posar el numero corresponent de la funcio que vols utilitzar")
            

        


def xifrar():
    print("         XIFRAR          ")
    print("-------------------------")

def desxifrar():
    print("         DESXIFRAR          ")
    print("----------------------------")

def consultar_hashes():
    print("         CONSULTAR HASHES          ")
    print("-----------------------------------")

def ocultar_text():
    print("         OCULTAR TEXT          ")
    print("-------------------------------")


print()
menu()
