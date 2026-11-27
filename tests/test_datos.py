import pandas as pd
import pytest

from datos import DEMOS, a_csv, a_excel, cargar_demo, crear_ficha, limpiar


# TODO(Noel): Documentar y probar


def _df() -> pd.DataFrame:
    return pd.DataFrame({"categoria": ["A", "B", "A"], "monto": [10.0, 20.0, 30.0]})


def test_galeria_tiene_cuatro_datasets():
    assert len(DEMOS) == 4


def test_cargar_demo_rechaza_un_nombre_desconocido():
    with pytest.raises(ValueError):
        cargar_demo("No existe")


def test_limpiar_no_modifica_el_original():
    df = _df()
    copia = df.copy()
    limpio, acciones = limpiar(df)
    pd.testing.assert_frame_equal(df, copia)
    assert isinstance(limpio, pd.DataFrame)
    assert isinstance(acciones, list)


def test_ficha_tiene_las_claves_del_formato():
    ficha = crear_ficha(_df())
    assert set(ficha) == {"filas", "columnas", "tipos", "nulos", "unicos", "duplicados", "muestra"}


def test_exportaciones_devuelven_bytes():
    assert isinstance(a_csv(_df()), bytes)
    assert isinstance(a_excel(_df()), bytes)
