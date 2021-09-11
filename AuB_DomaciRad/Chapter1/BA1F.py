def diff_C_and_G(text, k):
    br = 0
    br1 = 0
    for i in range(0, k + 1, 1):
        if (text[i] == 'C'):
            br = br + 1
        if (text[i] == 'G'):
            br1 = br1 + 1
    return (br1 - br)


def skew_min(text):
    rez = dict()
    rez[0] = 0
    for i in range(0, len(text), 1):
        if (i == 0):
            if (text[0] == 'C'):
                rez[0] = -1
            if (text[0] == 'G'):
                rez[0] = 1
        else:
            rez[i] = diff_C_and_G(text, i)
    pozicije = [k for k in range(0, len(rez)) if rez[k] == min(rez.values())]
    return pozicije


if __name__ == "__main__":
    text = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
    res = skew_min(text)
    print([res[k] + 1 for k in range(0, len(res))])