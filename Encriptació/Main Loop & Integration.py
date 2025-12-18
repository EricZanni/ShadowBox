import Funcions_de_transormacio as ft
import File_System___Conversion_ as fl

def xifrar(nom_fitxer):
	contingut_bytes = fl.llegir_ruta(nom_fitxer)
	llista_numeros = fl.text_a_numeros(contingut_bytes)
	print(f"Iniciant xifratge de {len(llista_numeros)} bytes: {llista_numeros}")

	clau = input("Introdueix la contrasenya: ")
	clau_numeros = [ord(x) for x in clau]

	for i in range(3):
		llista_numeros = ft.sub_bytes(llista_numeros)     # Substitució [cite: 4]
		llista_numeros = ft.shift_rows(llista_numeros)    # Desplaçament [cite: 5]
		llista_numeros = ft.add_round_key(llista_numeros, clau_numeros) # Barreja amb clau [cite: 6]

	print(llista_numeros)



xifrar("secret.txt")