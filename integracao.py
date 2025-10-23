import numpy as np
import matplotlib.pyplot as plt

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
s = 100 
''' n = número de partições de trapézios'''
area = integral(funcao, a, b, n=100)
print(area)
grafico(funcao, a, b, s, area, n=20)

