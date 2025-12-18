# ShadowBox: Suite de Gestió d'Identitat i Criptografia Aplicada

## Introducció
**ShadowBox** és una plataforma de seguretat integral desenvolupada en Python, dissenyada per centralitzar la protecció d'informació sensible. El programa combina la gestió robusta d'identitats, algoritmes de transformació criptogràfica i la manipulació de fitxers a baix nivell.

L'objectiu principal és oferir un entorn controlat on els usuaris puguin assegurar la seva identitat i aplicar capes de xifratge personalitzat als seus documents, garantint que la informació només sigui accessible pels seus propietaris legítims.

---

## Funcionalitats del Programa

El sistema ofereix un conjunt d'eines tècniques avançades dividides en mòduls especialitzats:

* **Gestió d'Usuaris Segura:** Permet la creació de comptes amb validació de contrasenyes robustes que han d'incloure majúscules, minúscules, números i símbols.
* **Protecció mitjançant Hashing:** Utilitza l'algoritme **SHA-256** per generar signatures digitals de les contrasenyes, assegurant que les claus reals mai s'emmagatzemin en text pla.
* **Sistema de Conversió de Fitxers:** Capacitat per llegir fitxers en mode binari i convertir-los en llistes numèriques per facilitar el seu processament criptogràfic.
* **Validació de Propietat:** Inclou un mòdul per associar fitxers a usuaris específics mitjançant la verificació prèvia de credencials.
* **Esteganografia:** El sistema està preparat per integrar funcions d'ocultació de missatges de text dins de fitxers d'imatge.

---

## Públic Objectiu i Sector

**ShadowBox** està orientat a donar solució a necessitats en els següents sectors:

1. **Educació en Ciberseguretat:** Ideal per a estudiants que desitgin comprendre el funcionament intern dels processos de xifratge simètric i la gestió de bases de dades d'usuaris.
2. **Privacitat de Dades Personals:** Per a usuaris que requereixin una eina lleugera per anonimitzar fitxers locals abans del seu emmagatzematge.
3. **Desenvolupament de Programari:** Com a base per implementar mòduls de validació de contrasenyes i tractament de fitxers binaris en projectes de major escala.

---

## Especificacions Tècniques

* **Llenguatge:** Python 3.x.
* **Llibreries:** Ús de la llibreria estàndard `hashlib` per a seguretat criptogràfica.
* **Persistència:** Emmagatzematge de dades en fitxers de text pla per assegurar la portabilitat.

---

## Instruccions d'Ús

1. Executa el fitxer principal `menu.py`.
2. Selecciona una opció del menú interactiu (Xifrar, Desxifrar, Consultar Hashes u Ocultar text).
3. Segueix les instruccions en pantalla per al registre d'usuaris o la manipulació de fitxers.
