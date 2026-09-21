def checkValidPalindrome(text: str):
    cleaned = ''.join(ch for ch in text.lower() if ch.isalnum())
    ch_arry = list(cleaned)
    n = len(ch_arry)

    for i in range(n // 2):
        if ch_arry[i] != ch_arry[n - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    text = "A man, a plan, a canal: Panama"
    isValid = checkValidPalindrome(text=text)
    print(isValid)

