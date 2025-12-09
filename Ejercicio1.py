"""
Mini Proyecto 1
Lectura de operaciones desde un archivo CSV, cálculo del resultado
y actualización del mismo archivo con las columnas:
- computed_result
- is_correct
"""

import csv
from typing import Tuple, Optional


def leer_ruta_csv() -> str:
    """Pide al usuario la ruta del archivo CSV, con un valor por defecto."""
    ruta_por_defecto = "OG/data/math_operations.csv"
    print("=== Mini Proyecto 1: Operaciones matemáticas desde CSV ===")
    ruta = input(
        f"Ingrese la ruta del archivo CSV "
        f"(o presione Enter para usar '{ruta_por_defecto}'): "
    ).strip()
    if ruta == "":
        ruta = ruta_por_defecto
    return ruta


def convertir_numero(valor: str) -> float:
    """Convierte el texto a número (float). Lanza ValueError si no es válido."""
    return float(valor)


def calcular_operacion(operation: str,
                       op1: float,
                       op2: float) -> Tuple[Optional[float], bool]:
    """
    Calcula el resultado de la operación.

    Retorna:
      (resultado, hubo_error)
      - resultado None si hubo error (ej. división por cero).
      - hubo_error True si la operación no se pudo realizar.
    """
    op = operation.strip().upper()

    try:
        if op == "SUM":
            return op1 + op2, False
        elif op == "RES":
            return op1 - op2, False
        elif op == "MUL":
            return op1 * op2, False
        elif op == "DIV":
            if op2 == 0:
                return None, True
            return op1 / op2, False
        elif op == "POW":
            return op1 ** op2, False
        else:
            # Operación desconocida
            return None, True
    except Exception:
        # Cualquier otro error inesperado
        return None, True


def comparar_resultados(calculado: float, texto_correcto: str) -> bool:
    """
    Compara el resultado calculado con el valor de la columna correct_result.

    - Si correct_result se puede convertir a número, compara con tolerancia
      para flotantes.
    - Si no, compara como cadenas.
    """
    if texto_correcto is None:
        return False

    texto_correcto = texto_correcto.strip()
    if texto_correcto == "":
        return False

    try:
        esperado = float(texto_correcto)
        # Tolerancia para números flotantes
        return abs(calculado - esperado) < 1e-6
    except ValueError:
        # Si no es número, comparamos como texto
        return str(calculado) == texto_correcto


def procesar_archivo_csv(ruta_csv: str) -> None:
    """Lee, procesa y sobrescribe el archivo CSV con los resultados."""
    try:
        with open(ruta_csv, "r", newline="", encoding="utf-8") as f_in:
            lector = csv.DictReader(f_in)
            filas = []
            total = 0
            correctas = 0
            errores = 0

            # Encabezados originales
            fieldnames = lector.fieldnames or []

            # Aseguramos que las columnas nuevas estén
            columnas_nuevas = ["computed_result", "is_correct"]
            for col in columnas_nuevas:
                if col not in fieldnames:
                    fieldnames.append(col)

            for fila in lector:
                total += 1

                operation = fila.get("operation", "")
                op1_txt = fila.get("operand_1", "")
                op2_txt = fila.get("operand_2", "")

                try:
                    op1 = convertir_numero(op1_txt)
                    op2 = convertir_numero(op2_txt)
                except ValueError:
                    # No se pueden convertir los operandos
                    fila["computed_result"] = "ERROR"
                    fila["is_correct"] = "False"
                    errores += 1
                    filas.append(fila)
                    continue

                resultado, hubo_error = calcular_operacion(operation, op1, op2)

                if hubo_error or resultado is None:
                    fila["computed_result"] = "ERROR"
                    fila["is_correct"] = "False"
                    errores += 1
                else:
                    fila["computed_result"] = resultado
                    texto_correct = fila.get("correct_result")
                    if "correct_result" in fila and texto_correct is not None:
                        es_correcto = comparar_resultados(resultado, texto_correct)
                        fila["is_correct"] = str(es_correcto)
                        if es_correcto:
                            correctas += 1
                    else:
                        # No hay columna correct_result en el CSV
                        fila["is_correct"] = ""

                filas.append(fila)

    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {ruta_csv}")
        return

    # Escribimos de nuevo el archivo con resultados
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f_out:
        escritor = csv.DictWriter(f_out, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(filas)

    print("\nProcesamiento completado.")
    print(f"Filas procesadas: {total}")
    if "correct_result" in fieldnames:
        print(f"Resultados correctos según 'correct_result': {correctas}")
    print(f"Operaciones con error (incluye división por cero): {errores}")


def main() -> None:
    ruta = leer_ruta_csv()
    procesar_archivo_csv(ruta)


if __name__ == "__main__":
    main()