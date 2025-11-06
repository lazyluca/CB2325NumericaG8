import numpy as np
import matplotlib.pyplot as plt

def aproximacao_polinomial(abscissas, ordenadas, grau):
    """
    Aproxima os pontos (x, y) por um polinômio de grau n usando mínimos quadrados.

    Parâmetros:
        abscissas (list ou array): coordenadas x
        ordenadas (list ou array): coordenadas y
        grau (int): grau do polinômio
    
    Raises:
        ValueError: Se o grau fornecido não for um número inteiro
        ValueError: Se o grau fornecido for menor que 1
        ValueError: Se as abicissas e as ordenadas tiverem um número diferente de elementos
        ValueError: Se o grau fornecido for maior ou igual à quantidade de abcissas e ordenadas
        
    Retorna:
        list: coeficientes do polinômio aproximado, do maior para o menor grau
    """
    if not isinstance(grau, int):
        raise ValueError(
            "O grau do polinômio aproximado precisa ser um número inteiro"
        )
    
    if grau<1:
        raise ValueError(
            "O grau do polinômio aproximado precisa ser maior ou igual a 1"
        )
    
    if len(abscissas) != len(ordenadas):
        if len(abscissas) < len(ordenadas):
            raise ValueError(
                "O número de abscissas (x) é menor que o número de ordenadas (y)"
            )
        raise ValueError(
            "O número de abscissas (x) é maior que o número de ordenadas (y)"
        )

    if len(abscissas) <= grau:
        raise ValueError(
            "O grau do polinômio aproximado deve ser menor que o número de pontos fornecidos"
        )

    X = []
    for xi in abscissas:
        linha = []
        for j in range(grau, -1, -1):
            linha.append(xi**j)
        X.append(linha)

    X_array = np.array(X)
    y_array = np.array(ordenadas)
    beta = np.linalg.solve(X_array.T @ X_array, X_array.T @ y_array)

    # Transforma beta em uma lista padrão do python e arredonda para 10 casas decimais
    return [float(f"{coef:.10f}") for coef in beta]

def plot_aproximacao(x_pontos, y_pontos, coeficientes, n_suave=500):
    """
    Gera um gráfico dos pontos de entrada e do polinômio de aproximação.

    Args:
        x_pontos (list ou array): Coordenadas x de entrada.
        y_pontos (list ou array): Coordenadas y de entrada.
        coeficientes (list): Coeficientes do polinômio (maior para menor grau).
        n_suave (int, optional): Número de pontos para a curva suave.
                                 Padrão é 500.
    """
    plt.style.use('seaborn-v0_8-darkgrid') 
    
    x_min = np.min(x_pontos)
    x_max = np.max(x_pontos)
    x_suave = np.linspace(x_min, x_max, n_suave)

    y_suave = np.polyval(coeficientes, x_suave)

    #Curva Suvae
    plt.plot(x_suave, y_suave, 
             '-', 
             label="Aproximação por Mínimos Quadrados", 
             color='orange', 
             linewidth=2,
             zorder=2)

    #Pontos de Entrada        
    plt.plot(x_pontos, y_pontos, 
             'o', 
             label="Pontos de Entrada", 
             color='blue', 
             markersize=7, 
             markeredgecolor='black',
             zorder=3)

    plt.title("Gráfico da Aproximação Polinomial (Mínimos Quadrados)", 
              fontsize=14, fontweight='bold')
    plt.xlabel("Eixo X", fontsize=12)
    plt.ylabel("Eixo Y", fontsize=12)
    plt.legend(loc='best', frameon=True, shadow=True)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    """
    Bloco de teste para executar o código.
    """
    x = [-2, -1, 0, 1, 2]
    y = [-3, 0, 3, 0, 9]
    grau = 4  
    n = 500
    
    coeficientes = aproximacao_polinomial(x, y, grau)
    print([float(f"{coef:.2f}") for coef in coeficientes])
    plot_aproximacao(x, y, coeficientes, n)
