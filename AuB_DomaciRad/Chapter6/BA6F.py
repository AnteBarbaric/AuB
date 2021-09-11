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

if __name__ == '__main__':
    x = '''(+1 -2 -3 +4)'''
    x = x[1:-1]
    p = x.split(" ")
    for i in range(len(p)):
        p[i] = int(p[i])
    res = ChromosomeToCycle(p)
    for i in range(len(res)):
        res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)