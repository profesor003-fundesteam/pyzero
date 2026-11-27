import pandas as pd
from matplotlib.figure import Figure

from graficos import generar_informe, graficar, validar_especificacion


# TODO(Noel): Documentar y probar


ESPEC = {
    "tipo": "barras", "x": "categoria", "transformacion": "ninguna",
    "y": "monto", "agregacion": "suma", "titulo": "Monto por categoría",
}


def _df() -> pd.DataFrame:
    return pd.DataFrame({"categoria": ["A", "B", "A"], "monto": [10.0, 20.0, 30.0]})


def test_graficar_devuelve_una_figura():
    assert isinstance(graficar(_df(), ESPEC), Figure)


def test_validar_devuelve_una_lista():
    tipos = {"categoria": "categorica", "monto": "numerica"}
    assert isinstance(validar_especificacion(ESPEC, tipos), list)


def test_informe_es_html():
    html = generar_informe("Prueba", {}, {}, {}, [], [])
    assert html.startswith("<!DOCTYPE html>")
