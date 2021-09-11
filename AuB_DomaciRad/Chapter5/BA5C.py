def LCSBacktrack(v,w):
    Backtrack=[]
    s = []
    for i in range(len(v)+1):
        s.append([0])
    for j in range(1, len(w)+1):
        s[0].append(0)

    for i in range(0,len(v)):
        Backtrack.append([])

    for i in range (1,len(v)+1):
        for j in range(1, len(w)+1):
            if v[i-1]==w[j-1]:
                s[i].append(max([s[i-1][j],s[i][j-1],s[i-1][j-1]+1]))
            else:
                s[i].append(max([s[i - 1][j], s[i][j - 1],s[i-1][j-1]]))
            if s[i][j]==s[i-1][j]:
                Backtrack[i-1].append("D")
            else:
                if s[i][j] == s[i][j-1]:
                    Backtrack[i-1].append("R")
                else:
                    Backtrack[i-1].append("Diag")
    return Backtrack

def OutputLCS(Backtrack, v, i, j,final):
    if i==-1 or j==-1:
        print(final[::-1])
        return
    if Backtrack[i][j]=="D":
        OutputLCS(Backtrack, v, i -1, j,final)
    else:
        if Backtrack[i][j]=="R":
            OutputLCS(Backtrack, v, i, j -1,final)
        else:
            final = final + v[i]
            OutputLCS(Backtrack, v, i -1, j -1,final)

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1500)
    x = '''AACCTTGG
ACACTGTGA'''
    inlines = x.split("\n")
    v = inlines[0]
    w = inlines[1]
    res = OutputLCS(LCSBacktrack(v, w), v, len(v) - 1, len(w) - 1, "")