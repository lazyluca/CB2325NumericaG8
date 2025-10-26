import pytest

from interpolacao.hermite_interpolator import HermiteInterpolator

def test_listas_tamanhos_diferentes():
    """
    Testa se a classe levanta um ValueError se as listas
    tiverem tamanhos diferentes.
    """
    with pytest.raises(ValueError, match="mesmo tamanho"):
        HermiteInterpolator(
            valorx=[0, 1],
            valory=[1, 2],
            valory_deriv=[1] # Lista com tamanho 1
        )

    with pytest.raises(ValueError, match="mesmo tamanho"):
        HermiteInterpolator(
            valorx=[0, 1],
            valory=[1], # Lista com tamanho 1
            valory_deriv=[1, 0]
        )

def test_listas_vazias():
    """
    Testa se a classe levanta um ValueError se as listas estiverem vazias.
    """
    with pytest.raises(ValueError, match="não podem estar vazias"):
        HermiteInterpolator([], [], [])
