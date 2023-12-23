import re
import bisect

class Map():
    def __init__(self):
        self.records = []

    def is_empty(self):
        return len(self.records) == 0

    def add_record(self, record):
        if len(record) != 3:
            raise Exception()
        # Keep records sorted
        bisect.insort(self.records, [int(x) for x in record])

    def do_mapping(self, num):
        for record in self.records:
            if num >= record[1] and num < record[1] + record[2]:
                return record[0] + num - record[1]
        return num

    def do_reverse_mapping(self, num):
        for record in self.records:
            if num >= record[0] and num < record[0] + record[2]:
                return record[1] + num - record[0]
        return num

    # Return values where the mapping changes
    def get_splits(self):
        result = []
        for record in self.records:
            result.append(record[0])
        result.append(self.records[-1][0] + self.records[-1][2])
        return result

with open('input.txt') as infile:
    map_list = []
    seed_list = [int(x) for x in re.findall('\d+', infile.readline())]
    seed_ranges = []
    for i in range(0, len(seed_list), 2):
        seed_ranges.append(range(seed_list[i], seed_list[i] + seed_list[i+1]))

    for line in infile:
        if line[0].isalpha():
            map_list.append(Map())
        elif line != '\n':
            map_list[-1].add_record(re.findall('\d+', line))

split_list = []
for i in range(len(map_list)):
    # Get splits for the current map
    temp_list = map_list[i].get_splits()
    # Map each split to a location
    for j in range(i+1, len(map_list)):
        temp_list = [map_list[j].do_mapping(x) for x in temp_list]
    split_list += temp_list
# Eliminate duplicates and sort
split_list = list(set(split_list))
split_list.sort()
# Reverse map each split
for i in split_list:
    num = i
    for cur_map in map_list[::-1]:
        num = cur_map.do_reverse_mapping(num)
    for r in seed_ranges:
        if num in r:
            print(i)
            exit()
