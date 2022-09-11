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
        self.CrossProbability = CrossProbability
        self.MutateProbability = MutateProbability
        self.Crhomosome = np.array([Vspace[0]+(Vspace[1]-Vspace[0])
                                    *np.random.rand() for Vspace in SearchSpace])
        self.score = 0
        self.adt = 0
        self.sum_score = 0

    

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
    
    
