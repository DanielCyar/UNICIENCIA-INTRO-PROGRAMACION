🐉 Mini Proyecto 2 – Sistema de Batallas Pokémon
Introducción a la Programación (Python 3) – UNICIENCIA

Este proyecto implementa un sistema interactivo de gestión y batallas Pokémon utilizando:

Python 3

La librería pandas

El archivo pokemon.csv suministrado por el docente

El sistema permite cargar información real de Pokémon desde un archivo CSV, manipularla (CRUD) y simular batallas 1 vs 1 basadas en sus estadísticas.

📂 Estructura del proyecto
UNICIENCIA-INTRO-PROGRAMACION
├── Ejercicio1.py
├── Ejercicio2.py   ← este proyecto
└── OG
    └── data
        └── pokemon.csv  ← datos oficiales del docente


El archivo Ejercicio2.py está preparado para detectar automáticamente el archivo CSV en:

OG/data/pokemon.csv

🎯 Objetivos del proyecto

Cargar datos desde un archivo CSV utilizando pandas.

Filtrar y validar columnas relevantes (name, type_1, hp, attack, defense, speed).

Implementar un menú interactivo que permita:

Listar Pokémon.

Agregar un Pokémon.

Modificar un Pokémon existente.

Eliminar un Pokémon.

Guardar cambios en un nuevo CSV.

Simular batallas Pokémon basadas en estadísticas reales.

Practicar programación modular, validación de entradas y uso básico de estructuras de datos.

📘 Características del sistema
✔ Carga de datos desde CSV

El programa usa pandas.read_csv() para cargar y validar los Pokémon existentes.

✔ Operaciones CRUD

Crear: agregar un nuevo Pokémon con sus estadísticas.

Read: listar los primeros registros del dataset.

Update: modificar cualquier Pokémon existente.

Delete: eliminar Pokémon por nombre.

✔ Sistema de batalla

Basado en estadísticas reales:

Quien tenga mayor speed ataca primero.

Fórmula de daño usada:

daño = max(1, attack_atacante - defense_defensor // 2)


El combate continúa por rondas hasta que uno o ambos Pokémon lleguen a 0 HP.

Se muestra un registro completo de la batalla.

✔ Guardado de cambios

Los datos modificados pueden exportarse a:

OG/data/pokemon_salida.csv


o una ruta que el usuario elija.

▶ Cómo ejecutar el programa

Instala dependencias:

pip install pandas


Ejecuta el programa:

python Ejercicio2.py


Cuando el programa pregunte:

Ingrese la ruta del archivo CSV de pokémons (o Enter para 'OG/data/pokemon.csv'):


Presiona Enter, a menos que quieras usar otra ruta.

📑 Explicación de archivos
Ejercicio2.py

Contiene toda la lógica del proyecto:

Manejo de archivos (carga y guardado).

Interfaz de menús.

CRUD con pandas.

Simulación de batalla por turnos.

Validación de campos numéricos.

pokemon.csv

Dataset oficial provisto por el docente.
Contiene más de 1000 registros con información de distintas generaciones Pokémon.

🧪 Ejemplo de uso
Menú principal
=== Menú Principal ===
1. Listar pokémons
2. Agregar pokémon
3. Modificar pokémon
4. Eliminar pokémon
5. Batalla entre pokémons
6. Guardar pokémons en CSV
0. Salir

Ejemplo de batalla
=== Batalla Pokémon ===
Nombre del primer Pokémon: Charmander
Nombre del segundo Pokémon: Squirtle

Batalla entre Charmander (Fire) y Squirtle (Water)!

--- Ronda 1 ---
Squirtle ataca a Charmander y causa 9 de daño. HP restante de Charmander: 30
--- Ronda 2 ---
Charmander ataca a Squirtle y causa 6 de daño. HP restante de Squirtle: 38
...
¡Squirtle gana la batalla!

🧠 Complejidad

Tiempo

Carga/guardado CSV: O(n)

Búsquedas por nombre: O(n)

CRUD: O(n) por reindexaciones de pandas

Batalla: O(r) siendo r el número de rondas

Espacio

O(n) para almacenar el DataFrame de Pokémon.

✔ Requisitos del entorno

Python 3.8 o superior

Librería pandas

Archivo pokemon.csv en:

OG/data/pokemon.csv

📌 Notas finales

El proyecto está diseñado a un nivel intermedio universitario, evitando sobreingeniería.

Se utiliza pandas porque es específicamente solicitado en el enunciado oficial.

Toda la lógica está implementada mediante funciones y estructuras básicas, sin POO avanzada.
