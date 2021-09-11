def prefix(pattern):
    """substring of pattern without  the last letter"""
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def overlapGraph(seq):
    adjacency=dict()
    seq.sort()
    for pattern in seq:
        adjacency[pattern]=[pattern2 for pattern2 in seq if suffix(pattern)==prefix(pattern2)]
    return adjacency

def graphPrint(adj):
    for key in adj.keys():
        if len(adj[key])>0:
            print(key,'->',adj[key][0])

if __name__ == '__main__':

    x='''ATGCG
GCATG
CATGC
AGGCA
GGCAT'''
    inlines=x.split()
    res=overlapGraph(inlines)
    graphPrint(res)