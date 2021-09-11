def greedySorting(P):
    approxReversalDistance=0
    reversalList=[]
    for k in range (1,len(P)+1):
        newP=[]
        if (P[k-1]!=k):
            l=0
            if (k in P):
                l=P.index(k)
            if (-k in P):
                l=P.index(-k)
            newP = P.copy()
            for i in range (k-1,l+1):
                newP[i]=-P[l-(i-k)-1]
            reversalList.append(newP)
            P=newP
            approxReversalDistance=approxReversalDistance+1
        if (P[k-1]==-k):
            newP=P.copy()
            newP[k-1]=k
            reversalList.append(newP)
            P=newP
            approxReversalDistance=approxReversalDistance+1
    return reversalList

if __name__ == '__main__':
    x = '''(-3 +4 +1 +5 -2)'''
    P = x.split(" ")
    P[0] = P[0][1:]
    P[len(P) - 1] = P[len(P) - 1][:-1]
    for i in range(len(P)):
        P[i] = int(P[i])
    res = greedySorting(P)
    pr = []
    for L in res:
        for i in range(len(L)):
            if L[i] > 0:
                L[i] = "+" + str(L[i])
            else:
                L[i] = str(L[i])
        pr.append(("(" + " ".join(L) + ")"))
    resfin = "\n".join(pr)
    print(resfin)