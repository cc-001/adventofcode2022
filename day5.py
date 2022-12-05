import re

def day5(input:str, part2 = False):
    stacks = {}
    pat = re.compile('move (\d+) from (\d+) to (\d+)')
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            
            found_stack = False
            for i in range(0, len(line)):
                ch = line[i]
                val = ord(ch)
                if val >= ord('A') and val <= ord('Z'):
                    index = int((i - 1) / 4) + 1
                    if index not in stacks:
                        stacks[index] = []
                    stacks[index].insert(0, ch)
                    found_stack = True
            
            if found_stack == False:
                m = pat.match(line)
                if m:
                    num = int(m.group(1))
                    from_stack = int(m.group(2))
                    to_stack = int(m.group(3))
                    if part2:
                        stacks[to_stack].extend(stacks[from_stack][-num:])
                        stacks[from_stack] = stacks[from_stack][:-num]
                    else:
                        for i in range(0, num):
                            stacks[to_stack].append(stacks[from_stack].pop())
                    
    out = ''
    for i in sorted(stacks.keys()):
        out = out + stacks[i].pop()
    return out
    
#print(day5('day5_test0.txt'))
#CVCWCRTVQ
#print(day5('day5_input0.txt'))
#print(day5('day5_test0.txt', True))
#CNSCZWLVT
print(day5('day5_input0.txt', True))