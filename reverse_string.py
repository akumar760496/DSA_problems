def reverseString(txt: str) -> str:
    words = txt.split()
    words.reverse()
    return " ".join(words)

def rev_str_without_function(txt:str):
    words = txt.split()
    rev_word = []

    for i in range(len(words)-1 , -1 ,-1):
        rev_word.append(words[i])

    return " ".join(rev_word)

if __name__ == "__main__":
    s = "the sky is blue"
    #print(reverseString(txt=s))
    print(rev_str_without_function(txt=s))
    # Output: blue is sky the