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

# Find vertical symmetry
def find_symmetry(pattern):
    for i in range(len(pattern)-1):
        # If one line matches the following line
        if pattern[i] == pattern[i+1]:
            mismatch = False
            a, b = i-1, i+2
            # Look for mismatches across the line of symmetry
            while a > -1 and b < len(pattern) and not mismatch:
                if pattern[a] != pattern[b]:
                    mismatch = True
                a -= 1
                b += 1
            if not mismatch:
                return i
    return -1

main()
