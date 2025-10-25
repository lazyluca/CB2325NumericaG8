def erro_absoluto(v_real, v_aproximado):
    '''
    Retorna o erro absoluto para um valor de referência dado e um valor obtido.

    Args:
        v_real (float): Valor teórico de referência.
        v_aproximado (float): Valor obtido para comparação.

    Returns:
        float: Erro absoluto.
    '''
    erro = abs(v_real - v_aproximado)
    return float(f"{erro:.4g}")

def erro_relativo(v_real, v_aproximado):
    '''
    Retorna o erro relativo para um valor de referência dado e um valor obtido.

    Args:
        v_real (float): Valor teórico de referência.
        v_aproximado (float): Valor obtido para comparação.

    Returns:
        float: Erro relativo.
    '''
    erro = abs((v_real-v_aproximado)/v_real)
    return float(f"{erro:.4g}")