def kmer(text, i, k):
    return text[i:(i+k)]

def prefix(pattern):
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    #substring of pattern without first letter
    return pattern[1:]

def Lwindows(text,L):
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def multipleGraphPrint(adj):
    for key in adj.keys():
        print(key,'->',",".join(adj[key]))

def DeBruijn(k,text):
    adjacency=dict()
    sortedWindows=sorted(Lwindows(text,k))
    for window in sortedWindows:
        adjacency[prefix(window)]=[]
    for window in sortedWindows:
        adjacency[prefix(window)].append(suffix(window))
    return  adjacency

if __name__ == '__main__':

    x='''4
AAGATTCTCTAC'''
    inlines=x.split()
    k=int(inlines[0])
    text=inlines[1]
    res=DeBruijn(k,text)
    multipleGraphPrint(res)