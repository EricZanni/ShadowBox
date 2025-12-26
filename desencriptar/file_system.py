def llegir_arxiu_xifrat(nom_arxiu):
    with open(nom_arxiu, "r", encoding='utf-8') as f: 
        contingut = f.read()
        if contingut == "":
            return []

    numeros_text = contingut.split(',')
    llista_numeros = []

    for numero in numeros_text:
        if numero.strip():
            llista_numeros.append(int(numero))
            
    print(llista_numeros)

    return llista_numeros


llegir_arxiu_xifrat("xifratge_secret.txt")