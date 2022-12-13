import ast
from functools import cmp_to_key

def ordered(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif r < l:
            return 1
        return 0
    elif isinstance(l, list) and isinstance(r, list):
        if len(l) == 0:
            if len(r) == 0:
                return 0
            return -1
        elif len(r) == 0:
            return 1
        result = ordered(l[0], r[0])
        if result != 0:
            return result
        return ordered(l[1:], r[1:])
    elif isinstance(l, list):
        return ordered(l, [r])
    elif isinstance(r, list):
        return ordered([l], r)
    assert False

def day13Part1(input:str):
    sum = 0
    with open(input) as f:
        lines = list(map(lambda x: x.rstrip('\n'), f.readlines()))
        pair_index = 1
        i = 0
        while i < len(lines):
            if len(lines[i]) == 0:
                i += 1
                continue
            l = ast.literal_eval(lines[i]) # lol
            r = ast.literal_eval(lines[i+1])
            if ordered(l, r) < 0:
                sum += pair_index
            pair_index += 1
            i += 2
    return sum
    
def day13Part2(input:str):
    with open(input) as f:
        lines = list(map(lambda x: x.rstrip('\n'), f.readlines()))
        packets = [[2],[6]]
        for line in lines:
            if len(line) == 0:
                continue
            packets.append(ast.literal_eval(line))
    ps = sorted(packets, key=cmp_to_key(ordered))
    d1 = ps.index([2])+1
    d2 = ps.index([6])+1
    return d1 * d2
    
#print(day13Part1('day13_test0.txt'))
#6395
#print(day13Part1('day13_input0.txt'))
#print(day13Part2('day13_test0.txt'))
print(day13Part2('day13_input0.txt'))