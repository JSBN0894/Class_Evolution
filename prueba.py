import AER
import numpy as np
import matplotlib.pyplot as plt

A = lambda r: 2*np.pi*r**2 + 2*np.pi*r*(1/(np.pi*r**2))
def adt(ind):
    r = ind.Chromosome[0]
    ind.adt = 100/(1*A(r))

pop = AER.population(100,[(0,0.6)],0.7,0.1,adt)
pop.Evolution(100)

R = np.linspace(0.01,2,100)
area = A(R)
best = pop.best.Chromosome[0]

plt.plot(R,area)
plt.plot(best,A(best),"*",color = "red")
plt.show()


