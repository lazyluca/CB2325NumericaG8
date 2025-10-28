import numpy as np
import matplotlib.pyplot as plt

#OBSERVAÇÃO: Por enquanto sem arredondamento de casas decimais

#SUGESTÃO: Fazer um map para receber uma lista de pontos (tuplas) e separar em dois arrays de coordenadas x e y 

#SUGESTÃO: Fazer uma função para adicionar pontos base (dados) a um interpolador. AKA criar nova array 

class Interpolação_Linear_por_Partes():

    def __init__(self, lista_x: list, lista_y:list): #Supõe que as listas recebidas já são devidamente pareadas.
        
        if len(lista_x)!=len(lista_y):
            raise ValueError('As listas devem ter a mesma quantidade de elementos.')
        if len(lista_x)!=len(set(lista_x)):
            raise ValueError('A lista de abscissas possui valores repetidos.')

        self.x = np.array(lista_x)
        self.y = np.array(lista_y)

    def reta(self,i):
        
        """
        Função auxiliar que calcula a reta do ponto a ser interpolado.
        
        Empregada em '__call__'; calcular_retas;       
        """

        coef_angular = (self.y[i+1]-self.y[i])/(self.x[i+1]-self.x[i])
        coef_linear = self.y[i] - self.x[i]*coef_angular
      
        return coef_angular, coef_linear

    def __call__(self, x):
  
        if x<self.x[0] or x>self.x[-1]:
            raise ValueError('Erro de Extrapolação: a abscissa a ser avaliada está fora do intrevalo de interpolação.')
        elif x==self.x[-1]:
            return self.y[-1] 
        else:
            i = 0
            while True:
                if self.x[i]<=x<self.x[i+1]: 
                    break
                i+=1
                
            a,b = self.reta(i)
        
            return a*x+b
        
    def calcular_retas(self):      
  
        """
        Útil caso o usuário deseje realizar muitas interpolações (mais que a quantidade de pontos em self.x).

        Implementada para ser empregada para a função 'interpolar_muitos_pontos'. 

        Já calcula todas as retas entre os pontos fornecidos e armazena-as como lista de tuplas:
        
        [(coeficiente angular, coeficiente linear),...]. 
        """

        lista = [] #Atributo que só passa a existir quando esta função é chamada
        
        for i in range(len(self.x)-1):
            a,b = self.reta(i) 
            lista.append((a,b))
      
        self.retas = np.array(lista)

        return self.retas

    def interpolar_muitos_pontos(self,x):
        
        """
        Interpola um único ponto, mas é mais eficiente que '__call__' quando utilizada muitas vezes.
        
        Necessita antes que a função 'calcular_retas' seja chamada. 
        """

        if x<self.x[0] or x>self.x[-1]:
            return ValueError('Erro de Extrapolação: a abscissa a ser avaliada está fora do intrevalo de interpolação.')
        elif x == self.x[-1]:
            return self.y[-1]
        else:    
            i = 0
            while True:
                if self.x[i]<=x<self.x[i+1]: 
                    break
                i+=1
        
        y = self.retas[i][0]*x+self.retas[i][1]

        return y

#TESTES

#1 - Teste do interpolador 'call':

x = [1,2,3,5]
y = [2,4,8,32]
interpolador_1 = Interpolação_Linear_por_Partes(x,y)

print(interpolador_1(4)) #saída esperada: 20.0

#2 - Teste de 'calcular_retas' e 'interpolar_muitos_pontos':

a = [2,3,4]
b = [4,9,16]
interpolador_2 = Interpolação_Linear_por_Partes(a,b)

interpolador_2.calcular_retas()

pontos_interpolados = []
for i in range(40):
    k=2+i/20
    pontos_interpolados.append((k,float(interpolador_2.interpolar_muitos_pontos(k))))

print(pontos_interpolados) #saída esperada: lista com os pontos interpolados
