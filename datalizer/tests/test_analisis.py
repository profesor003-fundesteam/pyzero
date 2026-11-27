import pandas as pd

from analisis import PERFILES, agrupar, calcular_perfil

# TODO(Noel): Documentar y probar

def _df() -> pd.DataFrame:
    return pd.DataFrame({"categoria": ["A", "B", "A"], "monto": [10.0, 20.0, 30.0]})


def test_perfiles_tiene_los_tres_perfiles():
    assert set(PERFILES) == {"generico", "temporal", "comercial"}
    for perfil in PERFILES.values():
        assert set(perfil) == {"roles", "enfoque_ia", "calcular", "graficos"}


def test_agrupar_devuelve_grupo_y_valor():
    tabla = agrupar(_df(), "categoria", y="monto", agregacion="suma")
    assert list(tabla.columns) == ["grupo", "valor"]


def test_comercial_devuelve_todas_sus_claves():
    roles = {"monto": "monto", "categoria": "categoria"}
    metricas = calcular_perfil(_df(), "comercial", roles)
    assert set(metricas) == {
        "total", "ticket_promedio", "por_categoria", "pareto",
        "categorias_80", "por_dia_semana", "por_mes", "por_segmento",
    }
