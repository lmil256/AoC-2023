import re

with open('input.txt') as infile:
    total = 0
    for line in infile:
        numlists = line[line.find(':')+2:-1].split(' | ')
        winning_nums = set(re.findall('\d+', numlists[0]))
        have_nums = set(re.findall('\d+', numlists[1]))
        num_matches = len(winning_nums & have_nums)
        if num_matches > 0:
            total += pow(2, num_matches-1)
    print(total)
