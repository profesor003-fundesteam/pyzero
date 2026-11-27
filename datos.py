import io
from pathlib import Path
from typing import BinaryIO

import pandas as pd

# 1. Funciones de carga de los datos

# Definición de la ruta de datos
RUTA_DATOS = Path(__file__).with_name("data")

# Definición de los dataset demo a utilizar
DEMOS = {
    "Ventas de supermercado": {
        "archivo": "supermarket_sales.csv",
        "descripcion": "1000 ventas de 3 sucursales, enero a marzo de 2019.",
        "perfil": "comercial",
    },
    "Clima diario de Delhi": {
        "archivo": "clima_delhi.csv",
        "descripcion": "Temperatura, humedad, viento y presión diarios.",
        "perfil": "temporal",
    },
    "Factores de rendimiento estudiantil": {
        "archivo": "student_performance.csv",
        "descripcion": "Factores asociados a la nota de 6607 estudiantes.",
        "perfil": "generico",
    },
    "Ventas de supermercado (con errores)": {
        "archivo": "supermarket_sales_con_errores.csv",
        "descripcion": "Copia con errores conocidos para mostrar la limpieza.",
        "perfil": "comercial",
    },
}

# Función ayudante temporal que crea un dataset falso
# TODO: Eliminar cuando se coloquen datos reales
def _ejemplo() -> pd.DataFrame:
    return pd.DataFrame({
        "fecha": pd.to_datetime(["2019-01-05", "2019-01-06", "2019-01-07"]),
        "categoria": ["A", "B", "A"],
        "monto": [10.0, 20.0, 30.0],
    })


def cargar_archivo(archivo: BinaryIO) -> pd.DataFrame:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar el valor de ejemplo por la lectura real de CSV o XLSX
    return _ejemplo()


def cargar_demo(nombre: str) -> pd.DataFrame:
    # TODO(Noel): docstring
    if nombre not in DEMOS:
        raise ValueError(f"No existe el dataset de demostración «{nombre}».")
    # TODO Rol 1: reemplazar el valor de ejemplo por la lectura de RUTA_DATOS / archivo
    return _ejemplo()


# 2. Funciones de revisión de los datos:

def detectar_tipos(df: pd.DataFrame) -> dict[str, str]:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar por las reglas de la sección 14.1
    tipos = {}
    for columna in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[columna]):
            tipos[columna] = "fecha"
        elif pd.api.types.is_numeric_dtype(df[columna]):
            tipos[columna] = "numerica"
        else:
            tipos[columna] = "categorica"
    return tipos


def crear_ficha(df: pd.DataFrame) -> dict:
    # TODO(Noel): docstring
    return {
        "filas": len(df),
        "columnas": len(df.columns),
        "tipos": detectar_tipos(df),
        "nulos": {columna: int(n) for columna, n in df.isna().sum().items()},
        "unicos": {columna: int(n) for columna, n in df.nunique().items()},
        "duplicados": int(df.duplicated().sum()),
        "muestra": df.head(5).to_dict("records"),
    }


def atipicos_iqr(serie: pd.Series) -> pd.Series:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar por el cálculo de Q1 - 1,5·IQR y Q3 + 1,5·IQR
    return pd.Series(False, index=serie.index)


def diagnosticar(df: pd.DataFrame) -> pd.DataFrame:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar por la detección de vacíos, atípicos, negativos y duplicados
    return pd.DataFrame(columns=["fila", "columna", "problema", "valor"])


# 3. Funciones de limpieza de los datos:

def limpiar(
    df: pd.DataFrame, rellenar_mediana: bool = False, eliminar_vacios: bool = False
) -> tuple[pd.DataFrame, list[dict]]:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar por las acciones seguras de la sección 3.5
    return df.copy(), []


# 4. Funciones de filtro y exportación de los datos:

def opciones_filtro(df: pd.DataFrame, tipos: dict[str, str]) -> dict:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar por los rangos y valores de cada columna
    return {"fechas": {}, "categorias": {}, "rangos": {}}


def aplicar_filtros(df: pd.DataFrame, filtros: dict) -> pd.DataFrame:
    # TODO(Noel): docstring
    # TODO Rol 1: reemplazar por el filtrado con el formato de la sección 10
    return df.copy()

def a_csv(df: pd.DataFrame) -> bytes:
    # TODO(Noel): docstring
    return df.to_csv(index=False).encode("utf-8-sig")

def a_excel(df: pd.DataFrame) -> bytes:
    # TODO(Noel): docstring
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine="openpyxl")
    return buffer.getvalue()

