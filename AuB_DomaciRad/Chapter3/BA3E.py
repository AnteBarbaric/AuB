def prefix(pattern):
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    return pattern[1:]

def DeBrujinRec(Patterns):
    adjacency = dict()
    sortedPattern = sorted(Patterns)
    for pattern in sortedPattern:
        adjacency[prefix(pattern)] = []
    for pattern in sortedPattern:
        adjacency[prefix(pattern)].append(suffix(pattern))
    return adjacency

def multipleGraphPrint(adj):
    for key in adj.keys():
        print(key,'->',",".join(adj[key]))

if __name__ == '__main__':

    x='''GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG'''
    inlines=x.split()
    res=DeBrujinRec(inlines)
    multipleGraphPrint(res)