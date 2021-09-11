def kmer(text, i, k):
    return text[i:(i+k)]

def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return(D)

def mostfrequentkmers(text, k):
    D = kmersfrequency(text, k)
    maxcount = max(D.values())
    return [x[0] for x in D.items() if x[1] == maxcount]

if __name__ == '__main__':
    x = '''ACGTTGCATGTCGCATGATGCATGAGAGCT
4'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    res = mostfrequentkmers(text, k)
    print(" ".join(res))