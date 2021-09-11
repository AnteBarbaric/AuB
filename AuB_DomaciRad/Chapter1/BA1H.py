def kmer(text,i,k):
    return text[i:i+k]


def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def positions(text,pattern,d):
    res=[]
    for i in range(0,len(text)-len(pattern)):
        if(hamming_distance(kmer(text,i,len(pattern)), pattern)<=d):
            res.append(i)
    return res


if __name__ == "__main__":

    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
    pattern="ATTCTGGA"
    d=3
    res = positions(text,pattern,d)
    print(res)