# ShadowBox

## Descripció
ShadowBox és una eina de seguretat multifuncional desenvolupada en Python. Aquest programa integra diverses tècniques de criptografia i seguretat informàtica en una sola interfície de consola, permetent als usuaris xifrar missatges, ocultar informació dins d'imatges (esteganografia) i gestionar la integritat dels fitxers mitjançant funcions hash.

## Funcionalitats Principals
El sistema disposa d'un menú principal amb quatre mòduls clau:

1. **Xifratge de Text:** - Converteix el contingut d'un fitxer de text en una seqüència numèrica il·legible.
   - Utilitza un algorisme propi de 3 rondes que combina: substitució (S-Box inversa), desplaçament de bits a l'esquerra i operacions XOR amb una clau proporcionada per l'usuari.

2. **Desxifratge de Text:** - Reverteix el procés de xifratge per recuperar el missatge original.
   - Aplica les operacions inverses: XOR, desplaçament a la dreta i substitució original.

3. **Gestió de Hashes i Usuaris:** - Sistema complet de registre i autenticació.
   - **Creació de comptes:** Polítiques de contrasenya robustes (majúscules, minúscules, números, símbols i mínim 8 caràcters).
   - **Integritat de fitxers:** Registra l'empremta digital (Hash SHA-256) de fitxers per verificar posteriorment si han estat modificats.
   - **Panell d'administrador:** Permet visualitzar l'historial de tots els registres de fitxers.

4. **Esteganografia:** - Permet ocultar missatges de text dins de fitxers d'imatge (tècnica de *file appending*) i recuperar-los posteriorment.
   - Utilitza un separador binari (`#####`) per distingir la imatge del text ocult.

## Requisits del Sistema
Per executar aquest programa necessites tenir instal·lat:
* **Python 3.x**
* La llibreria externa `pwinput` (per a l'entrada oculta de contrasenyes al mòdul de hash).

## Instal·lació
1. Assegura't de tenir els fitxers del projecte organitzats en les seves carpetes corresponents (`encriptar`, `desencriptar`, `hash`, `esteganografia`) tal com requereixen els imports del `menu.py`.
2. Instal·la la dependència necessària executant la següent comanda a la terminal:

```bash
pip install pwinput

Instruccions d'Ús
Per iniciar el programa, executa l'arxiu principal:

Bash

python menu.py
1. Xifrar
Important: Has de tenir un fitxer anomenat exactament secret.txt al directori principal amb el text que vols protegir.

Introdueix una clau quan el sistema t'ho demani. Com més forta sigui la clau, millor serà l'encriptació.

Es generarà un nou fitxer anomenat xifratge_secret.txt.

2. Desxifrar
El sistema buscarà automàticament l'arxiu xifratge_secret.txt.

Introdueix la mateixa clau utilitzada durant el xifratge per veure el missatge original revelat per pantalla.

3. Consultar Hashes
Crear compte: Segueix les instruccions per crear un usuari vàlid.

Associar/Verificar: Et permet guardar el hash d'un fitxer i comprovar més tard si ha estat modificat (detecta canvis en el contingut).

Administració: Per accedir a l'historial global (opció 4), necessites credencials d'administrador.

Usuari Admin per defecte: kevindre

Contrasenya Admin: tUTU77.0

4. Ocultar textos en imatges
Amagar text: Arrossega una imatge a la terminal quan se't demani i escriu el text secret. El programa afegirà el text al final del fitxer d'imatge.

Recuperar text: Arrossega la imatge que conté el secret per extreure el missatge amagat.

Estructura del Projecte
L'estructura de directoris ha de ser la següent perquè el menu.py funcioni correctament:

menu.py: Script principal.

secret.txt: Arxiu d'entrada per defecte.

Usuaris.txt: Base de dades d'usuaris.

Administradors.txt: Credencials d'admin.

Usuaris_fitxers.txt: Registre d'auditoria.

/encriptar: Conté main_loop_integration.py, funcions_de_transformacio.py, etc.

/desencriptar: Conté desxifrar.py, Funcions_desencriptar.py, etc.

/hash: Conté hash.py.

/esteganografia: Conté esteganografia.py, esteganografia_recuperar.py.

Notes
L'algorisme de xifratge fa 3 passades per millorar la seguretat.

En l'esteganografia, evita utilitzar la seqüència ##### dins del teu missatge secret, ja que actua com a delimitador de final de fitxer.
