from operator import truediv
import AER

def Restrictions(ind):
    if ind.Chromosome[0] >3 or ind.Chromosome[0]<1:
        return False
    else:
        return True

def adtFunction(ind):
    y = lambda x:4-x**2
    ind.adt = y(ind.Chromosome[0])
    
    if ind.adt<0:
        ind.adt = 1E-6
  
pop = AER.population(1000,[(-10,10)],0.7,0.4,adtFunction,Restrictions)

pop.Evolution(100)
