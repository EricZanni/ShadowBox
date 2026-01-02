def recuperar_text(imatge):
    # Obrim la imatge en mode binari ('rb') per llegir tota la informació del fitxer
    with open(imatge, "rb") as f:
        contingut = f.read()
    
    separador = b"#####" 

    # Busquem el separador dins del contingut, si hi és, tallem el contingut i la part [0] és la imatge i la part [1] és el text secret.
    if separador in contingut:
        missatge_en_bytes = contingut.split(separador)[1]
        
        # Convertim els bytes a text (utf-8)
        text_recuperat = missatge_en_bytes.decode("utf-8")
        print(f"\nMissatge recuperat amb èxit:")
        print(f"{text_recuperat}")
    else:
        print("\n No s'ha trobat cap missatge secret en aquesta imatge.")


