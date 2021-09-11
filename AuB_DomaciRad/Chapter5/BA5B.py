def ManhattanTourist(n, m, Down, Right):
    s=[]
    for i in range (n+1):
        s.append([])
    s[0].append(0)
    #first column
    for i in range(1,n+1):
        s[i].append(s[i-1][0]+Down[i-1][0])
    #first row
    for j in range(1,m+1):
        s[0].append(s[0][j-1]+Right[0][j-1])
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i].append(max(s[i-1][j]+Down[i-1][j],s[i][j-1]+Right[i][j-1]))
    return s[n][m]

if __name__ == '__main__':
    x='''4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2'''
    inlines=x.split("\n")
    n=int(inlines[0].split()[0])
    m=int(inlines[0].split()[1])
    down=[inlines[i+1].split() for i in range(n)]
    Down=[]
    for i in range (len(down)):
        Down.append([])
        for el in down[i]:
            Down[i].append(int(el))
    right = [inlines[i + 1+n+1].split() for i in range(n+1)]
    Right = []
    for i in range(len(right)):
        Right.append([])
        for el in right[i]:
            Right[i].append(int(el))
    ##down niz podnizova=[[],[],..], analogno i right uzima se redak po redak
    res=ManhattanTourist(n,m,Down,Right)
    print (res)