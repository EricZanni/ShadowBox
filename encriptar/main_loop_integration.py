
from . import funcions_de_transformacio as ft
from . import file_system___conversion_ as fl

def xifrar(nom_fitxer):
    contingut_bytes = fl.llegir_ruta(nom_fitxer)

    llista_numeros = fl.text_a_llista(contingut_bytes)
    print(f"Iniciant xifratge de {len(llista_numeros)} bytes...")
    while True:
        print("Ara introduiras la clau, pensa que quan mes forta sigui aquesta millor encriptacio tindra el text")
        clau = input("Introdueix la clau: ")
        if clau == "":
            print("ERROR: La clau no pot estar buida.")
            return
        else:
            clau_numeros = [ord(x) for x in clau] #Per cada lletra en la clau es transforma en ord

            for i in range(3):
                llista_numeros = ft.sub_bytes(llista_numeros)     
                llista_numeros = ft.shift_rows(llista_numeros)    
                llista_numeros = ft.add_round_key(llista_numeros, clau_numeros) 
    
            print(llista_numeros)
            fl.guardar_llista_bytes(llista_numeros, "xifratge_" + nom_fitxer)
            print(f"Arxiu xifrat correctament: xifratge_{nom_fitxer}")
            break


if __name__ == "__main__":
    xifrar("secret.txt")