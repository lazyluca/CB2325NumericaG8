import numpy as np
import matplotlib.plotly as plt

#OBSERVAÇÃO: Por enquanto sem arredondamento de casas decimais

class Interpolador_Linear_por_Partes():

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
                          
    def interpolar_x(self, x):
  
        if x<self.x[0] or x>self.x[-1]:
            return ValueError('Erro de Extrapolação: a abscissa a ser avaliada está fora do intrevalo de interpolação.')
        else:
            while True:
                i = 0
                if self.x[i]<=x<self.x[i+1]: 
                    break
                i+=1
                
            coef_angular = (self.y[i+1]-self.y[i])/(self.x[i+1]-self.x[i])
            coef_linear = self.y[i] - self.x[i]*coef_angular
      
            return coef_angular*x+coef_linear
        

    
        
        
              
            
    
