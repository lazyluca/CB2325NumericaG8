import numpy as np
import matplotlib.pyplot as plt

class PolynomialInterpolator:
    """
    Cria um objeto de polinômio interpolador usando o método de Newton.
    """

    def __init__(self, valores_x: list, valores_y: list):
        """
        Inicializa o interpolador com os pontos (x, y).
        """
        if not isinstance(valores_x, list) or not isinstance(valores_y, list):
            raise TypeError('A função recebe duas listas como entrada')
            
        if not valores_x or len(valores_x) != len(valores_y):
            raise ValueError('As listas estão vazias ou têm tamanhos diferentes')
            
        self.valores_x = valores_x
        self.valores_y = valores_y
        self.memory = {}

    def _calc_coef_rec(self, valores_x: list, valores_y: list, lista: list):
        """
        Calcula coeficientes recursivamente com memoização (cache).
        """
        if len(valores_x) == 1:
            return [float(valores_y[0]), lista]
        else:
            if tuple(valores_x[1:]) in self.memory:
                if tuple(valores_x[:-1]) in self.memory:
                    a = self.memory[tuple(valores_x[1:])]
                    b = self.memory[tuple(valores_x[:-1])]
                else:
                    a = self.memory[tuple(valores_x[1:])]
                    b = self._calc_coef_rec(valores_x[:-1], valores_y[:-1], lista)[0]
                    self.memory[tuple(valores_x[:-1])] = b
            elif tuple(valores_x[:-1]) in self.memory:
                if tuple(valores_x[1:]) in self.memory:
                    a = self.memory[tuple(valores_x[1:])]
                    b = self.memory[tuple(valores_x[:-1])]
                else:
                    b = self.memory[tuple(valores_x[:-1])]
                    a = self._calc_coef_rec(valores_x[1:], valores_y[1:], [])[0]
                    self.memory[tuple(valores_x[1:])] = a
            else:
                a = self._calc_coef_rec(valores_x[1:], valores_y[1:], [])[0]
                b = self._calc_coef_rec(valores_x[:-1], valores_y[:-1], lista)[0]
                self.memory[tuple(valores_x[1:])] = a
                self.memory[tuple(valores_x[:-1])] = b
                
            denominador = float(valores_x[-1]) - float(valores_x[0])

            if len(valores_x) > 2:
                lista.append(b)

            if denominador == 0:
                raise ValueError('A entrada dos valores de x contém números repetidos')

            return [(a - b) / denominador, lista]

    def _calc_coef_ite(self):
        """
        Calcula os coeficientes iterativamente (O(n^2)).
        """
        n = len(self.valores_x)
        # BUG FIX: Cria uma cópia float com NumPy para não modificar 
        # a lista original 'self.valores_y'.
        coef = np.array(self.valores_y, dtype=float)

        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                denominador = (self.valores_x[i] - self.valores_x[i - j])

                if denominador == 0:
                    raise ValueError('A entrada dos valores de x contém números repetidos')

                coef[i] = (coef[i] - coef[i - 1]) / denominador
        return coef

    def __call__(self, x: float):
        """
        Avalia o polinômio interpolador em um ponto 'x'
        """
        k = 0
        
        # --- Abordagem 1: Iterativa ---
        coef = self._calc_coef_ite()
        
        # --- Abordagem 2: Recursiva (Comentada) ---
        # Para usar o método recursivo, as linhas abaixo são necessárias.
        # A chamada é feita com [self.valores_y[0]] (c0) já na lista,
        # pois a lógica recursiva '_calc_coef_rec' não captura esse
        # primeiro coeficiente (o caso base de len(valor_x) == 2).
        
        # lista = self._calc_coef_rec(
        #     self.valores_x, self.valores_y, [self.valores_y[0]]
        # )
        # coef = lista[1] + [lista[0]]
        
        prod = 1
        for i in range(len(self.valores_x)):
            k += coef[i] * prod
            prod *= (x - self.valores_x[i])

        return k


    def plot_polynomial(self, n_suave=500):
                """
                Gera um gráfico do polinômio de interpolação e dos pontos de entrada.
    
                Args:
                    n_suave (int, optional): Número de pontos para a curva suave.
                                            Padrão é 500.
                """
    
                plt.style.use('seaborn-v0_8-darkgrid') 
                
                x_min = np.min(self.valores_x)
                x_max = np.max(self.valores_x)
                x_suave = np.linspace(x_min, x_max, n_suave)
                y_suave = [self(x) for x in x_suave]
     
                plt.plot(x_suave, y_suave, 
                        '-', 
                        label="Polinômio de Interpolação", 
                        color='orange', 
                        linewidth=2,
                        zorder=2)
     
                plt.plot(self.valores_x, self.valores_y, 
                        'o', 
                        label="Pontos de Entrada", 
                        color='blue', 
                        markersize=7, 
                        markeredgecolor='black',
                        zorder=3)
                
                plt.title("Gráfico do Polinômio de Interpolação de Newton", 
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
    vetor_x = [0, 1, 2, 3]
    vetor_y = [1, 2, 0, 4]
    
    n_suave = 500 
    
    p = PolynomialInterpolator(vetor_x, vetor_y)

    ponto_teste = 1.5
    resultado = p(ponto_teste)
    print(f"P({ponto_teste}) = {resultado}")

    p.plot_polynomial(n_suave)
    
