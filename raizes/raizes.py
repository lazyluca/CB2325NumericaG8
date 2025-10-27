'''implementação do método das raízes'''

def raiz(funcao, a, b, tol, method):

    if method == "bissecao":
        return bissecao(funcao,a,b,tol)

    elif method == "secante":
        return secante(funcao,a,b,tol)

    elif method == "newton_raphson":
        return newton(funcao,a,b,tol)

    else:
        raise ValueError("Método não reconhecido")

def bissecao(funcao, a, b, tol):

    f_a = funcao(a)
    f_b = funcao(b)

    if f_a*f_b > 0:
        raise ValueError(
            "Erro: f(a) e f(b) têm o mesmo sinal."
            "O método não pode garantir uma raiz no intervalo."
            )
    
    elif f_a == 0:
        return a, [a]
    elif f_b == 0:
        return b, [b]
    
    else:
        iter = 0
        iter_para_plot = []

        while (b-a)/2 > tol and iter < 1000:
            m = (a+b)/2
            f_m = funcao(m)
            iter_para_plot.append(m)
            iter += 1

            if f_m == 0:
                break

            if f_a*f_m < 0:
                b = m
                f_b = f_m
            else:
                a = m
                f_a = f_m

    return (a+b)/2, iter_para_plot

def secante(funcao,a,b,tol):
    iter=0

    while iter<10000:

        f_a=funcao(a)
        f_b=funcao(b)

        if(f_a-f_b==0):
            raise ZeroDivisionError("Erro: f(a) - f(b) = 0. Divisão por zero.")
        
        c=b-f_b*((b-a)/(f_b-f_a))
        f_c=funcao(c)

        if(abs(c-b)<tol or abs(f_c)<tol):
            return c,[c]
        a=b
        b=c
        iter+=1
    raise RuntimeError("Número máximo de iterações atingido sem convergência.")


def newton(funcao,a,b,tol):
    #Implementar o Método de Newton-Raphson
    pass

if __name__=="__main__":
  f=lambda x: x**2-2
  valor1,_=raiz(f,0,2,1e-6,"bissecao")
  print(valor1)

  fi= lambda x: x**2-4
  valor2,_=raiz(fi,0,4,1e-6,"bissecao")
  print(valor2)

  f=lambda x:x**3-9*x+5
  raiz_0,_=raiz(f,a=0,b=2,tol=1e-6,method="secante")
  print(f"{raiz_0:.3f}")

  g= lambda x: x**10-5
  valor2,_=raiz(g,0,4,1e-6,"bissecao")
  print(valor2)

  h = lambda x: x**10-5
  valor2,_=raiz(h,0,4,1e-6,"bissecao")
  print(valor2)
