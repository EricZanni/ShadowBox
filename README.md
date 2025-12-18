# ShadowBox: Suite de Gestión de Identidad y Criptografía Aplicada

## Introducción
**ShadowBox** es una plataforma de seguridad integral desarrollada en Python, diseñada para centralizar la protección de información sensible. [cite_start]El programa combina la gestión robusta de identidades, algoritmos de transformación criptográfica y la manipulación de archivos a bajo nivel[cite: 1].

El objetivo principal es ofrecer un entorno controlado donde los usuarios puedan asegurar su identidad y aplicar capas de cifrado personalizado a sus documentos, garantizando que la información solo sea accesible por sus propietarios legítimos.

---

## Funcionalidades del Programa

El sistema ofrece un conjunto de herramientas técnicas avanzadas divididas en módulos especializados:

* **Gestión de Usuarios Segura:** Permite la creación de cuentas con validación de contraseñas robustas que deben incluir mayúsculas, minúsculas, números y símbolos.
* **Protección mediante Hashing:** Utiliza el algoritmo **SHA-256** para generar firmas digitales de las contraseñas, asegurando que las claves reales nunca se almacenen en texto plano.
* **Motor de Cifrado (Transformación):** Implementa funciones de sustitución de bytes (SubBytes), rotación de filas (ShiftRows) y mezcla con clave secreta mediante operaciones XOR (AddRoundKey).
* [cite_start]**Sistema de Conversión de Archivos:** Capacidad para leer archivos en modo binario y convertirlos en listas numéricas para facilitar su procesamiento criptográfico[cite: 1].
* **Validación de Propiedad:** Incluye un módulo para asociar archivos a usuarios específicos mediante la verificación previa de credenciales.
* **Esteganografía:** El sistema está preparado para integrar funciones de ocultación de mensajes de texto dentro de archivos de imagen.

---

## Público Objetivo y Sector

**ShadowBox** está orientado a dar solución a necesidades en los siguientes sectores:

1.  **Educación en Ciberseguridad:** Ideal para estudiantes que deseen comprender el funcionamiento interno de los procesos de cifrado simétrico y la gestión de bases de datos de usuarios.
2.  [cite_start]**Privacidad de Datos Personales:** Para usuarios que requieran una herramienta ligera para anonimizar archivos locales antes de su almacenamiento[cite: 1].
3.  **Desarrollo de Software:** Como base para implementar módulos de validación de contraseñas y tratamiento de archivos binarios en proyectos de mayor escala.

---

## Especificaciones Técnicas

* **Lenguaje:** Python 3.x.
* **Librerías:** Uso de la librería estándar `hashlib` para seguridad criptográfica.
* **Persistencia:** Almacenamiento de datos en ficheros de texto plano para asegurar la portabilidad.

---

## Instrucciones de Uso

1. Ejecuta el archivo principal `menu.py`.
2. Selecciona una opción del menú interactivo (Xifrar, Desxifrar, Consultar Hashes u Ocultar texto).
3. Sigue las instrucciones en pantalla para el registro de usuarios o la manipulación de archivos.
