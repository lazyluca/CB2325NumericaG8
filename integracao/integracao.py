import numpy as np
import matplotlib.pyplot as plt
from utils.kahan import soma_kahan


def integral_trapezoidal(funcao, a, b, n=100, mostrar_grafico=False, precisao=None):
    """
    Integra numericamente uma função dada, utilizando uma aproximação trapezoidal.

    Args:
        funcao (callable): Expressão dada para a função.
        a (float): Limite inferior da integral.
        b (float): Limite superior da integral.
        n (int): Número de divisões do intervalo de integração. Valor padrão é 100.
        mostrar_grafico (bool, optional): Define se deve gerar o gráfico ou não. Valor padrão é False.
        precisao (int, optional): Número de casas decimais no resultado retornado.

    Returns:
        float: Valor numérico obtido para a integral arredondado 
        de acordo com a precisão, caso fornecida.
    """

    vals_x = np.linspace(a, b, n + 1)
    y = [funcao(x) for x in vals_x]
    delta = (b - a) / n
    soma_intermediaria = soma_kahan(y[1:-1])
    valor_integral = (delta / 2) * soma_kahan([y[0], 2 * soma_intermediaria, y[-1]])

    if mostrar_grafico:
        grafico(funcao, a, b, s=300, area=valor_integral, n=n)

    if precisao is not None:
        return round(valor_integral, precisao)
    return valor_integral


def integral_simpson(funcao, a, b, n=100, mostrar_grafico=False, precisao=None):
    """
    Integra numericamente uma função dada, utilizando o método de Simpson.

    Args:
        funcao (callable): Expressão dada para a função.
        a (float): Limite inferior da integral.
        b (float): Limite superior da integral.
        n (int): Número de divisões do intervalo de integração. Valor padrão é 100.
        mostrar_grafico (bool, optional): Define se deve gerar o gráfico ou não. Valor padrão é False.
        precisao (int, optional): Número de casas decimais no resultado retornado.

    Raises:
        NotImplementedError: Método Simpson ainda não implementado.
    """

    raise NotImplementedError("Método Simpson ainda não implementado.")


metodos_integral = {
    'Trapezoidal': integral_trapezoidal,
    'Simpson': integral_simpson,
}


def integral(funcao, a, b, n=100, mostrar_grafico=False, precisao=None, metodo='Trapezoidal'):
    """
    Integra numericamente uma função dada, utilizando o método escolhido.

    Args:
        funcao (callable): Expressão dada para a função.
        a (float): Limite inferior da integral.
        b (float): Limite superior da integral.
        n (int): Número de divisões do intervalo de integração. Valor padrão é 100.
        mostrar_grafico (bool, optional): Define se deve gerar o gráfico ou não. Valor padrão é False.
        precisao (int, optional): Número de casas decimais no resultado retornado. Se None, não arredonda.
        metodo (str, optional): Método escolhido para a integração. Valor padrão é 'Trapezoidal'.

    Raises:
        ValueError: Se o método escolhido não estiver entre os implementados.

    Returns:
        float: Valor numérico obtido para a integral arredondado 
        de acordo com a precisão, caso fornecida.
    """

    metodo = metodo.capitalize()

    if metodo not in metodos_integral:
        raise ValueError(
            f"Erro: o método escolhido é inválido. "
            f"Os métodos válidos são {', '.join(metodos_integral.keys())}"
        )

    funcao_escolhida = metodos_integral[metodo]
    return funcao_escolhida(funcao, a, b, n, mostrar_grafico, precisao)

def grafico(funcao, a , b , s, area, n=20):
    ''' dados curva suave '''
    x_curva = np.linspace(a , b , s)
    y_curva = funcao(x_curva)

    '''vértices do trapézio '''
    x_disc = np.linspace(a , b , n+1)
    y_disc = funcao(x_disc)


    plt.plot(x_curva,y_curva, label = "f(x)", color = "blue", alpha = 0.8)
    plt.fill_between(x_disc,y_disc,0, label = "Área da Integral", color = "skyblue", alpha = 0.8)
    plt.vlines(x_disc,0,y_disc, color = "red" , linestyle = "--" , linewidth = 1)
    plt.plot(x_disc,y_disc, color = "red" , linewidth = 1.5)

    plt.title(f"Aproximação da Integral ≈ {area:.4f}")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.legend()
    plt.grid(True, linestyle = ":" , alpha = 0.6)
    

    return plt.show()

funcao = lambda x: np.sin(x)
a = 0
b = np.pi
'''número de pontos para a curva suave'''
# s = 100 
''' n = número de partições de trapézios'''
area = integral(funcao, a, b, n=10, mostrar_grafico=True, metodo='Trapezoidal')
print(area)
# grafico(funcao, a, b, s, area, n=20)