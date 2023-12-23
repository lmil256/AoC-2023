import math
import re

with open('input.txt') as infile:
    lines = infile.read().splitlines()
    time = int(''.join(re.findall('\d+', lines[0])))
    record = int(''.join(re.findall('\d+', lines[1])))

# Even easier :P
foo = math.sqrt(time**2 - 4 * record)
time1 = (time - foo) / 2
time2 = (time + foo) / 2
print(math.ceil(time2) - math.floor(time1) - 1)
