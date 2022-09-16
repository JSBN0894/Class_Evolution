import atexit
import AER

"""
Definimos la función de adaptación, la cual tiene como parametro un individuo
y modifica su valor de adaptación.
"""

def adtFunction(ind):
    y = lambda x:4-x**2
    ind.adt = y(ind.Chromosome[0])

pop = AER.population(3,[(-10,10)],0.6,0.1,adtFunction)

print("---"*30)
for i in pop.Population:
    print("score = {}, sumScore = {}".format(i.score,i.scoreSum))
print("---"*30)
print("\n")
print("---"*30)

pop.EvaluePopulation()
for i in pop.Population:
    print("score = {}, sumScore = {}".format(i.score,i.scoreSum))
print("---"*30)
