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

    Restrictions --> función que define las restricciones que debe cumplir el individuo, debe
                    retornar verdadero si el individuo cumple con las caracteristicas minimas para
                    ser una posible solución

    """
    def __init__(self,SearchSpace,Restrictions = lambda x: True):

        self.SearchSpace = SearchSpace
        self.Restrictions = Restrictions
        self.MakeChromosome()
        self.score = 0
        self.adt = 0
        self.scoreSum= 0

    def MakeChromosome(self):
        """
        actualiza el valor del cromosoma teniendo en cuenta la función de restricción
        """
        cont = 0
        while True:
            cont+=1
            self.Chromosome = np.array([Vspace[0]+(Vspace[1]-Vspace[0])
                                        *np.random.rand() for Vspace in self.SearchSpace])
            if self.Restrictions(self):
                break
            assert cont<1.5E6, "se iteraron {} veces, y no se encontró un individuo que cumpliera las restricciones".format(cont)


    def UniformMutate(self):
        i = np.random.randint(len(self.SearchSpace))
        self.Chromosome[i] = self.SearchSpace[i][0] + (self.SearchSpace[i][1] - self.SearchSpace[i][0])*np.random.rand()
        if self.Restrictions()!=True:
            self.MakeChromosome()

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
        if self.Restrictions(self)!= True:
            self.MakeChromosome()
        if self.Restrictions(ind)!=True:
            ind.MakeChromosome()
        

            
