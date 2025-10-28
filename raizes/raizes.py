#Implementação do método das raízes

def raiz(funcao, a=None, b=None, tol=None, f_prime=None, max_iter=1000, method=None):

    if method == "bissecao":
        return bissecao(funcao, a, b, tol,max_iter)

    elif method == "secante":
        return secante(funcao,a,b,tol,max_iter)

    elif method == "newton_raphson":
        return newton(funcao,a,tol,f_prime, max_iter)

    else:
        raise ValueError("Método não reconhecido")

def bissecao(funcao, a, b, tol,max_iter):

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

def secante(funcao,a,b,tol,max_iter):
    iter=0
    iter_para_plot=[]

    while iter<max_iter:

        f_a=funcao(a)
        f_b=funcao(b)

        if(f_a-f_b==0):
            raise ZeroDivisionError("Erro: f(a) - f(b) = 0. Divisão por zero.")
        
        c=b-f_b*((b-a)/(f_b-f_a))
        f_c=funcao(c)
        iter_para_plot.append(c)

        if(abs(c-b)<tol or abs(f_c)<tol):
            return c,iter_para_plot
        a=b
        b=c
        iter+=1
    raise RuntimeError("Número máximo de iterações atingido sem convergência.")


def newton(funcao, a, tol, f_prime, max_iter):
    iter=0
    iter_para_plot=[]

    while iter<max_iter:
        f_a=funcao(a)

        if(f_prime==None):
            pass
        else:
            f_prime_a=f_prime(a)

        if f_prime_a==0:
            raise ZeroDivisionError("Erro: derivada zero f_prime(a) = 0. Divisão por zero.")
        
        c=a-f_a/f_prime_a
        iter_para_plot.append(c)
        
        if(abs(c-a)<tol):
            return c,iter_para_plot
        
        a=c
        iter+=1
    
    raise RuntimeError("Número máximo de iterações atingido sem convergência.")

#Testes temporários
if __name__=="__main__":
  f=lambda x: x**2-2
  valor1,_=raiz(f,0,2,1e-6,method="bissecao")
  print(valor1)

  fi= lambda x: x**2-4
  valor2,_=raiz(fi,0,4,1e-6,method="bissecao")
  print(valor2)

  f=lambda x:x**3-9*x+5
  raiz_0,_=raiz(f,a=0,b=2,tol=1e-6,method="secante")
  print(f"{raiz_0:.3f}")

  g= lambda x: x**10-5
  valor2,_=raiz(g,0,4,1e-6,method="bissecao")
  print(valor2)

  h = lambda x: x**10-5
  h_prime = lambda x: 10*x**9
  valor2=raiz(h,2,tol=1e-6,f_prime=h_prime, method="newton_raphson")
  print(valor2)
