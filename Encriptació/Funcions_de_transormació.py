sbox = list(range(255, -1, -1))

def sub_bytes(llista):
   
    resultat = []
    for n in llista:
        nou_valor = sbox[n]
        resultat.append(nou_valor)
    return resultat

def inv_sub_bytes(llista):
    
    resultat = []
    for n in llista:
        original = sbox.index(n)
        resultat.append(original)
    return resultat

def shift_rows(llista):
    if len(llista) < 2:
        return llista
    return llista[1:] + [llista[0]]

def inv_shift_rows(llista):
    if len(llista) < 2:
        return llista
    return [llista[-1]] + llista[:-1]

def add_round_key(llista, clau):
    resultat = []
    for i in range(len(llista)):
        valor = llista[i] ^ clau[i % len(clau)]
        resultat.append(valor)
    return resultat