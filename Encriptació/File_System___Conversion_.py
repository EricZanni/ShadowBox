def demanar_arxiu():
    while True:
        entrada_usuari = input("Arrossega l'arxiu: ")

        nom_net = entrada_usuari.replace("&", "")
        nom_net = nom_net.replace("'", "").replace('"', "")
        nom_net = nom_net.strip()
        llegir_arxiu(nom_net)
   
        return nom_net


def llegir_arxiu(nom_net):
    try:
        with open(nom_net, "rb") as f:
            contingut_bytes = f.read()
            llista_bytes = list(contingut_bytes)
            text_bytes = str(llista_bytes)
            net_text_byte = text_bytes.replace(",", "").replace("[", "").replace("]","")
        return net_text_byte
    except FileNotFoundError:
        print(f"ERROR: No trobo l'arxiu {nom_net}")
     
def llegir_arxiu(nom_net):
    try:
        with open(nom_net, "rb") as f:
            datos_bytes = f.read()  # Aqu  tienes un objeto de tipo 'bytes'
            
        # Decodificamos los bytes directamente a texto
        texto = datos_bytes.decode("utf-8") 
        return texto
    except FileNotFoundError:
        print(f"ERROR: No trobo l'arxiu {nom_net}")

   
arxiu = demanar_arxiu()
text_bytes = llegir_arxiu(arxiu)
