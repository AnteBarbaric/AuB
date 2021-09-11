def suffix(pattern):
    return pattern[1:]

def HammingDistance(p, q):
    if len(p) != len(q):
        return -1

    dist = 0
    #zip(AB,CD) gives (('A','C'),('B','D'))
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist

def Neighbors(pattern,d):
    nucleotides={'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=Neighbors(suffix(pattern),d)
    for x in suffixNeighbors:
        if (HammingDistance(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

if __name__ == '__main__':
    x = '''ACG
1'''
    inlines = x.split()
    pattern = inlines[0]
    d = int(inlines[1])
    res = Neighbors(pattern, d)
    for r in res:
        print(r)