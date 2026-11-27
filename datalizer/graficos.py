import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# 1. Funciones de estilo de los gráficos

def _preparar_figura(titulo: str) -> tuple[Figure, Axes]:
    # TODO(Noel): docstring
    # TODO Rol 3: agregar colores y tamaños de letra comunes
    fig = Figure(figsize=(8, 4.5))
    ax = fig.subplots()
    ax.set_title(titulo)
    return fig, ax


# 2. Funciones de validación de los gráficos

def validar_especificacion(espec: dict, tipos: dict[str, str]) -> list[str]:
    # TODO(Noel): docstring
    # TODO Rol 3: reemplazar por las reglas de la sección 4.2
    return []


# 3. Funciones directas de graficación:

def graficar(df: pd.DataFrame, espec: dict) -> Figure:
    # TODO(Noel): docstring
    # TODO Rol 3: reemplazar por los 5 tipos del catálogo
    fig, _ = _preparar_figura(espec.get("titulo", ""))
    return fig


def graficos_especiales(perfil: str, metricas: dict) -> list[Figure]:
    # TODO(Noel): docstring
    # TODO Rol 3: reemplazar por el mapa de calor, el Pareto y la serie con media móvil
    return []


# 4. Funciones de código (Convierten especificaciones de la app en código de Python)

def generar_codigo(espec: dict, nombre_archivo: str = "datos.csv") -> str:
    # TODO(Noel): docstring
    # TODO Rol 3: reemplazar por una plantilla por tipo de gráfico
    return (
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n\n"
        f'df = pd.read_csv("{nombre_archivo}")\n'
    )


# 5. Funciones para el informe en HTML:

def generar_informe(
    nombre: str,
    ficha: dict,
    decision: dict,
    metricas: dict,
    acciones: list[dict],
    figuras: list[Figure],
    interpretacion: dict | None = None,
) -> str:
    # TODO(Noel): docstring
    # TODO Rol 3: reemplazar por el informe completo con tablas y figuras en base64
    return (
        '<!DOCTYPE html><html lang="es"><meta charset="utf-8">'
        f"<h1>Informe DataLizer · {nombre}</h1></html>"
    )

