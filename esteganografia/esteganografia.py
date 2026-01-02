


def amagar_text(imatge, text):
    # Convertim el missatge de text a bytes
    missatge_en_bytes = text.encode("utf-8")
    
    # Definim un separador per saber on comença el missatge secret
    # Utilitzo "#####" com a marca.
    separador = b"#####" 

    # Obrim la imatge en mode "append binary" ('ab')
    # 'a' = append (afegir al final), 'b' = binary (binari)
    with open(imatge, "ab") as f:
        f.write(separador)        # Escrivim la marca
        f.write(missatge_en_bytes) # Escrivim el missatge secret
    
    print(f"Missatge amagat amb exit a {imatge}!")
    



