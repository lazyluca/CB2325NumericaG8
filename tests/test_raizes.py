#desenvolvimento de testes para o metodo das raizes. 

import pytest
import math
from raizes.raizes import raiz 

#Exemplos de funções
def f1(x):
    return x**2 - 4

def f2(x):
    return math.exp(x) - 2

def f3(x):
    return x**3 - x - 2


def test_metodo_invalido():
    """
    Testa se a função levanta ValueError para método inválido.
    """
    with pytest.raises(ValueError, match="Método não reconhecido"):
        raiz(f1, a=0, b=3, method="nao_existe")

def test_bissecao_intervalo_invalido():
    """
    Testa se o método levanta ValueError quando o intervalo não contém raiz.
    """
    with pytest.raises(ValueError, match="mesmo sinal"):
        raiz(f1, a=3, b=4, tol=1e-6, method="bissecao")

