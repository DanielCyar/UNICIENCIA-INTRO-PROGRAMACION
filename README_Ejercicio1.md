# 🧮 Mini Proyecto 1 — Procesamiento de Operaciones Matemáticas desde Archivo CSV  
### *Curso Nivelatorio 7mo Semestre (Python 3) – UNICIENCIA*

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CSV](https://img.shields.io/badge/CSV-Processing-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)
![License](https://img.shields.io/badge/License-Academic-lightgrey.svg)

Un sistema de **procesamiento automático de operaciones matemáticas** desde archivos CSV utilizando exclusivamente **Python 3** y la librería estándar.  
El programa lee operaciones como SUMA, RESTA, MULTIPLICACIÓN, DIVISIÓN y POTENCIA desde un archivo, calcula sus resultados y actualiza el CSV con las columnas `computed_result` e `is_correct`.

---

## 📑 Tabla de Contenidos

- Descripción General  
- Características  
- Estructura del Repositorio  
- Requisitos  
- Instalación y Ejecución  
- Formato del Archivo CSV  
- Proceso de Cálculo  
- Ejemplos de Ejecución  
- Complejidad Algorítmica  
- Créditos  

---

## 🧩 Descripción General

Este proyecto implementa un programa que:

✔ Lee un archivo CSV con operaciones matemáticas.  
✔ Calcula resultados en función del tipo de operación.  
✔ Compara el resultado con la columna `correct_result` (si existe).  
✔ Actualiza el CSV original añadiendo los campos:  
   - `computed_result`  
   - `is_correct`  
✔ Gestiona errores como división por cero, operaciones inválidas y operandos no numéricos.

El diseño está orientado a un **nivel intermedio universitario**, priorizando claridad, modularidad y uso responsable de la librería estándar.

---

## 🚀 Características

### 📥 Lectura de Datos (csv.DictReader)
- Interpretación automática de filas como diccionarios.  
- Manejo seguro de rutas de archivo.  
- Validación de columnas requeridas.

### 🧠 Motor de Cálculo Integrado
Soporta operaciones:

```
SUM → Suma
RES → Resta
MUL → Multiplicación
DIV → División (con verificación de división por cero)
POW → Potencia
```

Cada cálculo retorna:

- El valor numérico **o**
- `"ERROR"` cuando no es posible computar la operación.

### ✔ Validación de Resultados
Cuando el archivo contiene `correct_result`, el sistema verifica:

- Igualdad numérica (con tolerancia para flotantes).  
- Igualdad textual como alternativa de respaldo.

### 💾 Actualización del CSV
Las dos nuevas columnas agregadas son:

```
computed_result
is_correct
```

El archivo de entrada se sobrescribe con los resultados procesados.

---

## 📂 Estructura del Repositorio

```
UNICIENCIA-INTRO-PROGRAMACION
├── Ejercicio1.py        # ← script principal
├── Ejercicio2.py
└── data
    └── math_operations.csv   # dataset de operaciones
```

---

## 📦 Requisitos

- Python **3.8+**
- No requiere librerías externas.

---

## ▶ Instalación y Ejecución

1. Clonar o descargar el repositorio.  
2. Ejecutar el archivo:

```bash
python Ejercicio1.py
```

3. El sistema pedirá:

```
Ingrese la ruta del archivo CSV (o Enter para 'data/math_operations.csv'):
```

Presiona **Enter** para usar el archivo por defecto.

---

## 📁 Formato del Archivo CSV

El archivo debe incluir al menos:

| operation | operand_1 | operand_2 | correct_result (opcional) |

Ejemplo:

```csv
operation,operand_1,operand_2,correct_result
SUM,2,3,5
MUL,4,5,20
DIV,10,2,5
DIV,7,0,
POW,2,3,8
```

---

## 🔢 Proceso de Cálculo

### Fórmulas utilizadas

```
SUM: op1 + op2
RES: op1 - op2
MUL: op1 * op2
DIV: op1 / op2 (error si op2 == 0)
POW: op1 ** op2
```

### Manejo de errores

| Caso | Acción |
|------|--------|
| División por cero | `computed_result = "ERROR"` |
| Operación desconocida | `"ERROR"` |
| Operandos no numéricos | `"ERROR"` |
| `correct_result` ausente | `is_correct = ""` |

### Columnas agregadas al CSV

```
computed_result: resultado numérico o "ERROR"
is_correct: True / False / ""
```

---

## 🟦 Ejemplo de Ejecución

```
=== Mini Proyecto 1: Operaciones matemáticas desde CSV ===
Ingrese la ruta del archivo CSV (o Enter para 'data/math_operations.csv'):

Procesamiento completado.
Filas procesadas: 5
Resultados correctos según 'correct_result': 4
Operaciones con error (incluye división por cero): 1
```

### 🟩 Archivo actualizado

```csv
operation,operand_1,operand_2,correct_result,computed_result,is_correct
SUM,2,3,5,5.0,True
MUL,4,5,20,20.0,True
DIV,10,2,5,5.0,True
DIV,7,0,,ERROR,False
POW,2,3,8,8.0,True
```

---

## 📊 Complejidad Algorítmica

- **Tiempo:** O(n) — Cada fila se procesa exactamente una vez.  
- **Espacio:** O(n) — Las filas se almacenan temporalmente para sobrescribir el archivo.  

---

## 🧾 Créditos

Este proyecto fue desarrollado como parte del curso:

**Curso Nivelatorio 7mo Semestre – UNICIENCIA (Python 3)**  
Mini Proyecto 1 — Procesamiento de operaciones matemáticas desde CSV.

Uso académico autorizado.  
Desarrollado por: *Daniel Mauricio Castro Yaruro*.
