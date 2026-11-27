import pandas as pd

# 1. Funciones de estadística:

def estadisticas_descriptivas(df: pd.DataFrame) -> pd.DataFrame:
    """Función que utiliza pandas para aplicar medidas de estadística descriptiva
    generales a un DataFrame con el propósito de analizarlo y describirlo."""
    # TODO Rol 2: reemplazar por conteo, media, mediana, desviación estándar, mínimo, Q1 (cuartil 1), Q3 (cuartil 3) y máximo
    return df.describe()

def frecuencias(df: pd.DataFrame, columna: str, top: int = 15) -> pd.DataFrame:
    """Función encargada de establecer una tabla de frecuencias para el dataframe en cuestión
    con el propósito de analizarlo."""
    # TODO Rol 2: reemplazar el valor del ejemplo por el cálculo real
    return pd.DataFrame(columns=["valor","conteo","porcentaje"])

def correlaciones(df: pd.DataFrame) -> pd.DataFrame:
    """Función encargada de generar una matriz de correlaciones a partir de un DataFrame"""
    # TODO Rol 2: reemplazar por la matriz de Pearson de las columnas numéricas
    return pd.DataFrame()

# 2. Funciones de agrupación de los datos:

def agrupar(
        df: pd.DataFrame,
        x: str,
        transformacion: str = "ninguna",
        y: str | None = None,
        agregacion: str = "conteo",
        top: int | None = 15,
) -> pd.DataFrame:
    """Devuelve las columnas grupo y valor después de transformar y agregar."""
    operaciones = {"suma": "sum", "promedio": "mean", "mediana": "median"}
    if x not in df.columns:
        raise ValueError(f"No existe la columna «{x}» para agrupar.")
    if transformacion not in ("ninguna", "dia_semana", "mes", "anio"):
        raise ValueError(f"Transformación de fecha desconocida: «{transformacion}».")
    if agregacion not in operaciones and agregacion not in ("conteo", "ninguna"):
        raise ValueError(f"Agregación desconocida: «{agregacion}».")
    if top is not None and top < 0:
        raise ValueError("El límite de categorías debe ser cero o un número positivo.")

    grupo = df[x]
    es_fecha = pd.api.types.is_datetime64_any_dtype(grupo)
    if transformacion != "ninguna":
        grupo = _transformar_fecha(grupo, transformacion)
        es_fecha = True

    datos = grupo.to_frame(name="grupo")
    if agregacion != "conteo":
        if y is None or y not in df.columns:
            raise ValueError("Selecciona una columna de valores existente.")
        if not pd.api.types.is_numeric_dtype(df[y]):
            raise ValueError(f"La columna de valores «{y}» debe ser numérica.")
        datos["valor"] = df[y]
    datos = datos.dropna()

    if agregacion == "ninguna":
        tabla = datos
    else:
        grupos = datos.groupby("grupo", sort=False, observed=True)
        if agregacion == "conteo":
            valores = grupos.size()
        else:
            valores = grupos["valor"].agg(operaciones[agregacion])
        tabla = valores.reset_index(name="valor")

    if es_fecha:
        tabla = tabla.sort_values("grupo", kind="stable")
        if transformacion == "dia_semana":
            dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
            tabla["grupo"] = tabla["grupo"].map(dict(enumerate(dias)))
    else:
        tabla = tabla.sort_values("valor", ascending=False, kind="stable")
        if top is not None:
            categorias = tabla["grupo"].drop_duplicates().head(top)
            tabla = tabla.loc[tabla["grupo"].isin(categorias)]

    return tabla.reset_index(drop=True)


def _transformar_fecha(columna: pd.Series, transformacion: str) -> pd.Series:
    """Obtiene el día de la semana, el mes o el año de cada fecha."""
    mensaje = f"La columna «{columna.name}» debe contener fechas válidas."
    if pd.api.types.is_numeric_dtype(columna):
        raise ValueError(mensaje)

    try:
        fechas = pd.to_datetime(columna, errors="coerce", format="mixed")
    except (TypeError, ValueError) as error:
        raise ValueError(mensaje) from error
    if fechas.isna().all() and columna.notna().any():
        raise ValueError(mensaje)

    if transformacion == "dia_semana":
        return fechas.dt.dayofweek
    if transformacion == "mes":
        return fechas.dt.strftime("%Y-%m")
    return fechas.dt.year.astype("Int64")

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

