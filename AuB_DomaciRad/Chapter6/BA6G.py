def CycleToChromosome(Nodes):
    Chromosome=[]
    k=int(len(Nodes)/2)
    for j in range(0,k):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome.append(int(Nodes[2*j+1]/2))
        else:
            Chromosome.append(int(-Nodes[2*j]/2))
    return Chromosome

if __name__ == '__main__':
    x = '''(1 2 4 3 6 5 7 8)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = CycleToChromosome(p)
    for i in range(len(res)):
        if res[i] > 0:
            res[i] = "+" + str(res[i])
        else:
            res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)