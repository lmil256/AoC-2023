def getfirstdigit(s):
    for c in s:
        if c.isdigit():
            return c
    return None

with open('input.txt') as infile:
    total = 0
    for line in infile:
        total += int(getfirstdigit(line) + getfirstdigit(line[::-1]))
    print(total)
