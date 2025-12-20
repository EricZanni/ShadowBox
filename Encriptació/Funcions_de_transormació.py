# Creem la taula de substitució del 255 al 0
sbox = list(range(255, -1, -1))

# Funció per substituir cada número de la llista per un altre segons la sbox
def substituir_nums(llista):
    resultat = []
    for n in llista:
        nou_valor = sbox[n] # Busquem el valor que hi ha a la posició n de la sbox
        resultat.append(nou_valor) # Afegim aquest valor a la nostra llista
    return resultat

# Funció contrària a la substitució
def invertir_substitució_nums(llista):
    resultat = []
    for n in llista:
        posicio_original = sbox.index(n) # Busquem en quina posició es troba el número n dins la sbox
        resultat.append(posicio_original)
    return resultat

# Funció per moure els elements cap a l'esquerra
def moure_esquerra(llista):
    if len(llista) < 2: # Si la llista té 0 o 1 elements, no cal moure res
        return llista
    return llista[1:] + [llista[0]] # Agafem des del segon element fins al final i hi enganxem el primer element al final

# Funció per moure els elements cap a la dreta
def moure_dreta(llista):
    if len(llista) < 2:
        return llista
    return [llista[-1]] + llista[:-1] # L'últim passa a ser el primer

# Barrejem la llista amb una clau secreta fent servir l'operació XOR
def afegeix_clau(llista, clau):
    resultat = []
    for i in range(len(llista)):
        # Apliquem l'operador XOR entre la dada i la clau
        # Utilitzem '%' per si la clau s'ha de repetir (si és més curta que la llista)
        valor_combinat = llista[i] ^ clau[i % len(clau)]
        resultat.append(valor_combinat)
    return resultat