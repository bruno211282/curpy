# PyNotes

Implementación de un block de notas para presentar en el curso de python dictado por la UTN FRBA.
Se utiliza como motor de ventanas PyQt5 y base de datos a SQLite3.
![PyNotes](img/pynotes.png "Pantalla principal")

## Autores (Nivel Intermedio)
  - García, Bruno
  - Gómez, Ezequiel
  - Mazzucco, Francisco
  - Rodríguez, María Belén

## Autores (Nivel Avanzado)
  - García, Bruno

## Dependencias
La aplicación está desarrollada utilizando Python versión 3.9.13. Antes de ejecutar nada se debe tener instalado el interprete de python correspondiente. Se lo puede descargar de [python.org](https://www.python.org/downloads/).
Una vez instalado el interprete, para instalar las dependencias se debe ejecutar el comando:

    pip install -r requirements.txt


## Modo de uso
Se debe ejecutar el siguiente comando en una consola ubicada en el directorio raíz del proyecto:

    python notes.py


## Funcionalidades pendientes
  - Agregar el acceso a una SQL via red para compartir notas.
  - Desarrollo de un ORM basado en descriptores.
  - Agregar manejo de algunas excepciones
  - Agregar la funcionalidad del filtrado de notas (existe el campo para filtrar, pero no tiene funcionalidad)
  - Chequear / Escapar caracteres especiales en los campos de texto para evitar SQL Inj.
