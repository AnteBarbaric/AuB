def LinearSpectrum(Peptide, AminoAcid, AminoAcidMass):
    PrefixMass=[]
    PrefixMass.append(0)
    for i in range (len(Peptide)):
        for j in range (0,20):
            if AminoAcid[j] == Peptide[i]:
                PrefixMass.append(PrefixMass[i] + AminoAcidMass[j])
    LinearSpectrum=[0]
    for i in range (len(Peptide)):
        for j in range (i+1,len(Peptide)+1):
            LinearSpectrum.append(PrefixMass[j]-PrefixMass[i])
    LinearSpectrum=sorted(LinearSpectrum)
    for i in range (len(LinearSpectrum)):
        LinearSpectrum[i]=str(LinearSpectrum[i])
    return " ".join(LinearSpectrum)

if __name__ == '__main__':
    x = '''NQEL'''
    res = LinearSpectrum(x,
                         ["G", "A", "S", "P", "V", "T", "C", "I", "L", "N", "D", "K", "Q", "E", "M", "H", "F", "R", "Y",
                          "W"],
                         [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163,
                          186])
    print(res)