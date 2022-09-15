from ast import Assert
import numpy as np

class Ind:
    """
    Clase individuo -> Representa la solución del problema como un individuo, como una especie.

    Parametros:
    -----------
    SearchSpace -> Espacio de busqueda, debe ser una lista de tuplas, cada tupla representa los 
                   Limites de busqueda de una variable.

    Chromosome --> Un array de números flotantes que representa el estado de las variables
                   para un individuo

    CrossProbability --> Numero flotante entre 0 y 1 que representa
                         la probabilidad de cruce del individuo

    MutateProbability --> Numero flotante entre 0 y 1 que representa 
                          la probabilidad de mutación del individuo


    """
    def __init__(self,SearchSpace,CrossProbability,MutateProbability):

        self.SearchSpace = SearchSpace
        self.CrossProbability = CrossProbability
        self.MutateProbability = MutateProbability
        self.Chromosome = np.array([Vspace[0]+(Vspace[1]-Vspace[0])
                                    *np.random.rand() for Vspace in self.SearchSpace])
        self.score = 0
        self.adt = 0
        self.sum_score = 0

    def SbxCrossover(self,ind):
        assert len(self.Chromosome) == len(ind.Chromosome),"Los individuos no son de la misma especie"
        """
        Esta función cruza los individuos y remplaza los 
        padres por los hijos.

        Despues del cruce remplaza los cromosomas de los padres por los hijos.
        """
        n = 2
        while True:
            """
            Controlando el posible error de división por cero
            cuando se genera el número alpha.
            """
            alpha = np.random.rand()
            if alpha !=1:
                break
        
        if alpha < 1/2:
            beta = 2*alpha**(1/(n+1))
        else:
            beta = (1/(2*(1-alpha)))**(1/(n+1))

        chromosome_1 = np.random.rand(len(self.SearchSpace))
        chromosome_2 = np.random.rand(len(self.SearchSpace))
        for i in range(len(self.SearchSpace)):
            chromosome_1[i] = 1/2*((self.Chromosome[i] + ind.Chromosome[i]) - beta*abs(ind.Chromosome[i]-self.Chromosome[i]))
            chromosome_2[i] = 1/2*((self.Chromosome[i] + ind.Chromosome[i]) + beta*abs(ind.Chromosome[i]-self.Chromosome[i]))        
        """
        Los condicionales agregan un indice de aleatoriedad en los genes
        por si sus valores en el cruce se salen de los limites de busqueda.
        """
        if (chromosome_1[i]<self.SearchSpace[i][0]) or (chromosome_1[i]>self.SearchSpace[i][1]):
            chromosome_1[i] = self.SearchSpace[i][0] + (self.SearchSpace[i][1] - self.SearchSpace[i][0])*np.random.rand()

        if (chromosome_2[i]<self.SearchSpace[i][0]) or (chromosome_2[i]>self.SearchSpace[i][1]):
            chromosome_2[i] = self.SearchSpace[i][0] + (self.SearchSpace[i][1] - self.SearchSpace[i][0])*np.random.rand()

        self.Chromosome = chromosome_1
        ind.Chromosome = chromosome_2
      


        

    

class population:
    def __init__(self,N,SearchSpace,CrossProbability,MutateProbability,AdtFunction):
        self.N = N
        self.CrossProbability = CrossProbability
        self.SearchSpace = SearchSpace
        self.MutateProbability = MutateProbability
        self.Population = [Ind(self.SearchSpace,self.CrossProbability
                            ,self.MutateProbability) for i in range(self.N)]

    




class Evolution:
    def __init__(self,N,SearchSpace,CrossProbability,MutateProbability,AdtFunction,FinallyFunction = None):
        pass    
    
    """
        creamos la poblacion
        evaluamos la poblacion --> funcion de adaptacion a cada individuo y calcula 
        while True:
            seleccion
            cruce 
            mutación
            evaluar poblacion --> se escoje el mejor individuo Elite
            if Finally(Elite) == True:
                break
    """
    
""" p = population(10,[(0,1),(0,1),(0,1)],0.6,0.1,lambda x: True)
for i in p.Population:
    print(i.Chromosome)
 """
ind1 = Ind([(0,1),(0,1)],0.6,0.1)
ind2 = Ind([(0,1),(0,1)],0.6,0.1)

print("Cromosoma del individuo 1 = ",ind1.Chromosome)
print("Cromosoma del individuo 2= ",ind2.Chromosome)
Ind.SbxCrossover(ind1,ind2)
print("Cromosoma del individuo 1 = ",ind1.Chromosome)
print("Cromosoma del individuo 2= ",ind2.Chromosome)


