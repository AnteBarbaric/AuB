def reconstr(seq):
    text=seq[0]
    for i in range (1,len(seq)):
        text=text+seq[i][-1]
    return text

if __name__ == '__main__':

    x='''ACCGA
CCGAA
CGAAG
GAAGC
AAGCT'''
    inlines=x.split()
    res=reconstr(inlines)
    print(res)