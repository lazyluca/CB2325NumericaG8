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
    f_a=funcao(a)
    f_b=funcao(b)
    if f_a*f_b>0:
        raise ValueError("Erro: f(a) e f(b) têm o mesmo sinal. O método não pode garantir uma raiz no intervalo.")
    elif f_a==0:
        return a,[a]
    elif f_b==0:
        return b,[b]
    else:
        iter=0
        iter_para_plote=[]
        while (b-a)/2>tol and iter<1000:
            m=(a+b)/2
            f_m=funcao(m)
            iter_para_plote.append(m)
            iter+=1
            if f_m==0:
                break
            if f_a*f_m<0:
                b=m
                f_b=f_m
            else:
                a=m
                f_a=f_m
    return (a+b)/2,iter_para_plote

def Secante(funcao,a,b,tol):
    #Implementar o Método da Secante
    pass

def Newton(funcao,a,b,tol):
    #Implementar o Método de Newton-Raphson
    pass

if __name__=="__main__":
  f=lambda x: x**2-2
  valor1,_=raiz(f,0,2,1e-6,"bissecao")
  print(valor1)

  fi= lambda x: x**2-4
  valor2,_=raiz(fi,0,4,1e-6,"bissecao")
  print(valor2)
