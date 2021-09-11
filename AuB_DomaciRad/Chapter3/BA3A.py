def kmer(text, i, k):
    return text[i:(i+k)]

def stringComposition(text,k):
	lista=list()
	for i in range(0,len(text)-k+1):
		lista.append(kmer(text,i,k))
	return sorted(lista)

if __name__ == '__main__':

    x='''5
CAATCCAAC'''
    inlines=x.split()
    text=inlines[1]
    k=int(inlines[0])
    res=stringComposition(text,k)
    print("\n".join(res))