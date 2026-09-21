def validAnagramBrutForce(text1:str , text2:str) -> bool:
    if (len(text2) != len(text1)):
        return False

    counter = {}

    for ch in text1:
        counter[ch] = counter.get(ch,0) + 1

    for ch in text2:
        if ch not in counter or counter[ch] == 0:
            return False
        counter[ch] -= 1

    return True


if __name__ == "__main__":
    s = "anagramf"
    t = "nagaram"
    print(validAnagramBrutForce(text1= s , text2= t))


