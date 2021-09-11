def Paths(Graph, i, j,path,L):
    if i==j:
        L.append(path)
        return
    if i not in Graph.keys():
        return

    for node in Graph[i]:
        Path=path.copy()
        Path.append([i,node[0],int(node[1])])
        Paths(Graph,node[0],j,Path,L)

    return L

def LongestPath(L):
    sums=[]
    for l in L:
        s=0
        for edge in l:
            s+=edge[2]
        sums.append(s)
    maxval=max(sums)
    i=sums.index(maxval)

    ret=[L[i][0][0]]
    for e in L[i]:
        ret.append(e[1])

    return maxval,"->".join(ret)

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1500)
    x = '''0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3'''
    inlines = x.split("\n")
    i = inlines[0]
    j = inlines[1]
    graph = dict()
    for k in inlines[2:]:
        pair = k.split("->")
        if pair[0] not in graph.keys():
            graph[pair[0]]=[]
        graph[pair[0]].append(pair[1].split(":"))
    paths=Paths(graph,i,j,[],[])
    res=LongestPath(paths)
    print(res[0])
    print(res[1])