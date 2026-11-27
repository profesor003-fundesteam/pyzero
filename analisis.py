import pandas as pd

# 1. Funciones de estadística:

def estadisticas_descriptivas(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve conteo, media, mediana, desviación, mínimo, Q1, Q3 y máximo por columna numérica."""
    numericas = df.select_dtypes(include=["integer", "floating"], exclude="timedelta")
    cuartiles = numericas.quantile([0.25, 0.75])

    return pd.DataFrame({
        "conteo": numericas.count(),
        "media": numericas.mean(),
        "mediana": numericas.median(),
        "desviacion": numericas.std(),
        "minimo": numericas.min(),
        "q1": cuartiles.loc[0.25],
        "q3": cuartiles.loc[0.75],
        "maximo": numericas.max(),
    }).rename_axis("columna")


def frecuencias(df: pd.DataFrame, columna: str, top: int = 15) -> pd.DataFrame:
    """Devuelve valor, conteo y porcentaje sobre los valores presentes de una columna."""
    if columna not in df.columns:
        raise ValueError(f"No existe la columna «{columna}» para calcular frecuencias.")
    if top < 0:
        raise ValueError("El límite de frecuencias debe ser cero o un número positivo.")

    conteos = df[columna].value_counts(sort=False, dropna=True)
    conteos = conteos.loc[conteos > 0].sort_values(ascending=False, kind="stable")
    tabla = conteos.head(top).rename_axis("valor").reset_index(name="conteo")
    tabla["porcentaje"] = tabla["conteo"] / conteos.sum() * 100
    return tabla


def correlaciones(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve la matriz de Pearson, vacía si hay menos de dos columnas numéricas."""
    numericas = df.select_dtypes(include=["integer", "floating"], exclude="timedelta")
    if numericas.shape[1] < 2:
        return pd.DataFrame()
    return numericas.corr(method="pearson")

# 2. Funciones de agrupación de los datos:

def agrupar(
        df: pd.DataFrame,
        x: str,
        transformacion: str = "ninguna",
        y: str | None = None,
        agregacion: str = "conteo",
        top: int | None = 15,
) -> pd.DataFrame:
    """Función que aplica la transformación de fecha, agrega y devuelve las columnas grupo y valor."""
    # TODO Rol 2: reemplazar el valor del ejemeplo; la firma y las columnas de salida no cambian
    return pd.DataFrame(columns=["grupo","valor"])

# 3. Funciones de perfiles de dominio:

def calcular_generico(df: pd.DataFrame, roles: dict[str,str]) -> dict:
    """Función que aplica el análisis al perfil de dominio genérico"""
    # TODO Rol 2: reemplazar los valores de ejemplo por cálculos reales
    return {
        "descriptivas": pd.DataFrame(),
        "frecuencias": {},
        "correlaciones": pd.DataFrame(),
        "atipicos": pd.DataFrame(columns=["columna","cantidad","porcentaje"])
    }

def graficos_generico(df: pd.DataFrame, roles: dict[str, str]) -> list[dict]:
    """Función que devuelve una lista de especificaciones de gráfico como diccionarios planos
    para el perfil genérico"""
    # TODO Rol 2: reemplazar por las especificaciones de los gráficos fijos
    return [] 

def calcular_temporal(df: pd.DataFrame, roles: dict[str, str]) -> dict:
    """Función que aplica el análisis al perfil de dominio temporal"""
    # TODO Rol 2: reemplazar los valores de ejemplo por cálculos reales
    return {
        "periodo": "D",
        "serie": pd.DataFrame(columns=["fecha","valor","media_movil"]),
        "cambio_porcentual": 0.0,
        "maximo": {"fecha": None, "valor": 0.0},
        "minimo": {"fecha": None, "valor": 0.0},
        "volatilidad": 0.0,
        "pendiente": 0.0,
    }

def graficos_temporal(df: pd.DataFrame, roles: dict[str, str]) -> list[dict]:
    """Función que devuelve una lista de especificaciones de gráfico como diccionarios planos
    para el perfil temporal"""
    # TODO Rol 2: reemplazar por las especificaciones de los gráficos fijos
    return [] 


def calcular_comercial(df: pd.DataFrame, roles: dict[str, str]) -> dict:
    """Función que aplica el análisis al perfil de dominio comercial"""
    # TODO Rol 2: reemplazar los valores de ejemplo por cálculos reales
    return {
        "total": 0.0,
        "ticket_promedio": 0.0,
        "por_categoria": pd.DataFrame(columns=["grupo","valor","participacion"]),
        "pareto": pd.DataFrame(columns=["grupo","valor","porcentaje_acumulado"]),
        "categorias_80": 0,
        "por_dia_semana": None,
        "por_mes": None,
        "por_segmento": None,
    }

def graficos_comercial(df: pd.DataFrame, roles: dict[str, str]) -> list[dict]:
    """Función que devuelve una lista de especificaciones de gráfico como diccionarios planos
    para el perfil comercial"""
    # TODO Rol 2: reemplazar por las especificaciones de los gráficos fijos
    return [] 

# 4. Registro de los perfiles de dominio:

PERFILES = {
        "generico": {
        "roles": {},
        "enfoque_ia": "",
        "calcular": calcular_generico,
        "graficos": graficos_generico,
    },
    "temporal": {
        "roles": {
            "fecha": {"tipo": "fecha", "obligatorio": True},
            "valor": {"tipo": "numerica", "obligatorio": True},
            "volumen": {"tipo": "numerica", "obligatorio": False},
        },
        "enfoque_ia": "",
        "calcular": calcular_temporal,
        "graficos": graficos_temporal,
    },
    "comercial": {
        "roles": {
            "monto": {"tipo": "numerica", "obligatorio": True},
            "categoria": {"tipo": "categorica", "obligatorio": True},
            "fecha": {"tipo": "fecha", "obligatorio": False},
            "cantidad": {"tipo": "numerica", "obligatorio": False},
            "segmento": {"tipo": "categorica", "obligatorio": False},
        },
        "enfoque_ia": "Concentración de ventas y patrones semanales",
        "calcular": calcular_comercial,
        "graficos": graficos_comercial,
    },
}

def calcular_perfil(df: pd.DataFrame, perfil: str, roles:  dict[str, str]) -> dict:
    """Función que calcula las métricas del perfil elegido sobre los datos de trabajo.

    Devuelve el diccionario de métricas del perfil y las métricas opcionales valen None si falta su rol."""
    return PERFILES[perfil]["calcular"](df, roles)

def graficos_perfil(df: pd.DataFrame, perfil: str, roles: dict[str, str]) -> list[dict]:
    """Función que devuelve las especificaciones de los gráficos fijos del perfil elegido."""
    return PERFILES[perfil]["graficos"](df, roles)

