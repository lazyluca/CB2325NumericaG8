'''implementação do método das raízes'''

def raiz(funcao, a, b, tol, method):

    if method == "bissecao":
        return Bissecao(funcao,a,b,tol)

    elif method == "secante":
        return Secante(funcao,a,b,tol)

    elif method == "newton_raphson":
        return Newton(funcao,a,b,tol)

    else:
        #Exibir mensagem de erro: "método não reconhecido"    
        pass
        

    def Bissecao(funcao,a,b,tol):
        '''parametros: função, intervalos e tolerância'''
        '''retornar erro se na verificação de sinais der f(a).f(b)>0, ou seja, raiz não está entre esse intervalo, se der certo(<0), continua'''
        '''estrutura principal: loop até encontrar a raiz (valor encontrado menor que a tolerância) ou o número de iterações ultrapassar o esperado(prevenir loop infinito se algo der errado)'''
        ''' ideia: calcular o ponto médio do intervalo, analisar os sinais, modificar o intervalo para o ponto medio até a ou b e repetir...'''
        ''' ou seja: Verificar Sinais(f(a).f(b)<0) -> Loop -> Calcular Meio -> Salvar Meio -> Decidir Nova Metade -> Repetir até encontrar uma raiz'''
       
        pass

    def Secante(funcao,a,b,tol):
        #Implementar o Método da Secante
        pass

    def Newton(funcao,a,b,tol):
        #Implementar o Método de Newton-Raphson
        pass
