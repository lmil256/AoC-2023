def string_hash(s):
    cur = 0
    for c in s:
        cur = ((cur+ord(c))*17)%256
    return cur

with open('input.txt') as infile:
    steps = infile.read().rstrip('\n').split(',')

result = 0
for step in steps:
    result += string_hash(step)

print(result)
