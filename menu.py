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
    from desencriptar.desxifrar import desxifrar

def consultar_hashes():
    from hash.hash import opcio_usuari
    opcio_usuari()

def ocultar_text():
    print("         OCULTAR TEXT          ")
    print("-------------------------------")

    print("Selecciona una opcio: ")
    print("1. Amagar text")
    print("2. Recuperar text")
    opcio = input("Opcio: ")
    
    if opcio == "1":
        from esteganografia.esteganografia import amagar_text
        while True:
            imatge = input("Arrossega la imatge : ").replace('"', '')
            if imatge == "":
                print("ERROR: No s'ha detectat cap imatge")
            else:
                text = input("Introdueix el text que vols amagar: ")
                if text == "":
                    print("ERROR: No s'ha detectat cap text")
                else:
                    from esteganografia.esteganografia import amagar_text
                    amagar_text(imatge, text)
                    break


    elif opcio == "2":
        while True:
            imatge = input("Arrossega la imatge per llegir el missatge: ")
            if imatge == "":
                print("No hi ha cap imatge")
            else:
                from esteganografia.esteganografia_recuperar import recuperar_text
                recuperar_text(imatge)
    else:
        print("Opcio no valida.")
   

menu()
seleccionar_opcio()

