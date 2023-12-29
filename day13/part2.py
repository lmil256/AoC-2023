def main():
    with open('input.txt') as infile:
        patterns = [[]]
        for line in infile.read().splitlines():
            if line != '':
                patterns[-1].append(line)
            else:
                patterns.append([])

    result = 0
    for pattern in patterns:
        if (t := find_symmetry(pattern)) != -1:
            result += 100*(t+1)
        else:
            rotated_pattern = [[line[i] for line in pattern]
                                for i in range(len(pattern[0]))]
            result += find_symmetry(rotated_pattern)+1

    print(result)

# 0 - Strings are equal
# 1 - One character difference
# 2 - More than one character difference
def compare_strings(str1, str2):
    count = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            count += 1
            if count > 1:
                break
    return count

def find_symmetry(pattern):
    for i in range(len(pattern)-1):
        dist = compare_strings(pattern[i], pattern[i+1])
        if dist <= 1:
            a, b = i-1, i+2
            while a > -1 and b < len(pattern) and dist <= 1:
                dist += compare_strings(pattern[a], pattern[b])
                a -= 1
                b += 1
            if dist == 1:
                return i
    return -1

main()
