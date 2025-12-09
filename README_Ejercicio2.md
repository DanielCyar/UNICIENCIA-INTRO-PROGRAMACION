# 🐉 Mini Proyecto 2 — Pokémon Battle System  
### *Curso Nivelatorio 7mo Semestre (Python 3) – UNICIENCIA*

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-✓-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)
![License](https://img.shields.io/badge/License-Academic-lightgrey.svg)

Un sistema interactivo de gestión y batallas Pokémon construido en **Python 3** y **pandas**, utilizando datos reales del archivo `pokemon.csv` suministrado por el docente.  
Incluye CRUD completo, menú interactivo y simulador de combate por turnos basado en estadísticas.

---

## 📑 Tabla de Contenidos

- Descripción General
- Características
- Estructura del Repositorio
- Requisitos
- Instalación y Ejecución
- Uso del Sistema
- Simulación de Batallas
- Ejemplos de Ejecución
- Complejidad Algorítmica
- Créditos

---

## 🧩 Descripción General

El proyecto implementa un **sistema de administración de Pokémon** junto con un **simulador de batallas 1 vs 1**, utilizando estadísticas reales del archivo `pokemon.csv`.

Este sistema permite:

✔ Cargar y validar datos desde CSV  
✔ Listar y administrar Pokémon con operaciones CRUD  
✔ Simular batallas completas mostrando cada ronda  
✔ Guardar cambios en un archivo CSV de salida  
✔ Validar estadísticos numéricos y entradas del usuario  

Todo el proyecto está diseñado para un **nivel intermedio universitario**, con código claro, modular y sin sobreingeniería.

---

## 🚀 Características

### 📥 Carga de Datos (pandas)
- Lectura limpia usando `pandas.read_csv()`.
- Filtrado de columnas relevantes.
- Conversión segura a tipos numéricos (`int`).
- Manejo de rutas relativo a la ubicación del script.

### 🛠️ CRUD Completo
- **Agregar Pokémon**
- **Modificar Pokémon**
- **Eliminar Pokémon**
- **Listar Pokémon**

### ⚔️ Sistema de Batalla
- Determinación del primer turno por `speed`.
- Daño calculado con fórmula simplificada:

```
damage = max(1, attack - defense // 2)
```

- Rondas iterativas hasta que un Pokémon llega a 0 HP.
- Registro detallado de cada acción.

### 💾 Guardado en CSV
Permite exportar cambios a:

```
OG/data/pokemon_salida.csv
```

o a una ruta personalizada.

---

## 📂 Estructura del Repositorio

```
UNICIENCIA-INTRO-PROGRAMACION
├── Ejercicio1.py
├── Ejercicio2.py          # ← este archivo
└── OG
    └── data
        └── pokemon.csv    # dataset oficial
```

---

## 📦 Requisitos

- Python **3.8+**
- La librería **pandas**

Instalar dependencias:

```bash
pip install pandas
```

---

## ▶ Instalación y Ejecución

1. Clonar o descargar el repositorio.
2. Ejecutar el programa desde la raíz:

```bash
python Ejercicio2.py
```

3. Al iniciar, verás:

```
Ingrese la ruta del archivo CSV de pokémons (o Enter para 'OG/data/pokemon.csv'):
```

Presiona **Enter** para usar el dataset por defecto.

---

## 🕹 Uso del Sistema

Una vez cargado el archivo, aparece el menú:

```
=== Menú Principal ===
1. Listar pokémons
2. Agregar pokémon
3. Modificar pokémon
4. Eliminar pokémon
5. Batalla entre pokémons
6. Guardar pokémons en CSV
0. Salir
```

---

## 🔥 Simulación de Batallas

La mecánica de combate es por turnos:

- El Pokémon con mayor **speed** ataca primero.
- El combate imprime cada ronda como un "log de batalla".
- Se calcula el daño con:

```
damage = max(1, attack - defense // 2)
```

- El combate termina cuando uno (o ambos) bajan a 0 HP.
- Se muestra el ganador o un empate.

---

## 📌 Ejemplos de Ejecución

### 🟦 Inicio de batalla

```
=== Batalla Pokémon ===
Nombre del primer Pokémon: Charmander
Nombre del segundo Pokémon: Squirtle

Batalla entre Charmander (Fire) y Squirtle (Water)!
```

### 🟥 Rondas

```
--- Ronda 1 ---
Squirtle ataca a Charmander y causa 9 de daño. HP restante: 30
--- Ronda 2 ---
Charmander ataca a Squirtle y causa 6 de daño. HP restante: 38
```

### 🟩 Resultado final

```
¡Squirtle gana la batalla!
```

---

## 🧾 Créditos

Este proyecto fue desarrollado como parte del curso:

**Curso Nivelatorio 7mo Semestre – UNICIENCIA (Python 3)**  
Mini Proyecto 2 — Sistema de Batallas Pokémon

Uso académico autorizado.  
Desarrollado por: *Daniel Mauricio Castro Yaruro*.
