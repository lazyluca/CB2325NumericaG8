import numpy as np
import matplotlib.plotly as plt

class Interpolador_Linear_por_Partes()

  def __init__(self, lista_x: list, lista_y:list):

    self.x = lista_x
    self.y = lista_y

  def interpolar(x):

    if x<self.x[0] or x>self.x[-1]:
      return ValueError('Erro de Extrapolação: a abscissa a ser avaliada está fora do intrevalo de interpolação.
    else:
      
                        
    
