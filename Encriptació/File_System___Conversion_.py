
def llegir_ruta(nom_fitxer):
    with open(nom_fitxer, "rb") as f:
        contingut = f.read()
    return contingut

def text_a_numeros(contingut):
    llista_bytes = list(contingut)
    return llista_bytes

def numeros_a_text(llista_bytes):
    llista_numeros = bytes(llista_bytes)
    return(llista_numeros)

def guardar_llista_bytes(llista_numeros, nom_fitxer):
    text_final = ""

    for i in range(len(llista_numeros)):
        # Passem el número a text i l'afegim al resultat
        text_final += str(llista_numeros[i])
        
        # Si NO és l'últim número, hi afegim una coma per separar 
        if i < len(llista_numeros) - 1:
            text_final += ","
    
    # Ara que ja tenim tot el "72,111,108...", el guardem
    with open(nom_fitxer, "w", encoding="utf-8") as f:
        f.write(text_final)
    
    print(f"Fet! Arxiu guardat a: {nom_fitxer}")

