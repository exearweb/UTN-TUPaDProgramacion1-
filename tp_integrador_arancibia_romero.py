"""
TPI - Programación 1
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

Requisitos cubiertos:
- Lectura desde CSV (nombre, poblacion, superficie, continente)
- Búsqueda por nombre (parcial o exacta)
- Filtros: continente / rango de población / rango de superficie
- Ordenamientos: nombre / población / superficie (asc/desc)
- Estadísticas: mayor/menor población, promedios, cantidad por continente
- Validaciones de entrada + manejo básico de errores
- Código modular (una función = una responsabilidad)
"""

import paises.csv
import os
from typing import List, Dict, Optional, Tuple
# Tipos 
Pais = Dict[str, object]  # {"nombre": str, "poblacion": in|t, "superficie": int, "continente": str}

# Utilidades de impresión
def imprimir_linea(ancho: int = 80, char: str = "-") -> None:
    print(char * ancho)

def formatear_entero(n: int) -> str:
    """Devuelve el entero con separadores de miles para mejor lectura."""
    return f"{n:,}".replace(",", ".")

def mostrar_tabla(paises: List[Pais]) -> None:
    """Muestra una tabla simple y legible en consola."""
    if not paises:
        print("No hay datos para mostrar.")
        return
    # Anchos de columnas calculados
    col_n = max(6, max(len(p["nombre"]) for p in paises))  # "Nombre"
    col_c = max(10, max(len(p["continente"]) for p in paises))  # "Continente"
    col_p = max(10, max(len(formatear_entero(p["poblacion"])) for p in paises))  # "Población"
    col_s = max(10, max(len(formatear_entero(p["superficie"])) for p in paises))  # "Superficie"
    header = f'{"Nombre":<{col_n}}  {"Continente":<{col_c}}  {"Población":>{col_p}}  {"Superficie (km²)":>{col_s}}'
    imprimir_linea(len(header), "=")
    print(header)
    imprimir_linea(len(header), "-")
    for p in paises:
        print(
            f'{p["nombre"]:<{col_n}}  '
            f'{p["continente"]:<{col_c}}  '
            f'{formatear_entero(p["poblacion"]):>{col_p}}  '
            f'{formatear_entero(p["superficie"]):>{col_s}}'
        )
    imprimir_linea(len(header), "=")

# ---------- Lectura y validación de CSV ----------
def parsear_entero(valor: str, campo: str, fila_nro: int) -> Optional[int]:
    try:
        v = int(valor)
        if v < 0:
            raise ValueError
        return v
    except Exception:
        print(f"[AVISO] Fila {fila_nro}: valor inválido en '{campo}' -> '{valor}'. Fila omitida.")
        return None

def leer_csv(ruta: str) -> List[Pais]:
    """
    Lee paises.csv y devuelve una lista de diccionarios tipados.
    Omite filas con errores de formato y muestra avisos.
    """
    paises: List[Pais] = []
    if not os.path.exists(ruta):
        print(f"[ERROR] No se encontró el archivo CSV en: {ruta}")
        return paises

    with open(ruta, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        requeridos = {"nombre", "poblacion", "superficie", "continente"}
        if set(lector.fieldnames or []) != requeridos:
            print("[ERROR] Encabezados inválidos. Se requieren exactamente: nombre,poblacion,superficie,continente")
            return paises

        for i, fila in enumerate(lector, start=2):  # comienza en 2 por la cabecera
            nombre = (fila.get("nombre") or "").strip()
            continente = (fila.get("continente") or "").strip()
            if not nombre or not continente:
                print(f"[AVISO] Fila {i}: nombre/continente vacío. Fila omitida.")
                continue

            p = parsear_entero((fila.get("poblacion") or "").strip(), "poblacion", i)
            s = parsear_entero((fila.get("superficie") or "").strip(), "superficie", i)
            if p is None or s is None:
                continue

            paises.append({
                "nombre": nombre,
                "poblacion": p,
                "superficie": s,
                "continente": continente
            })

    print(f"[OK] Se cargaron {len(paises)} países desde '{ruta}'.")
    return paises

# ---------- Búsqueda ----------
def buscar_pais(nombre_parcial: str, paises: List[Pais]) -> List[Pais]:
    q = nombre_parcial.casefold().strip()
    return [p for p in paises if q in p["nombre"].casefold()]

# ---------- Filtros ----------
def filtrar_por_continente(continente: str, paises: List[Pais]) -> List[Pais]:
    q = continente.casefold().strip()
    return [p for p in paises if p["continente"].casefold() == q]

def filtrar_por_rango(
    paises: List[Pais],
    campo: str,
    minimo: Optional[int],
    maximo: Optional[int],
) -> List[Pais]:
    """
    campo ∈ {"poblacion", "superficie"}
    Rangos inclusivos. None significa sin límite.
    """
    res: List[Pais] = []
    for p in paises:
        v = int(p[campo])  # seguro int por tipado de carga
        if minimo is not None and v < minimo:
            continue
        if maximo is not None and v > maximo:
            continue
        res.append(p)
    return res

# ---------- Ordenamientos ----------
def ordenar_por_clave(paises: List[Pais], clave: str, descendente: bool = False) -> List[Pais]:
    """
    clave ∈ {"nombre", "poblacion", "superficie"}
    """
    if clave == "nombre":
        return sorted(paises, key=lambda p: p["nombre"].casefold(), reverse=descendente)
    return sorted(paises, key=lambda p: int(p[clave]), reverse=descendente)

# ---------- Estadísticas ----------
def estadisticas(paises: List[Pais]) -> Dict[str, object]:
    if not paises:
        return {}
    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)
    # Conteo por continente
    por_cont = {}
    for p in paises:
        c = p["continente"]
        por_cont[c] = por_cont.get(c, 0) + 1

    return {
        "mayor_poblacion": mayor,
        "menor_poblacion": menor,
        "promedio_poblacion": prom_pob,
        "promedio_superficie": prom_sup,
        "cantidad_por_continente": por_cont
    }

def mostrar_estadisticas(paises: List[Pais]) -> None:
    e = estadisticas(paises)
    if not e:
        print("No hay datos para calcular estadísticas.")
        return
    imprimir_linea()
    print("📊 ESTADÍSTICAS")
    imprimir_linea()
    print(f"- País con mayor población: {e['mayor_poblacion']['nombre']} "
          f"({formatear_entero(e['mayor_poblacion']['poblacion'])})")
    print(f"- País con menor población: {e['menor_poblacion']['nombre']} "
          f"({formatear_entero(e['menor_poblacion']['poblacion'])})")
    print(f"- Promedio de población: {formatear_entero(int(e['promedio_poblacion']))}")
    print(f"- Promedio de superficie (km²): {formatear_entero(int(e['promedio_superficie']))}")
    print("- Cantidad de países por continente:")
    for cont, cant in e["cantidad_por_continente"].items():
        print(f"  • {cont}: {cant}")
    imprimir_linea()

# ---------- Inputs seguros ----------
def pedir_opcion(msg: str, opciones_validas: List[str]) -> str:
    while True:
        op = input(msg).strip()
        if op in opciones_validas:
            return op
        print("Opción inválida. Intente nuevamente.")

def pedir_entero_opcional(msg: str) -> Optional[int]:
    """
    Permite Enter para dejar vacío (None). Si se ingresa algo, debe ser entero >= 0.
    """
    while True:
        dato = input(msg).strip()
        if dato == "":
            return None
        try:
            n = int(dato)
            if n < 0:
                raise ValueError
            return n
        except Exception:
            print("Valor inválido. Ingrese un entero >= 0 o vacío para omitir.")

# ---------- Menús ----------
def menu_principal() -> str:
    imprimir_linea()
    print("MENÚ PRINCIPAL")
    imprimir_linea()
    print("1) Buscar país por nombre")
    print("2) Filtrar países")
    print("3) Ordenar países")
    print("4) Mostrar estadísticas")
    print("5) Mostrar todos")
    print("0) Salir")
    return pedir_opcion("Seleccione una opción: ", list("123450"))

def menu_filtros() -> str:
    imprimir_linea()
    print("FILTROS")
    imprimir_linea()
    print("1) Por continente")
    print("2) Por rango de población")
    print("3) Por rango de superficie")
    print("0) Volver")
    return pedir_opcion("Seleccione una opción: ", list("1230"))

def menu_orden() -> Tuple[str, bool]:
    imprimir_linea()
    print("ORDENAMIENTOS")
    imprimir_linea()
    print("1) Nombre")
    print("2) Población")
    print("3) Superficie")
    op = pedir_opcion("Seleccione una opción: ", list("123"))
    desc = pedir_opcion("¿Descendente? (s/n): ", ["s", "n"]) == "s"
    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    return claves[op], desc

# ---------- Control ----------
def loop(ruta_csv: str = "paises.csv") -> None:
    paises = leer_csv(ruta_csv)
    if not paises:
        print("No hay datos. Revise el CSV e intente nuevamente.")
        return

    # "vista" actual para aplicar filtros y orden sin perder los datos originales
    vista = list(paises)

    while True:
        op = menu_principal()

        if op == "0":
            print("¡Hasta luego!")
            break

        elif op == "5":
            mostrar_tabla(vista)

        elif op == "1":
            q = input("Ingrese nombre (total o parcial): ").strip()
            res = buscar_pais(q, vista)
            if res:
                mostrar_tabla(res)
            else:
                print("No se encontraron países que coincidan con la búsqueda.")

        elif op == "2":
            while True:
                of = menu_filtros()
                if of == "0":
                    break
                if of == "1":
                    cont = input("Continente (ej.: América, Europa, Asia, África, Oceanía): ").strip()
                    res = filtrar_por_continente(cont, vista)
                    if res:
                        vista = res
                        print(f"[OK] Filtro por continente aplicado. {len(vista)} países.")
                        mostrar_tabla(vista)
                    else:
                        print("No hubo coincidencias para ese continente.")
                elif of == "2":
                    mn = pedir_entero_opcional("Población mínima (Enter para omitir): ")
                    mx = pedir_entero_opcional("Población máxima (Enter para omitir): ")
                    res = filtrar_por_rango(vista, "poblacion", mn, mx)
                    if res:
                        vista = res
                        print(f"[OK] Filtro por población aplicado. {len(vista)} países.")
                        mostrar_tabla(vista)
                    else:
                        print("No hubo coincidencias para ese rango de población.")
                elif of == "3":
                    mn = pedir_entero_opcional("Superficie mínima km² (Enter para omitir): ")
                    mx = pedir_entero_opcional("Superficie máxima km² (Enter para omitir): ")
                    res = filtrar_por_rango(vista, "superficie", mn, mx)
                    if res:
                        vista = res
                        print(f"[OK] Filtro por superficie aplicado. {len(vista)} países.")
                        mostrar_tabla(vista)
                    else:
                        print("No hubo coincidencias para ese rango de superficie.")

        elif op == "3":
            clave, desc = menu_orden()
            vista = ordenar_por_clave(vista, clave, desc)
            print(f"[OK] Vista ordenada por {clave} ({'desc' if desc else 'asc'}).")
            mostrar_tabla(vista)

        elif op == "4":
            mostrar_estadisticas(vista)

        # Pequeño submenú para restaurar la vista si el usuario lo desea
        if op in {"2", "3"}:
            r = pedir_opcion("¿Restaurar vista original (s/n)? ", ["s", "n"])
            if r == "s":
                vista = list(paises)
                print("[OK] Vista restaurada a los datos originales.")

# ---------- Punto de entrada ----------
if __name__ == "__main__":
    # Cambiá "paises.csv" si usás otro nombre/ruta
    loop("paises.csv")




