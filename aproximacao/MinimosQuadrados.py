import numpy as np


def aproximacao_polinomial(abscissas, ordenadas, grau):
    """
    Aproxima os pontos (x, y) por um polinômio de grau n usando mínimos quadrados.

    Parâmetros:
        abscissas (list ou array): coordenadas x
        ordenadas (list ou array): coordenadas y
        grau (int): grau do polinômio

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
    y_array = np.array(y)
    beta = np.linalg.solve(X_array.T @ X_array, X_array.T @ y_array)

    # arredonda para 10 casas decimais
    return [float(f"{coef:.10f}") for coef in beta]

if __name__ == "__main__":
    
    x = [-2, -1, 0, 1, 2]
    y = [-3, 0, 3, 0, 9]

    coeficientes = aproximacao_polinomial(x, y, 4)

    # arredonda para 2 casas decimais na impressão
    print([float(f"{coef:.2f}") for coef in coeficientes])

