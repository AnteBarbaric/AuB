def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }
    return mass

def Mass(peptide):
    aa_masses=get_amino_acid_mass()
    sumMass=0
    for a in peptide:
        if a in aa_masses.keys():
            sumMass=sumMass+aa_masses[a]
    return sumMass

def LinearspectrumList(peptide):
    subPeptides=['',peptide]
    for i in range (1,len(peptide)):
        for j in range(0,len(peptide)-i+1):
            subPeptides.append(peptide[j:j+i])
    spectrum=[]
    for pep in subPeptides:
        spectrum.append(Mass(pep))
    spectrum.sort()
    return spectrum

def LinearScore(peptide,Spectrum):
    spectrum = Spectrum.split()
    for i in range(len(spectrum)):
        spectrum[i] = int(spectrum[i])
    counter=0
    spec=spectrum.copy()
    for value in LinearspectrumList(peptide):
        if value in spec:
            counter=counter+1
            spec.remove(value)
    return counter

def Trim(Leaderboard,Spectrum,N):
    spectrum = Spectrum.split()
    for i in range(len(spectrum)):
        spectrum[i] = int(spectrum[i])
    LinearScores=[]
    for j in range (len(Leaderboard)):
        Peptide=Leaderboard[j]
        LinearScores.append(LinearScore(Peptide,Spectrum))
    #sorting two list according to one
    LinearScores, Leaderboard = (list(t) for t in zip(*sorted(zip(LinearScores, Leaderboard),reverse=True)))
    for j in range(N, len(Leaderboard)):
        if LinearScores[j]<LinearScores[N-1]:
            for i in range(len(Leaderboard)-j):
                Leaderboard.pop()
            break
    return Leaderboard

if __name__ == '__main__':
    x = '''LAST ALST TLLT TQAS
0 71 87 101 113 158 184 188 259 271 372
2'''
    inlines = x.split("\n")
    Leaderboard = inlines[0].split(" ")
    res = " ".join(Trim(Leaderboard, inlines[1], int(inlines[2])))
    print(res)