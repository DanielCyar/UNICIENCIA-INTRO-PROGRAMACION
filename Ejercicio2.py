#!/usr/bin/env python3
"""
Mini Proyecto 2
Sistema de batallas entre Pokémons usando pandas y el archivo OG/data/pokemon.csv.

Se usan estas columnas del CSV:
- name
- type_1
- hp
- attack
- defense
- speed
"""

import os
import pandas as pd

# Carpeta donde está este script (Ejercicio2.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta por defecto al CSV: OG/data/pokemon.csv (relativa a la ubicación del script)
DEFAULT_CSV_PATH = os.path.join(BASE_DIR, "OG", "data", "pokemon.csv")


class PokemonGame:
    """Gestor de pokémons y batallas basado en un DataFrame de pandas."""

    def __init__(self) -> None:
        self.df = pd.DataFrame()
        # Ruta actual del CSV que se está usando
        self.csv_path = DEFAULT_CSV_PATH

    # ===================== CARGA / GUARDADO =====================

    def load_from_csv(self, ruta: str) -> None:
        """Carga los pokémons desde un archivo CSV usando pandas.

        Si 'ruta' es relativa, se interpreta respecto a BASE_DIR.
        """
        # Si la ruta no es absoluta, la hacemos relativa al directorio del script
        if not os.path.isabs(ruta):
            ruta = os.path.join(BASE_DIR, ruta)

        try:
            df_full = pd.read_csv(ruta)
        except FileNotFoundError:
            print(f"[ERROR] No se encontró el archivo: {ruta}")
            return

        columnas_necesarias = ["name", "type_1", "hp", "attack", "defense", "speed"]
        for col in columnas_necesarias:
            if col not in df_full.columns:
                print(f"[ERROR] La columna requerida '{col}' no está en el CSV.")
                return

        df = df_full[columnas_necesarias].copy()

        # Asegurar tipos numéricos
        for col in ["hp", "attack", "defense", "speed"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Eliminar filas con datos numéricos inválidos
        df = df.dropna(subset=["hp", "attack", "defense", "speed"])
        df[["hp", "attack", "defense", "speed"]] = df[
            ["hp", "attack", "defense", "speed"]
        ].astype(int)

        self.df = df.reset_index(drop=True)
        self.csv_path = ruta

        print(f"[OK] Pokémons cargados desde '{ruta}': {len(self.df)} filas válidas.")

    def save_to_csv(self, ruta: str) -> None:
        """Guarda el DataFrame actual a un archivo CSV.

        Si 'ruta' es relativa, se interpreta respecto a BASE_DIR.
        """
        if self.df.empty:
            print("[ADVERTENCIA] No hay pokémons para guardar.")
            return

        if not os.path.isabs(ruta):
            ruta = os.path.join(BASE_DIR, ruta)

        self.df.to_csv(ruta, index=False)
        print(f"[OK] Pokémons guardados en '{ruta}'.")

    # ===================== UTILIDADES =====================

    def _pedir_entero(self, mensaje: str, minimo: int = 0) -> int:
        """Pide un entero al usuario, repite si hay error."""
        while True:
            texto = input(mensaje).strip()
            try:
                valor = int(texto)
                if valor < minimo:
                    print(f"Debe ser un entero >= {minimo}.")
                    continue
                return valor
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")

    def _buscar_indice_por_nombre(self, nombre: str):
        """Devuelve el índice de la primera fila cuyo 'name' coincide (ignora mayúsculas)."""
        if self.df.empty:
            return None
        mask = self.df["name"].str.lower() == nombre.lower()
        indices = self.df[mask].index
        if len(indices) == 0:
            return None
        return indices[0]

    # ===================== CRUD =====================

    def listar_pokemons(self) -> None:
        """Muestra una lista de pokémons con sus estadísticas básicas."""
        if self.df.empty:
            print("[INFO] No hay pokémons cargados.")
            return

        print("\n=== Lista de Pokémons (primeras 20 filas) ===")
        print(self.df.head(20).to_string(index=False))

    def agregar_pokemon(self) -> None:
        """Agrega un nuevo pokémon al DataFrame."""
        print("\n=== Agregar nuevo Pokémon ===")
        name = input("Nombre: ").strip()
        if not name:
            print("[ERROR] El nombre no puede estar vacío.")
            return

        tipo = input("Tipo principal (type_1): ").strip()
        hp = self._pedir_entero("HP: ", minimo=1)
        atk = self._pedir_entero("Attack: ", minimo=0)
        defense = self._pedir_entero("Defense: ", minimo=0)
        speed = self._pedir_entero("Speed: ", minimo=0)

        nueva_fila = {
            "name": name,
            "type_1": tipo,
            "hp": hp,
            "attack": atk,
            "defense": defense,
            "speed": speed,
        }

        self.df = pd.concat(
            [self.df, pd.DataFrame([nueva_fila])],
            ignore_index=True
        )
        print(f"[OK] Pokémon '{name}' agregado.")

    def modificar_pokemon(self) -> None:
        """Modifica los datos de un pokémon existente."""
        print("\n=== Modificar Pokémon ===")
        nombre = input("Nombre del Pokémon a modificar: ").strip()
        idx = self._buscar_indice_por_nombre(nombre)
        if idx is None:
            print("[ERROR] No se encontró ese Pokémon.")
            return

        fila = self.df.loc[idx]
        print(f"Pokémon actual: {fila.to_dict()}")
        print("Deje el campo vacío para mantener el valor actual.")

        nuevo_nombre = input(f"Nuevo name [{fila['name']}]: ").strip()
        nuevo_tipo = input(f"Nuevo type_1 [{fila['type_1']}]: ").strip()

        def leer_opcional_entero(mensaje: str, actual: int) -> int:
            texto = input(mensaje).strip()
            if texto == "":
                return actual
            try:
                return int(texto)
            except ValueError:
                print("Valor no válido. Se mantiene el actual.")
                return actual

        nuevo_hp = leer_opcional_entero(f"Nuevo hp [{fila['hp']}]: ", int(fila["hp"]))
        nuevo_atk = leer_opcional_entero(
            f"Nuevo attack [{fila['attack']}]: ", int(fila["attack"])
        )
        nuevo_def = leer_opcional_entero(
            f"Nuevo defense [{fila['defense']}]: ", int(fila["defense"])
        )
        nuevo_spd = leer_opcional_entero(
            f"Nuevo speed [{fila['speed']}]: ", int(fila["speed"])
        )

        if nuevo_nombre:
            self.df.at[idx, "name"] = nuevo_nombre
        if nuevo_tipo:
            self.df.at[idx, "type_1"] = nuevo_tipo
        self.df.at[idx, "hp"] = nuevo_hp
        self.df.at[idx, "attack"] = nuevo_atk
        self.df.at[idx, "defense"] = nuevo_def
        self.df.at[idx, "speed"] = nuevo_spd

        print("[OK] Pokémon actualizado.")
        print(self.df.loc[idx].to_dict())

    def eliminar_pokemon(self) -> None:
        """Elimina un pokémon por nombre."""
        print("\n=== Eliminar Pokémon ===")
        nombre = input("Nombre del Pokémon a eliminar: ").strip()
        if self.df.empty:
            print("[ERROR] No hay pokémons cargados.")
            return

        mask = self.df["name"].str.lower() == nombre.lower()
        count = mask.sum()
        if count == 0:
            print("[ERROR] No se encontró ese Pokémon.")
            return

        self.df = self.df[~mask].reset_index(drop=True)
        print(f"[OK] Se eliminaron {count} fila(s) con nombre '{nombre}'.")

    # ===================== BATALLA =====================

    @staticmethod
    def _calcular_daño(row_atacante, row_defensor) -> int:
        """Calcula el daño de un turno de ataque."""
        base = int(row_atacante["attack"]) - int(row_defensor["defense"]) // 2
        return max(1, base)

    def batalla(self) -> None:
        """Simula una batalla 1 vs 1 entre dos pokémons."""
        print("\n=== Batalla Pokémon ===")
        nombre1 = input("Nombre del primer Pokémon: ").strip()
        nombre2 = input("Nombre del segundo Pokémon: ").strip()

        idx1 = self._buscar_indice_por_nombre(nombre1)
        idx2 = self._buscar_indice_por_nombre(nombre2)

        if idx1 is None or idx2 is None:
            print("[ERROR] Uno o ambos pokémons no existen.")
            return

        p1 = self.df.loc[idx1]
        p2 = self.df.loc[idx2]

        hp1 = int(p1["hp"])
        hp2 = int(p2["hp"])

        print(f"\nBatalla entre {p1['name']} ({p1['type_1']}) "
              f"y {p2['name']} ({p2['type_1']})!\n")

        # Comienza el más rápido; si empatan, empieza el primero
        turno_p1 = int(p1["speed"]) >= int(p2["speed"])
        ronda = 1

        while hp1 > 0 and hp2 > 0:
            print(f"--- Ronda {ronda} ---")
            if turno_p1:
                daño = self._calcular_daño(p1, p2)
                hp2 -= daño
                print(f"{p1['name']} ataca a {p2['name']} y causa {daño} de daño. "
                      f"HP restante de {p2['name']}: {max(hp2, 0)}")
            else:
                daño = self._calcular_daño(p2, p1)
                hp1 -= daño
                print(f"{p2['name']} ataca a {p1['name']} y causa {daño} de daño. "
                      f"HP restante de {p1['name']}: {max(hp1, 0)}")

            turno_p1 = not turno_p1
            ronda += 1

        if hp1 <= 0 and hp2 <= 0:
            print("\n¡Empate! Ambos pokémons han sido derrotados.")
        elif hp1 > 0:
            print(f"\n¡{p1['name']} gana la batalla!")
        else:
            print(f"\n¡{p2['name']} gana la batalla!")

    # ===================== MENÚ =====================

    def mostrar_menu(self) -> None:
        """Muestra el menú principal y gestiona las opciones."""
        while True:
            print("\n=== Menú Principal ===")
            print("1. Listar pokémons")
            print("2. Agregar pokémon")
            print("3. Modificar pokémon")
            print("4. Eliminar pokémon")
            print("5. Batalla entre pokémons")
            print("6. Guardar pokémons en CSV")
            print("0. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.listar_pokemons()
            elif opcion == "2":
                self.agregar_pokemon()
            elif opcion == "3":
                self.modificar_pokemon()
            elif opcion == "4":
                self.eliminar_pokemon()
            elif opcion == "5":
                self.batalla()
            elif opcion == "6":
                ruta = input(
                    "Ruta del archivo CSV de salida "
                    "(Enter para 'OG/data/pokemon_salida.csv'): "
                ).strip()
                if ruta == "":
                    ruta = os.path.join("OG", "data", "pokemon_salida.csv")
                self.save_to_csv(ruta)
            elif opcion == "0":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


def main() -> None:
    print("=== Mini Proyecto 2: Batallas entre Pokémons ===")

    # Ruta que se muestra al usuario (relativa a la carpeta donde está el script)
    ruta_mostrada = os.path.relpath(DEFAULT_CSV_PATH, BASE_DIR)

    ruta = input(
        f"Ingrese la ruta del archivo CSV de pokémons "
        f"(o Enter para '{ruta_mostrada}'): "
    ).strip()

    if ruta == "":
        # Usamos la ruta absoluta por defecto
        ruta = DEFAULT_CSV_PATH

    juego = PokemonGame()
    juego.load_from_csv(ruta)
    juego.mostrar_menu()


if __name__ == "__main__":
    main()
