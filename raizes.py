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
        #Implementar o Método da Bisseção
        pass

    def Secante(funcao,a,b,tol):
        #Implementar o Método da Secante
        pass

    def Newton(funcao,a,b,tol):
        #Implementar o Método de Newton-Raphson
        pass