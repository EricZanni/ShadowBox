def guardar_imatge_text(imatge_original, imatge_sortida, text):
    separador = b"#####"
    missatge_en_bytes = text.encode("utf-8")

    # Llegim tota la imatge original
    with open(imatge_original, "rb") as f:
        contingut_imatge = f.read()

    # Escrivim una nova imatge amb el text ocult
    with open(imatge_sortida, "wb") as f:
        f.write(contingut_imatge)
        f.write(separador)
        f.write(missatge_en_bytes)

    print(f"Imatge creada amb el text ocult: {imatge_sortida}")
