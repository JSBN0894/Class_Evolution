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
        ind.adt = 1E-3

pop = AER.population(10,[(-10,10) for i in range(5)],0.7,0.1,adtFunction)

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

print("---"*30)
print("Probando la seleccion")
print("---"*30)
for i in pop.Population:
    print("adaptation = {}".format(i.adt))
print("---"*30)
pop.Selection()
for i in pop.Population:
    print("adaptation = {}".format(i.adt))
print("---"*30)
print("Probando la función de cruce de población")
print("---"*30)
for i in pop.Population:
    print("chromosome = {}".format(i.Chromosome))
pop.CrossingPopulation()
print("---"*30)
for i in pop.Population:
    print("chromosome = {}".format(i.Chromosome))

print("---"*30)
print("Probando mutación")
print("---"*30)
for i in pop.Population:
    print("chromosome = {}".format(i.Chromosome))

pop.MutatePopulation()
print("---"*30)
for i in pop.Population:
    print("chromosome = {}".format(i.Chromosome))