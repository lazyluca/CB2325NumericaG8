import pytest
import numpy as np
# Importa a sua classe do outro arquivo
from PolynomialInterpolator import PolynomialInterpolator 


@pytest.fixture
def p_main():
    """
    Cria um um objeto padrão para ser usado nos testes.
    Usa o seu exemplo principal.
    """
    vetor_x = [0, 1, 2, 3]
    vetor_y = [1, 2, 0, 4]
    return PolynomialInterpolator(vetor_x, vetor_y)



def test_main_evaluation(p_main):
    """
    Testa o valor de avaliação conhecido do exemplo (p(1.5) = 0.8125).
    """
    assert p_main(1.5) == pytest.approx(0.8125)


def test_passes_through_all_points(p_main):
    """
    Testa a propriedade fundamental da interpolação:
    O polinômio deve passar por todos os pontos originais.
    """
    for x, y in zip(p_main.valores_x, p_main.valores_y):
        assert p_main(x) == pytest.approx(y)


def test_constant_function():
    """
    Testa um polinômio de grau 0 (uma linha horizontal).
    """
    p_const = PolynomialInterpolator([0, 10, 20], [5, 5, 5])
    assert p_const(0) == pytest.approx(5)
    assert p_const(5) == pytest.approx(5)
    assert p_const(15) == pytest.approx(5)
    assert p_const(25) == pytest.approx(5)
    assert p_const(1000) == pytest.approx(5)


def test_linear_function():
    """
    Testa um polinômio de grau 1 (a reta, y = 2x + 1).
    """
    p_lin = PolynomialInterpolator([0, 1, 2], [1, 3, 5])
    assert p_lin(1.5) == pytest.approx(4.0)
    assert p_lin(10) == pytest.approx(21.0)
    assert p_lin(-1) == pytest.approx(-1.0)
    assert p_lin(-20) == pytest.approx(-39)
    


def test_quadratic_function():
    """
    Testa um polinômio de grau 2 (uma parábola, y = x^2).
    """
    p_quad = PolynomialInterpolator([0, 1, 2], [0, 1, 4])
    assert p_quad(1.5) == pytest.approx(2.25)
    assert p_quad(-1) == pytest.approx(1.0)


def test_init_raises_errors():
    """
    Testa se o __init__ levanta os erros de input corretos.
    """
    # Listas de tamanhos diferentes
    with pytest.raises(ValueError, match="tamanhos diferentes"):
        PolynomialInterpolator([0, 1], [1, 2, 3])
        
    # Listas vazias
    with pytest.raises(ValueError, match="listas estão vazias"):
        PolynomialInterpolator([], [])
        
    # Inputs que não são listas
    with pytest.raises(TypeError, match="duas listas"):
        PolynomialInterpolator("não é lista", [1, 2])
        
    with pytest.raises(TypeError, match="duas listas"):
        PolynomialInterpolator([1, 2], "não é lista")


def test_repeated_x_value_error(p_main):
    """
    Testa se o cálculo dos coeficientes falha se houver
    valores de 'x' repetidos.
    """
    p_bad = PolynomialInterpolator([0, 1, 1], [1, 2, 3])
    
    # O erro só é levantado quando os coeficientes são calculados
    # (dentro do __call__), por isso testamos p_bad(1.5).
    with pytest.raises(ValueError, match="x contém números repetidos"):
        p_bad(1.5)


def test_coefficient_methods_produce_same_result(p_main):
    """
    Verifica se o seu método iterativo e o método
    recursivo com memoização produzem os mesmos coeficientes.
    """
    # 1. Pega os coeficientes do método iterativo (o padrão)
    coef_ite = p_main._calc_coef_ite()
    
    # 2. Pega os coeficientes do método recursivo
    lista_rec = p_main._calc_coef_rec(
        p_main.valores_x, p_main.valores_y, [p_main.valores_y[0]]
    )
    # Converte para array NumPy para comparação
    coef_rec = np.array(lista_rec[1] + [lista_rec[0]])
    
    # 3. Compara os dois arrays
    np.testing.assert_allclose(coef_ite, coef_rec)
    
    # 4. Checa contra o valor esperado conhecido
    expected_coefs = np.array([1.0, 1.0, -1.5, 1.5])
    np.testing.assert_allclose(coef_ite, expected_coefs)
