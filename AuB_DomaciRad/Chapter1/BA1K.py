def kmer(text, i, k):
    return text[i:(i+k)]

def ComputingFrequencies(text, k):
    frequencyArray=[0]*(4**k)
    for i in range(0,len(text)-k+1):
        pattern=kmer(text,i,k)
        j=PatternToNumber(pattern)
        frequencyArray[j]=frequencyArray[j]+1
    return frequencyArray

def PatternToNumber(pattern):
    def allkmers(k):
        nucleotides = {'A', 'C', 'G', 'T'}
        kmers = []
        if k == 0:
            return kmers
        if k == 1:
            for n in nucleotides:
                kmers.append(n)
            return kmers
        for x in allkmers(k - 1):
            for n in nucleotides:
                kmers.append(n + x)
        return kmers
    all=allkmers(len(pattern))
    all.sort()
    return (all.index(pattern))

if __name__ == '__main__':
    x='''ACGCGGCTCTGAAA
2'''
    inlines = x.split()
    text = inlines[0]
    k = int(inlines[1])
    res=ComputingFrequencies(text,k)
    for i in range (len(res)):
        res[i]=str(res[i])
    print(" ".join(res))