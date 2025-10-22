import numpy as np

def integral(funcao, a, b, n=100):
    '''
    Integra numericamente uma função dada, utilizando uma aproximação trapezoidal.

    Args:
        funcao (callable): Expressão dada para a função.
        a (float): Limite inferior da integral.
        b (float): Limite superior da integral.
        n (int): Número de divisões do intervalo de integração.

    Returns:
        float: Valor numérico obtido para a integral.
    '''

    vals_x = np.linspace(a, b, n+1)
    y = [funcao(x) for x in vals_x]
    delta = (b-a)/n
    valor_integral = (delta/2)*(y[0] + 2*np.sum(y[1:-1]) + y[-1])

    return float(f"{valor_integral:.4g}")