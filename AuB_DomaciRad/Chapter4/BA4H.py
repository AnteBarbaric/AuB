def Convolution(arr):
    l=[]
    for a in arr:
        for b in arr:
            if a-b>0:
                l.append(a-b)
    for i in range (len(l)):
        l[i]=str(l[i])
    l.sort()
    return " ".join(l)

if __name__ == '__main__':
    x = '''0 137 186 323'''
    x = x.split(" ")
    for i in range(len(x)):
        x[i] = int(x[i])
    res = Convolution(x)
    print(res)