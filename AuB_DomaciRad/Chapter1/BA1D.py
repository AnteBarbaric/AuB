def kmer(text, i, k):
    return text[i:(i+k)]

def patternposition(text, pattern):
    p=list()
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            p.append(i)
    return p

if __name__ == '__main__':
    x='''ATAT
GATATATGCATATACTT'''
    inlines = x.split()
    pattern = inlines[0]
    text = inlines[1]
    res = patternposition(text, pattern)
    for i in range (len(res)):
        res[i]=str(res[i])
    print(" ".join(res))