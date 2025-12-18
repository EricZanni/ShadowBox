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
    archivo = input("Dime el nombre del archivo (ej: secret.txt): ")
    
    
    # Importamos DENTRO de la función para evitar errores al inicio
    try:
        from encriptar.main_loop_integration import xifrar
        # Llamamos a la función PASANDO el nombre del archivo
        xifrar(archivo) 
    except ImportError as e:
        print(f"Error de sistema: No se encuentra el modulo de encriptacion. {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

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

