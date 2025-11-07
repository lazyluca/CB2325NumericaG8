# 📈 Cálculo Numérico

Este repositório contém implementações de métodos de interpolação e cálculo de erros, desenvolvidos para a disciplina de programação 2 do IMPA TECH.

---

## 🚀 Funcionalidades

Este projeto implementa as seguintes funcionalidades:

* **Interpolação:**
    * Interpolação Polinomial (Método de Lagrange);
    * Interpolação de Hermite;
    * Interpolação Linear por partes.

* **Raízes de Funções:**
    * Método da Bisseção;
    * Método da Secante;
    * Método de Newton-Raphson.
---

## 📋 Pré-requisitos

Para executar este projeto, você precisará de:

* Python 3.9+
* NumPy
* Matplotlib

---

## 💡 Exemplo de Uso


### Interpoladores
Aqui estão exemplos de como usar os interpoladores.

#### Interpolação de Hermite

```python
# 1. defina os dados de entrada
pontos_x = [0, 1]
valores_y = [1, 2]
derivadas_dy = [1, 0]

# 2. Crie uma instância da class
polinomio = InterpoladorHermite(pontos_x, valores_y, derivadas_dy)

# 3. Ache o valor desejado para um ponto
print(f"H(0) = {polinomio(0):.4f}")
print(f"H(1) = {polinomio(1):.4f}")
print(f"H(0.5) = {polinomio(0.5):.4f}")
```
### Raízes
Aqui estão exemplos de como usar os métodos raízes de funções.

#### Método da Bisseção 

```python
#1. defina os dados de entrada
def f(x):
    return x**2 - 2

#2. Utilizar a função nos dados de entrada
raiz0,_ = raiz(f, a=0, b=2, tol=1e-6, method="bissecao")

#3. Saída esperada
print(raiz0)
```
