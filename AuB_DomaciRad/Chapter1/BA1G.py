def hamming_distance(text1, text2):
    br = 0
    if len(text1)!=len(text2):
        return -1
    else:
        for i in range(0, len(text1)):
            if (text1[i] != text2[i]):
                br = br + 1
    return br


if __name__ == "__main__":
    text1 = "GGGCCGTTGGT"
    text2 = "GGACCGTTGAC"
    res = hamming_distance(text1, text2)
    print(res)