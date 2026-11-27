from ia import crear_cliente, interpretar, proponer_perfil, traducir_pedido



# TODO(Noel): Documentar y probar


def test_sin_clave_no_hay_cliente():
    assert crear_cliente("") is None


def test_sin_cliente_el_perfil_es_generico():
    decision = proponer_perfil(None, {}, "")
    assert decision["perfil"] == "generico"
    assert decision["origen"] == "generico"


def test_sin_cliente_las_llamadas_devuelven_none():
    assert interpretar(None, {}, {}, [], "es") is None
    assert traducir_pedido(None, "ventas por mes", {}) is None
