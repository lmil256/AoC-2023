import re

num_matches = []

def count(cardno):
    total = 1
    for i in range(num_matches[cardno]):
        total += count(cardno+i+1)
    return total
    
with open('input.txt') as infile:
    for line in infile:
        numlists = line[line.find(':')+2:-1].split(' | ')
        winning_nums = set(re.findall('\d+', numlists[0]))
        have_nums = set(re.findall('\d+', numlists[1]))
        num_matches.append(len(winning_nums & have_nums))

total = 0
for i in range(len(num_matches)):
    total += count(i)
print(total)
