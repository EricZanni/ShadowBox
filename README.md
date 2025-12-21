# ShadowBox (Alpha)

> **Suite de Gestió d'Identitat i Criptografia Aplicada**

**ShadowBox** és una plataforma de seguretat desenvolupada en Python, dissenyada per centralitzar la protecció d'informació sensible. Aquesta versió **Alfa** presenta el nucli del motor de xifratge personalitzat i un sistema complet de gestió d'usuaris amb hashing segur.

---

## Introducció
L'objectiu principal és oferir un entorn controlat on els usuaris puguin assegurar la seva identitat i aplicar capes de xifratge personalitzat als seus documents. El projecte combina la gestió d'identitats, algoritmes de transformació criptogràfica i la manipulació de fitxers a baix nivell.

## Funcionalitats (Versió Alfa)

Aquesta versió inclou els següents mòduls operatius:

### 1. Sistema de Xifratge Personalitzat
Un algoritme de xifratge simètric propi que transforma fitxers de text (`secret.txt`) mitjançant múltiples capes de seguretat:
* [cite_start]**Transformació de Bytes:** Conversió directa de fitxers a llistes numèriques.
* **Algoritme de 3 Rondes:** Cada arxiu passa per 3 iteracions de transformació:
    * [cite_start]**Substitució (S-Box):** Substitució no lineal de valors (taula inversa 255-0).
    * [cite_start]**Permutació (Bit Shifting):** Desplaçament de bytes a l'esquerra.
    * [cite_start]**Mescla amb Clau (XOR):** Aplicació d'una clau secreta proporcionada per l'usuari.

### 2. Gestió d'Identitat i Hashing
Sistema robust per a la creació i validació d'usuaris:
* **Hashing SHA-256:** Les contrasenyes s'emmagatzemen com a hash hexadecimal, mai en text pla.
* **Polítiques de Contrasenya Forta:** Validació obligatòria (Majúscula, minúscula, número, símbol i mínim 8 caràcters).
* **Persistència:** Base de dades local a `Usuaris.txt`.

---
## Instruccions d'Ús

1. Executa el fitxer principal `menu.py`.
2. Selecciona una opció del menú interactiu (Xifrar, Desxifrar, Consultar Hashes u Ocultar text).
3. Segueix les instruccions en pantalla per al registre d'usuaris o la manipulació de fitxers.
## Requisits i Instal·lació

Aquest projecte requereix **Python 3.x**.

### Dependències
El projecte utilitza la llibreria externa `pwinput` per a l'entrada oculta de contrasenyes (asteriscs).

```bash
pip install pwinput

