import numpy as np
import matplotlib.pyplot as plt

#OBSERVAÇÃO: Por enquanto sem arredondamento de casas decimais

class Interpolação_Linear_por_Partes():

    def __init__(self, lista_x: list, lista_y:list):

      self.x = lista_x
      self.y = lista_y

    #Supondo que as listas já são recebidas devidamente pareadas
  
    """
    
    def calcular_retas(self):
  
        self.retas = [] #Atributo que só passa a existir quando esta função é chamada
        
          for i in range(len(self.x)-1):
            coef_angular = (self.y[i+1]-self.y[i])/(self.x[i+1]-self.x[i])
            coef_linear = self.y[i] - self.x[i]*coef_angular 
            self.retas.append((coef_angular,coef_linear)
      
        return self.retas
          
        """
                          
    def __call__(self, x):
  
        if x<self.x[0] or x>self.x[-1]:
            return ValueError('Erro de Extrapolação: a abscissa a ser avaliada está fora do intrevalo de interpolação.')
        else:
            i = 0
            while True:
                if self.x[i]<=x<self.x[i+1]: 
                    break
                i+=1
                
            coef_angular = (self.y[i+1]-self.y[i])/(self.x[i+1]-self.x[i])
            coef_linear = self.y[i] - self.x[i]*coef_angular
      
            return coef_angular*x+coef_linear

#TESTE:

x = [1,2,3,5]
y = [2,4,8,32]

interpolador = Interpolação_Linear_por_Partes(x,y)
print(interpolador(4)) #saída esperada: 20.0
              
            
    
