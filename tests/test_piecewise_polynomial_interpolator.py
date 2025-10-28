'''
Executar no terminal:
>>> pytest local_do_arquivo

Exemplo:
>>> pytest .\test_Piecewise_Linear_Interpolation.py
'''

import pytest
import numpy as np

from piecewise_polynomial_interpolator import Interpolação_Linear_por_Partes

#Dados Teste 1: 
X_1 = [1,2,3,4,5]
Y_1 = [1,2,3,4]

#Dados Teste 2:
X_2 = [1,2,3,3,4]
Y_2 = [1,2,3,4,5]

def test_listas_de_tamanhos_diferentes():

    with pytest.raises(ValueError, match='As listas devem ter a mesma quantidade de elementos.'):
        objeto = Interpolação_Linear_por_Partes(X_1,Y_1)

def test_abscissas_repetidas():

    with pytest.raises(ValueError, match='A lista de abscissas possui valores repetidos.'):
        objeto = Interpolação_Linear_por_Partes(X_2,Y_2)

'''
OBSERVAÇÃO: A comparação do match retorna verificação correta mesmo com substring.
    
Exemplo:

Se originalmente é  
    match = 'Teste do python'

mas no arquivo 'test_...' testamos
    match = 'o pyth'

ainda assim ele passa pela verificação como correto.
'''
