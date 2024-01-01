def string_hash(s):
    cur = 0
    for c in s:
        cur = ((cur+ord(c))*17)%256
    return cur

with open('input.txt') as infile:
    steps = infile.read().rstrip('\n').split(',')

boxes = {}
for i in range(256):
    boxes[i] = []

for step in steps:
    if step[-1] == '-':
        label = step[:-1]
        box = boxes[string_hash(label)]
        for record in box:
            if record[0] == label:
                box.remove(record)
                break
    else:
        label, num = step.split('=')
        box = boxes[string_hash(label)]
        found = False
        for record in box:
            if record[0] == label:
                found = True
                record[1] = num
                break
        if not found:
            box.append([label, num])

result = 0
for boxnum in range(256):
    box = boxes[boxnum]
    for slotnum in range(len(box)):
        result += (boxnum+1)*(slotnum+1)*int(box[slotnum][1])

print(result)
