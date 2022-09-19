import atexit
import AER

"""
Definimos la función de adaptación, la cual tiene como parametro un individuo
y modifica su valor de adaptación.
"""

def adtFunction(ind):
    y = lambda x:4-x**2
    ind.adt = y(ind.Chromosome[0])
    
    if ind.adt<0:
        ind.adt = 1E-6
  
pop = AER.population(1000,[(-1000,1000)],0.7,0.4,adtFunction)

pop.Evolution(100)