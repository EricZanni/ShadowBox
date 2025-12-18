# Fíjate en el punto (.) antes de los imports. 
# Esto significa "importar desde esta misma carpeta"

from . import funcions_de_transformacio as ft
from . import file_system___conversion_ as fl

def xifrar(nom_fitxer):
    try:
        # Intentamos leer el archivo
        contingut_bytes = fl.llegir_ruta(nom_fitxer)
    except FileNotFoundError:
        print(f"ERROR: No se encuentra el archivo '{nom_fitxer}'")
        return

    llista_numeros = fl.text_a_numeros(contingut_bytes)
    print(f"Iniciant xifratge de {len(llista_numeros)} bytes...")

    clau = input("Introdueix la contrasenya: ")
    # Aseguramos que la clave tenga longitud
    if not clau:
        print("Error: La contrasenya no pot estar buida.")
        return
        
    clau_numeros = [ord(x) for x in clau]

    for i in range(3):
        llista_numeros = ft.sub_bytes(llista_numeros)     
        llista_numeros = ft.shift_rows(llista_numeros)    
        llista_numeros = ft.add_round_key(llista_numeros, clau_numeros) 

    # Guardamos el resultado cifrado en un nuevo archivo para no romper el original
    fl.guardar_llista_bytes(llista_numeros, "cifrado_" + nom_fitxer)
    print(f"Arxiu xifrat correctament: cifrado_{nom_fitxer}")

# ELIMINAMOS O PROTEGEMOS LA LLAMADA FINAL
if __name__ == "__main__":
    xifrar("secret.txt")