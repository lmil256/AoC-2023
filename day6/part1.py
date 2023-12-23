import math
import re

with open('input.txt') as infile:
    lines = infile.read().splitlines()
    times = [int(x) for x in re.findall('\d+', lines[0])]
    records = [int(x) for x in re.findall('\d+', lines[1])]

total = 1

'''
time = time_held + time_moving
distance = time_held * time_moving = time_held * (time - time_held)
         = -time_held**2 + time * time_held
'''
for time, record in zip(times, records):
    # Use the quadratic formula to find the hold times that match the record
    foo = math.sqrt(time**2 - 4 * record)
    time1 = (time - foo) / 2
    time2 = (time + foo) / 2
    total *= (math.ceil(time2) - math.floor(time1) - 1)
print(total)
