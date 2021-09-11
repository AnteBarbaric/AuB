def kmer(text, i, k):
    return text[i:(i+k)]


def patterncount(text, pattern):
    count=0
    n=len(pattern)
    for i in range(0,len(text)-n+1):
        if kmer(text,i,n)==pattern:
            count=count+1
    return count


if __name__ == '__main__':

    x='''GCGCG
GCG'''
    inlines = x.split() #naredba split rasstavlja string u listu gdje je svaki znak u string novi element liste
    text = inlines[0]
    pattern = inlines[1]
    res = patterncount(text, pattern)
    print(str(res))