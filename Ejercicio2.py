"""
Mini Proyecto 2
Sistema de batallas entre Pokémons usando programación orientada a objetos.

- Carga inicial de pokémons desde un archivo CSV.
- Operaciones CRUD: agregar, modificar, eliminar.
- Simulación de batallas por turnos.
"""

import csv
from typing import Dict, Optional


class Pokemon:
    """Representa un Pokémon con estadísticas básicas de combate."""

    def __init__(self, name: str, ptype: str,
                 hp: int, attack: int, defense: int, speed: int) -> None:
        self.name = name
        self.ptype = ptype
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def __str__(self) -> str:
        return (f"{self.name} ({self.ptype}) - "
                f"HP: {self.hp}, ATK: {self.attack}, "
                f"DEF: {self.defense}, SPD: {self.speed}")

    def copy(self) -> "Pokemon":
        """Devuelve una copia simple del Pokémon."""
        return Pokemon(self.name, self.ptype,
                       self.hp, self.attack, self.defense, self.speed)


class PokemonGame:
    """Gestor principal de pokémons y batallas."""

    def __init__(self) -> None:
        self.pokemons: Dict[str, Pokemon] = {}

    @staticmethod
    def _normalizar_clave(clave: str) -> str:
        """Convierte el nombre de columna en minúsculas y sin espacios."""
        return clave.strip().lower().replace(" ", "")

    def load_from_csv(self, ruta: str) -> None:
        """Carga pokémons desde un archivo CSV."""
        try:
            with open(ruta, "r", newline="", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                filas = list(lector)

                if not filas:
                    print("[ADVERTENCIA] El archivo CSV está vacío.")
                    return

                # Mapeo de columnas
                columnas = [self._normalizar_clave(c) for c in lector.fieldnames or []]
                original = lector.fieldnames or []

                def buscar_columna(posibles):
                    for original_name, norm in zip(original, columnas):
                        if norm in posibles:
                            return original_name
                    return None

                col_name = buscar_columna({"name", "nombre"})
                col_type = buscar_columna({"type", "type1", "tipo"})
                col_hp = buscar_columna({"hp"})
                col_atk = buscar_columna({"attack", "atk"})
                col_def = buscar_columna({"defense", "def"})
                col_spd = buscar_columna({"speed", "spd"})

                if not all([col_name, col_type, col_hp, col_atk, col_def, col_spd]):
                    print("[ERROR] No se encontraron todas las columnas necesarias "
                          "(name, type, hp, attack, defense, speed).")
                    return

                self.pokemons.clear()
                cargados = 0
                omitidos = 0

                for fila in filas:
                    try:
                        name = fila[col_name].strip()
                        ptype = fila[col_type].strip()
                        hp = int(float(fila[col_hp]))
                        atk = int(float(fila[col_atk]))
                        defense = int(float(fila[col_def]))
                        speed = int(float(fila[col_spd]))
                    except (KeyError, ValueError, TypeError):
                        omitidos += 1
                        continue

                    if not name:
                        omitidos += 1
                        continue

                    key = name.lower()
                    self.pokemons[key] = Pokemon(name, ptype, hp, atk, defense, speed)
                    cargados += 1

            print(f"[OK] Pokémons cargados desde '{ruta}': {cargados}")
            if omitidos > 0:
                print(f"[INFO] Pokémons omitidos por datos inválidos: {omitidos}")

        except FileNotFoundError:
            print(f"[ERROR] No se encontró el archivo: {ruta}")

    def save_to_csv(self, ruta: str) -> None:
        """Guarda los pokémons actuales en un archivo CSV."""
        fieldnames = ["Name", "Type", "HP", "Attack", "Defense", "Speed"]
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=fieldnames)
            escritor.writeheader()
            for poke in self.pokemons.values():
                escritor.writerow({
                    "Name": poke.name,
                    "Type": poke.ptype,
                    "HP": poke.hp,
                    "Attack": poke.attack,
                    "Defense": poke.defense,
                    "Speed": poke.speed,
                })
        print(f"[OK] Pokémons guardados en '{ruta}'.")

    def _pedir_entero(self, mensaje: str, minimo: int = 1) -> int:
        """Pide un entero al usuario, validando y repitiendo en caso de error."""
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

    def add_pokemon_interactivo(self) -> None:
        """Agrega un nuevo Pokémon pidiendo datos por consola."""
        print("\n=== Agregar nuevo Pokémon ===")
        name = input("Nombre: ").strip()
        if not name:
            print("[ERROR] El nombre no puede estar vacío.")
            return

        key = name.lower()
        if key in self.pokemons:
            print("[ERROR] Ya existe un Pokémon con ese nombre.")
            return

        ptype = input("Tipo: ").strip()
        hp = self._pedir_entero("HP: ", minimo=1)
        atk = self._pedir_entero("Attack: ", minimo=1)
        defense = self._pedir_entero("Defense: ", minimo=0)
        speed = self._pedir_entero("Speed: ", minimo=0)

        self.pokemons[key] = Pokemon(name, ptype, hp, atk, defense, speed)
        print(f"[OK] Pokémon '{name}' agregado.")

    def list_pokemons(self) -> None:
        """Muestra un listado sencillo de todos los pokémons."""
        if not self.pokemons:
            print("[INFO] No hay pokémons cargados.")
            return

        print("\n=== Lista de Pokémons ===")
        for poke in self.pokemons.values():
            print("-", poke)

    def _buscar_pokemon(self, name: str) -> Optional[Pokemon]:
        """Busca un Pokémon por nombre (case-insensitive)."""
        return self.pokemons.get(name.lower())

    def update_pokemon_interactivo(self) -> None:
        """Modifica un Pokémon existente."""
        print("\n=== Modificar Pokémon ===")
        name = input("Nombre del Pokémon a modificar: ").strip()
        poke = self._buscar_pokemon(name)
        if not poke:
            print("[ERROR] No se encontró ese Pokémon.")
            return

        print("Deje el campo vacío para mantener el valor actual.")
        nuevo_nombre = input(f"Nuevo nombre [{poke.name}]: ").strip()
        nuevo_tipo = input(f"Nuevo tipo [{poke.ptype}]: ").strip()

        def leer_opcional_entero(mensaje, actual):
            texto = input(mensaje).strip()
            if texto == "":
                return actual
            try:
                val = int(texto)
                return val
            except ValueError:
                print("Valor no válido. Se mantiene el actual.")
                return actual

        nuevo_hp = leer_opcional_entero(f"Nuevo HP [{poke.hp}]: ", poke.hp)
        nuevo_atk = leer_opcional_entero(f"Nuevo Attack [{poke.attack}]: ", poke.attack)
        nuevo_def = leer_opcional_entero(f"Nuevo Defense [{poke.defense}]: ", poke.defense)
        nuevo_spd = leer_opcional_entero(f"Nuevo Speed [{poke.speed}]: ", poke.speed)

        # Actualizar
        old_key = poke.name.lower()
        if nuevo_nombre:
            poke.name = nuevo_nombre
        if nuevo_tipo:
            poke.ptype = nuevo_tipo
        poke.hp = nuevo_hp
        poke.attack = nuevo_atk
        poke.defense = nuevo_def
        poke.speed = nuevo_spd

        # Actualizar clave del diccionario si cambió el nombre
        if poke.name.lower() != old_key:
            self.pokemons.pop(old_key, None)
            self.pokemons[poke.name.lower()] = poke

        print("[OK] Pokémon actualizado:")
        print("-", poke)

    def delete_pokemon_interactivo(self) -> None:
        """Elimina un Pokémon por nombre."""
        print("\n=== Eliminar Pokémon ===")
        name = input("Nombre del Pokémon a eliminar: ").strip()
        key = name.lower()
        if key in self.pokemons:
            self.pokemons.pop(key)
            print(f"[OK] Pokémon '{name}' eliminado.")
        else:
            print("[ERROR] No se encontró ese Pokémon.")

    @staticmethod
    def _calcular_daño(atacante: Pokemon, defensor: Pokemon) -> int:
        """Calcula el daño de un ataque de atacante a defensor."""
        base = atacante.attack - defensor.defense // 2
        return max(1, base)

    def battle_interactiva(self) -> None:
        """Realiza una batalla interactiva entre dos pokémons."""
        print("\n=== Batalla Pokémon ===")
        name1 = input("Nombre del primer Pokémon: ").strip()
        name2 = input("Nombre del segundo Pokémon: ").strip()

        p1 = self._buscar_pokemon(name1)
        p2 = self._buscar_pokemon(name2)

        if not p1 or not p2:
            print("[ERROR] Uno o ambos pokémons no existen.")
            return

        # Copias para no modificar los originales
        c1 = p1.copy()
        c2 = p2.copy()

        print(f"\nBatalla entre {c1.name} y {c2.name}!\n")

        # Inicia el más rápido; si empatan, comienza el primero
        turno_p1 = c1.speed >= c2.speed
        ronda = 1

        while c1.hp > 0 and c2.hp > 0:
            print(f"--- Ronda {ronda} ---")
            if turno_p1:
                daño = self._calcular_daño(c1, c2)
                c2.hp -= daño
                print(f"{c1.name} ataca a {c2.name} y causa {daño} de daño. "
                      f"HP restante de {c2.name}: {max(c2.hp, 0)}")
            else:
                daño = self._calcular_daño(c2, c1)
                c1.hp -= daño
                print(f"{c2.name} ataca a {c1.name} y causa {daño} de daño. "
                      f"HP restante de {c1.name}: {max(c1.hp, 0)}")

            turno_p1 = not turno_p1
            ronda += 1

        if c1.hp <= 0 and c2.hp <= 0:
            print("\n¡Empate! Ambos pokémons han sido derrotados.")
        elif c1.hp > 0:
            print(f"\n¡{c1.name} gana la batalla!")
        else:
            print(f"\n¡{c2.name} gana la batalla!")

    def mostrar_menu(self) -> None:
        """Muestra el menú principal en un bucle hasta que el usuario salga."""
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
                self.list_pokemons()
            elif opcion == "2":
                self.add_pokemon_interactivo()
            elif opcion == "3":
                self.update_pokemon_interactivo()
            elif opcion == "4":
                self.delete_pokemon_interactivo()
            elif opcion == "5":
                self.battle_interactiva()
            elif opcion == "6":
                ruta = input("Ruta del archivo CSV de salida "
                             "(Enter para 'OG/data/pokemon.csv'): ").strip()
                if ruta == "":
                    ruta = "OG/data/pokemon.csv"
                self.save_to_csv(ruta)
            elif opcion == "0":
                print("Saliendo del juego. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


def main() -> None:
    print("=== Mini Proyecto 2: Batallas entre Pokémons ===")
    ruta_por_defecto = "OG/data/pokemon.csv"
    ruta = input(
        f"Ingrese la ruta del archivo CSV de pokémons "
        f"(o Enter para '{ruta_por_defecto}'): "
    ).strip()
    if ruta == "":
        ruta = ruta_por_defecto

    juego = PokemonGame()
    juego.load_from_csv(ruta)
    juego.mostrar_menu()


if __name__ == "__main__":
    main()