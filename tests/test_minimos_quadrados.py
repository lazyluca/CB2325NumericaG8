"""
Testes unitários para a função em minimos_quadrados.
"""

from cb2325numericag8.aproximacao.minimos_quadrados import AproximacaoPolinomial as ap
import pytest

def test_type_argumentos():
    '''
    Testa os types dos argumentos 1 ('list' ou 'tuple'), 2 ('list' ou 'tuple') e 3 'int'.
    Abscissas, ordenadas e grau respectivamente. Levantando TypeError caso contrário
    '''
    with pytest.raises(TypeError,
                       match="O argumento 1 de AproximacaoPolinomial \(abscissas\) precisa ser 'list' ou 'tuple'"):
        ap(
            abscissas = 2, # argumento 'int'
            ordenadas = [1,2],
            grau = 1
        )
        
    with pytest.raises(TypeError,
                       match="O argumento 2 de AproximacaoPolinomial \(ordenadas\) precisa ser 'list' ou 'tuple'"):
        ap(
            abscissas = [1,2], 
            ordenadas = 2, # argumento 'int'
            grau = 1
        )
    
    with pytest.raises(TypeError,
                       match="O argumento 3 de AproximacaoPolinomial \(grau do polinômio\) precisa ser 'int'"):
        ap(
            abscissas = [1,2], 
            ordenadas = [2,3],
            grau = 0.5 # argumento 'float'
        )
        
def test_listas_vazias():
    """
    Testa se a função levanta um ValueError se as listas estiverem vazias.
    """
    with pytest.raises(ValueError,
                       match="A quantidade de abscissas \(argumento 1\) precisa ser maior que 0"):
        ap(
            abscissas = [], #lista vazia
            ordenadas = [1,2],
            grau = 1
        )
    
    with pytest.raises(ValueError,
                       match="A quantidade de ordenadas \(argumento 2\) precisa ser maior que 0"):
        ap(
            abscissas = [1,2],
            ordenadas = [], #lista vazia
            grau = 1
        )

def test_valor_grau():
    '''
    Testa se grau é um inteiro maior que 0. ValuError caso contrário
    '''
    with pytest.raises(ValueError,
                       match="O grau do polinômio aproximado \(argumento 3\) precisa ser maior ou igual a 1"):
        ap(
            abscissas = [0,1],
            ordenadas = [1,2],
            grau = 0 #grau não positivo
        )
    
    with pytest.raises(ValueError,
                       match="O grau do polinômio aproximado \(argumento 3\) deve ser menor que o número de pontos fornecidos \(argumento 1\)"):
        ap(
            abscissas = [0,1],
            ordenadas = [1,2],
            grau = 2 #grau maior ou igual que len(abscissas)
        )
    
def test_listas_tamanhos_diferentes():
    """
    Testa se a classe levanta um ValueError se as abscissas e ordenadas
    tiverem tamanhos diferentes.
    """
    with pytest.raises(ValueError,
                       match="O número de abscissas \(argumento 1\) é maior que o número de ordenadas \(argumento 2\)"):
        ap(
            abscissas = [0, 1],
            ordenadas = [1]  # Lista com tamanho 1
        )

    with pytest.raises(ValueError,
                       match="O número de abscissas \(argumento 1\) é menor que o número de ordenadas \(argumento 2\)"):
        ap(
            abscissas = [0],  # Lista com tamanho 1
            ordenadas = [1, 2]
        )

def test_chamada_regressao_linear():
    """
    Testa se a função chama regressao linear e retorna coeficientes corretos para y = 2x + 1.
    """
    x = [0, 1, 2, 3]
    y = [1, 3, 5, 7]
    a, b = ap(x, y)
    assert a == pytest.approx(2.0)
    assert b == pytest.approx(1.0)
    
def test_interpolacao_polinomial():
    '''
    Testa se o grau fornecido len(abscissas) - 1 retorna os coeficientes do
    único polinomio que passa pelos pontos
    '''
    x=[-2,-1,0,1,2]
    y=[11,5,3,-1,11]
    a,b,c,d,e = ap(x,y,4) #Esperado [1.0, 1.0, -2.0, -4.0, 3.0]
    assert a == pytest.approx(1.0)
    assert b == pytest.approx(1.0)
    assert c == pytest.approx(-2.0)
    assert d == pytest.approx(-4.0)
    assert e == pytest.approx(3,0)
