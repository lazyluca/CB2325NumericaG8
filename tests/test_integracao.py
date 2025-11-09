import pytest
import numpy as np
from cb2325numericag8.integracao.integracao import integral, integral_trapezoidal, integral_simpson

funcao1 = lambda x: np.sin(x)
funcao2 = lambda x: 1 / x
funcao3 = lambda x: x**2

def test_trapezoidal_funcao1():
    pass

def test_simpson_funcao1():
    pass

def test_trapezoidal_funcao2():
    pass

def test_simpson_funcao2():
    pass

def test_metodo_invalido1():
    """
    Testa se retorna erro ao tentar utilizar um método inválido.
    """
    with pytest.raises(ValueError, match="método escolhido é inválido"):
        integral(funcao1, 0, np.pi, metodo="invalido")

def test_metodo_invalido2():
    """
    Testa se retorna erro ao não utilizar string na escolha de método.
    """
    with pytest.raises(ValueError, match="o método informado deve ser uma string"):
        integral(funcao1, 0, np.pi, metodo=123)

def test_intervalo_invalido():
    """
    Testa se ocorre erro ao tentar avaliar uma função não definida em um ponto.
    """
    with pytest.warns(RuntimeWarning, match="divide by zero"):
        with pytest.raises(ValueError, match="não definida"):
            integral(funcao2, -1, 1, metodo="Trapezoidal")

    with pytest.warns(RuntimeWarning, match="divide by zero"):
        with pytest.raises(ValueError, match="não definida"):
            integral(funcao2, -1, 1, metodo="Simpson")

def test_simpson_corrige_n_impar(capsys):
    """
    Testa se o método de Simpson força um número ímpar de subdivisões.
    """
    resultado = integral_simpson(funcao1, 0, np.pi, n=19)
    saida = capsys.readouterr().out
    assert "Ajustado para 20" in saida
    assert np.isclose(resultado, 2.0, rtol=1e-4)