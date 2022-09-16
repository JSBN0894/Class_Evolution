import AER

def restiction(ind):
    for gen in ind.Chromosome:
        if gen>0.5:
            return False
    return True
            
searchSpace = [(0,1) for i in range(10)]
ind = AER.Ind(searchSpace,0.6,0.1,restiction)

print(ind.Chromosome)