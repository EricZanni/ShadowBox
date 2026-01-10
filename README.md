# ShadowBox

## Descripció
ShadowBox és una eina de seguretat multifuncional desenvolupada en Python. Aquest programa integra diverses tècniques de criptografia i seguretat informàtica en una sola interfície de consola, permetent als usuaris xifrar missatges, ocultar informació dins d'imatges (esteganografia) i gestionar la integritat dels fitxers mitjançant funcions hash.

## Funcionalitats Principals
El sistema disposa d'un menú principal amb quatre mòduls clau:

1. **Xifratge de Text:**
   - Converteix el contingut d'un fitxer de text en una seqüència numèrica il·legible.
   - Utilitza un algorisme propi de 3 rondes que combina: substitució (S-Box inversa), desplaçament de bits a l'esquerra i operacions XOR amb una clau proporcionada per l'usuari.

2. **Desxifratge de Text:**
   - Reverteix el procés de xifratge per recuperar el missatge original.
   - Aplica les operacions inverses: XOR, desplaçament a la dreta i substitució original.

3. **Gestió de Hashes i Usuaris:**
   - Sistema complet de registre i autenticació.
   - **Creació de comptes:** Polítiques de contrasenya robustes (majúscules, minúscules, números, símbols i mínim 8 caràcters).
   - **Integritat de fitxers:** Registra l'empremta digital (Hash SHA-256) de fitxers per verificar posteriorment si han estat modificats.
   - **Panell d'administrador:** Permet visualitzar l'historial de tots els registres de fitxers.

4. **Esteganografia:**
   - Permet ocultar missatges de text dins de fitxers d'imatge (tècnica de *file appending*) i recuperar-los posteriorment.
   - Utilitza un separador binari (`#####`) per distingir la imatge del text ocult.

## Requisits del Sistema
Per executar aquest programa necessites tenir instal·lat:
* **Python 3.x**
* La llibreria externa `pwinput` (per a l'entrada oculta de contrasenyes al mòdul de hash).

## Instal·lació
1. Clona el repositori o assegura't de tenir els fitxers del projecte organitzats en les seves carpetes corresponents.
2. Instal·la la dependència necessària executant la següent comanda a la terminal:

```bash
pip install pwinput
