from google import genai

# 1. Conexión de los modelos de gemini
MODELO = "gemini-3.5-flash"
MODELO_RESPALDO = "gemini-3.1-flash-lite"

def crear_cliente(clave: str) -> genai.Client | None:
    # TODO(Noel): docstring
    # TODO Rol 4: crear el cliente real cuando haya clave
    return None

# 2. Esquemas de validación del modelo de IA:

# TODO Rol 4: modelos de Pydantic de la sección 5.3


# 3. Instrucciones del modelo de IA:

# TODO Rol 4: _leer_instrucciones(seccion) con instrucciones_ia.md


# 4. Validación de los modelos de IA:

# TODO Rol 4: _validar_plan, _filtrar_hallazgos y _metricas_a_texto


# 5. Funciones públicas del modelo

def proponer_perfil(cliente: genai.Client | None, ficha: dict, contexto: str) -> dict:
    # TODO(Noel): docstring
    # TODO Rol 4: reemplazar el valor de ejemplo; si algo falla, se devuelve este genérico
    return {
        "perfil": "generico",
        "roles": {},
        "origen": "generico",
        "confianza": 0.0,
        "justificacion": "",
    }

def interpretar(
    cliente: genai.Client | None,
    decision: dict,
    metricas: dict,
    acciones: list[dict],
    idioma: str,
) -> dict | None:
    # TODO(Noel): docstring
    # TODO Rol 4: reemplazar el valor de ejemplo por la llamada validada
    return None


def traducir_pedido(cliente: genai.Client | None, pedido: str, ficha: dict) -> dict | None:
    # TODO(Noel): docstring
    # TODO Rol 4: reemplazar el valor de ejemplo por la llamada validada
    return None

