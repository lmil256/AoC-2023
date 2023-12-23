import re

class Map():
    def __init__(self):
        self.records = []

    def is_empty(self):
        return len(self.records) == 0

    def add_record(self, record):
        if len(record) != 3:
            raise Exception()
        self.records.append([int(x) for x in record])

    def do_mapping(self, num):
        for record in self.records:
            if num >= record[1] and num < record[1] + record[2]:
                return record[0] + num - record[1]
        return num

    def get_dest_max(self):
        if self.is_empty(): return None
        highest = self.records[0][0] + self.records[0][2] - 1
        for record in self.records[1:]:
            curr = record[0] + record[2] - 1
            if curr > highest:
                highest = curr
        return highest

with open('input.txt') as infile:
    map_list = []
    seednums = [int(x) for x in re.findall('\d+', infile.readline())]
    for line in infile:
        # Start new map
        if line[0].isalpha():
            map_list.append(Map())
        elif line != '\n':
            map_list[-1].add_record(re.findall('\d+', line))

lowest = map_list[-1].get_dest_max()
for seed in seednums:
    num = seed
    for cur_map in map_list:
        num = cur_map.do_mapping(num)
    if num < lowest:
        lowest = num
        
print(lowest)
