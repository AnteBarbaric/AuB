def CycleToChromosome(Nodes):
    Chromosome=[]
    k=int(len(Nodes)/2)
    for j in range(0,k):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome.append(int(Nodes[2*j+1]/2))
        else:
            Chromosome.append(int(-Nodes[2*j]/2))
    return Chromosome

def GraphToGenome(GenomeGraph):
     P=[]
     for Nodes in GenomeGraph:
          Chromosome=CycleToChromosome(Nodes)
          P.append(Chromosome)
     return P

def PairsToGraphnovi(p):
    graph = []
    start = 0
    P=p.copy()
    while len(P)>0:
        cycle=[P[start]]
        P.remove(P[start])
        while True:
            if cycle[-1][1]%2==0:
                for pair in P:
                    if cycle[-1][1]-1 in pair:
                        if cycle[-1][1]-1 == pair[0]:
                            cycle.append((pair[0],pair[1]))
                        else:
                            cycle.append((pair[1],pair[0]))
                        P.remove(pair)
                        break
            else:
                for pair in P:
                    if cycle[-1][1]+1 in pair:
                        if cycle[-1][1] + 1 == pair[0]:
                            cycle.append((pair[0], pair[1]))
                        else:
                            cycle.append((pair[1], pair[0]))
                        P.remove(pair)
                        break
            if cycle[0][0] % 2 == 0:
                if cycle[0][0] - 1 in cycle[-1]:
                    break
            else:
                if cycle[0][0] + 1 in cycle[-1]:
                    break
        Cycle=[cycle[0][1]]
        for i in range (1,len(cycle)):
            Cycle.append(cycle[i][0])
            Cycle.append(cycle[i][1])
        Cycle.append(cycle[0][0])
        graph.append(Cycle)
    return graph

def PairsToGraph(p):
    graph = []
    start = 0
    while start < len(p):
        cycle = []
        cycle.append(p[start][0])
        cycle.append(p[start][1])
        for i in range(start+1, len(p)):
            cycle.append(p[i][0])
            if p[i][1] - cycle[0] == 1 or p[i][1] - cycle[0] == -1:
                cycle.insert(0, p[i][1])
                start = i + 1
                break
            cycle.append(p[i][1])
        graph.append(cycle)
    return graph

if __name__ == '__main__':
    x = '''(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'''
    x = x[1:-1]
    p = x.split("), (")
    for i in range(len(p)):
        a = p[i].split(", ")
        p[i] = (int(a[0]), int(a[1]))
    graph = PairsToGraph(p)
    res = GraphToGenome(graph)
    for j in range(len(res)):
        for i in range(len(res[j])):
            if res[j][i] > 0:
                res[j][i] = "+" + str(res[j][i])
            else:
                res[j][i] = str(res[j][i])
        res[j] = " ".join(res[j])
        res[j] = "(" + res[j] + ")"
    res = "".join(res)
    print(res)