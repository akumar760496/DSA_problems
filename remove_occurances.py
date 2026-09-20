def removeOccurances(s: str, part: str) -> str:
    while True:
        idx = s.find(part)
        if idx == -1:
            break
        s = s[:idx] + s[idx + len(part):]
    return s

if __name__ == "__main__":
    s = "daabcbaabcbc"
    part = "abc"
    print(removeOccurances(s=s, part=part))
