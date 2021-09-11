def BreakOnGenomeGraph(GenomeGraph, i, I, j, J):
     if (i,I) in GenomeGraph:
         GenomeGraph.remove((i,I))
     else:
         if (I,i) in GenomeGraph:
             GenomeGraph.remove((I, i))
     if (j,J) in GenomeGraph:
         GenomeGraph.remove((j,J))
     else:
         if (J,j) in GenomeGraph:
             GenomeGraph.remove((J, j))
     GenomeGraph.append((i,j))
     GenomeGraph.append((I,J))
     return GenomeGraph

if __name__ == '__main__':
    x = '''(2, 4), (3, 8), (7, 5), (6, 1)
1, 6, 3, 8'''
    inlines = x.split("\n")
    edges = inlines[0]
    edges = edges[1:-1]
    p = edges.split("), (")
    for i in range(len(p)):
        a = p[i].split(", ")
        p[i] = (int(a[0]), int(a[1]))
    indices = inlines[1].split(", ")
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    #print(p)
    res = BreakOnGenomeGraph(p, indices[0], indices[1], indices[2], indices[3])
    for i in range(len(res)):
        res[i] = str(res[i])
    res = ", ".join(res)
    print(res)