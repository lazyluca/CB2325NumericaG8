from integracao.kahan import soma_kahan

def erro_absoluto(v_real, v_aproximado):
    '''
    Retorna o erro absoluto para um valor de referência dado e um valor obtido.

    Args:
        v_real (float): Valor teórico de referência.
        v_aproximado (float): Valor obtido para comparação.

    Returns:
        float: Erro absoluto.
    '''
    try:
        v_real = float(v_real)
        v_aproximado = float(v_aproximado)
    except ValueError:
        raise ValueError("Erro: os valores real e aproximado devem ser numéricos.")
    erro = abs(v_real - v_aproximado)
    return float(f"{erro:.4g}")

def erro_relativo(v_real, v_aproximado):
    '''
    Retorna o erro relativo para um valor de referência dado e um valor obtido.

    Args:
        v_real (float): Valor teórico de referência, deve ser diferente de zero.
        v_aproximado (float): Valor obtido para comparação.

    Returns:
        float: Erro relativo.
    '''
    try:
        v_real = float(v_real)
        v_aproximado = float(v_aproximado)
    except ValueError:
        raise ValueError("Erro: os valores real e aproximado devem ser numéricos.")
    if v_real == 0:
        raise ValueError("Erro: o valor real não pode ser zero para o cálculo do erro relativo.")
    erro = abs((v_real-v_aproximado)/v_real)
    return float(f"{erro:.4g}")

def erro_quadratico_medio(lista_real, lista_aproximada):
    '''
    Retorna o erro quadrático médio para uma lista de valores de referência e uma lista de valores obtidos.

    Args:
        lista_real (list): Valores teóricos de referência.
        lista_aproximada (list): Valores obtidos para comparação.

    Returns:
        float: Erro quadrático médio.
    '''
    if len(lista_real) != len(lista_aproximada):
        raise ValueError("Erro: as listas devem possuir a mesma quantidade de elementos.")
    n = len(lista_real)
    if n == 0:
        raise ValueError("Erro: as listas não podem ser vazias.")
    try:
        valores_reais = [float(v) for v in lista_real]
        valores_aproximados = [float(v) for v in lista_aproximada]
    except ValueError:
        raise ValueError("Erro: todos os valores das listas devem ser numéricos.")
    lista_erros_quadraticos = [(real - aproximado)**2 for real, aproximado in zip(valores_reais, valores_aproximados)]
    eqm = soma_kahan(lista_erros_quadraticos)/n
    return float(f"{eqm:.4g}")