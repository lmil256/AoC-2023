def identical(sequence):
    val = sequence[0]
    for i in sequence[1:]:
        if i != val: return False
    return True

with open('input.txt') as infile:
    lines = infile.read().splitlines()

result = 0
for line in lines:
    seqs = [[int(x) for x in line.split(' ')]]
    while not identical(seqs[-1]):
        new_seq = []
        for i in range(len(seqs[-1]) - 1):
            new_seq.append(seqs[-1][i+1] - seqs[-1][i])
        seqs.append(new_seq)
    val = 0
    for seq in seqs[::-1]:
        val = seq[0] - val
    result += val

print(result)
