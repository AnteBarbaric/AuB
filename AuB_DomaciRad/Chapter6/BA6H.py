
def ChromosomeToCycle(Chromosome):
    Nodes=[]
    for j in range(0,len(Chromosome)):
        i=Chromosome[j]
        if i > 0:
            Nodes.append(2*i-1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i) #minus because i is negative
            Nodes.append(-2*i-1)
    return Nodes

def ColoredEdges(P):
     Edges=[]
     for Chromosome in P:
          Nodes=ChromosomeToCycle(Chromosome)
          for j in range(len(Chromosome)):
               Edges.append((Nodes[2*j+1], Nodes[(2*j+2)%len(Nodes)]))
     return Edges

if __name__ == '__main__':
    x = '''(+1 -2 -3)(+4 +5 -6)'''
    x = x[1:-1]
    p = x.split(")(")
    for j in range(len(p)):
        p[j] = p[j].split(" ")
        for i in range(len(p[j])):
            p[j][i] = int(p[j][i])
    res = ColoredEdges(p)
    for i in range(len(res)):
        res[i] = str(res[i])
    res = ", ".join(res)
    print(res)