from parse import parse
from functools import cmp_to_key

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + 1
    
def clamp(v, a, b):
    if v < a:
        return a
    if v > b:
        return b
    return v

#dumbest algo ever
def part1(s, r, row):
    ex = set()
    for i in range(0, len(s)):
        y = s[i][1]
        delta = abs(y-row)
        if delta <= r[i]:
            rem = r[i] - delta
            for j in range(-rem+1, rem):
                ex.add('{},{}'.format(s[i][0]+j, row))
    return ex
    
def compare(a, b):
    t = a[0] - b[0]
    if t == 0:
        return a[1] - b[1]
    return t
        
#sort pairs on a row such that for same x, open (0) < close (1)
#get to 0 count and then check for a gap of exactly 1
#still slow, like ~1m, part1 is 8s on same machine though so w/e
def gap(ranges):
    pairs = []
    for r in ranges:
        pairs.append([r[0], 0])
        pairs.append([r[1], 1])
    pairs = sorted(pairs, key=cmp_to_key(compare))
    count = 0
    for i in range(0, len(pairs)):
        x = pairs[i][0]
        if pairs[i][1] == 0:
            count += 1
        else:
            count -= 1
        if count == 0:
            if i+1 < len(pairs):
                if pairs[i+1][0] - x > 1:
                    return x+1
        
def part2(s, r, cmin, cmax):
    for row in range(cmin, cmax):
        ranges = []
        for i in range(0, len(s)):
            y = s[i][1]
            delta = abs(y-row)
            if delta <= r[i]:
                rem = r[i] - delta
                x = s[i][0]
                rmin = clamp(-rem+1 + x, cmin, cmax)
                rmax = clamp(rem-1 + x, cmin, cmax)
                if rmin <= rmax:
                    ranges.append([rmin, rmax])
        found = gap(ranges)
        if found:
            return found * 4000000 + row
    
def load(input:str):
    s = []
    r = []
    beacons = set()
    with open(input) as f:
        lines = list(map(lambda x: x.rstrip('\n').strip(), f.readlines()))
        for line in lines:
            p = parse('Sensor at x={}, y={}: closest beacon is at x={}, y={}', line)
            s.append([int(p[0]), int(p[1])])
            b = [int(p[2]), int(p[3])]
            beacons.add('{},{}'.format(b[0], b[1]))
            r.append(dist(s[-1], b))
    return s, r, beacons

def day15Part1(input:str, x:int):
    s, r, beacons = load(input)            
    return len(part1(s, r, x).difference(beacons))
    
def day15Part2(input:str, cmin:int, cmax:int):
    s, r, beacons = load(input)            
    return part2(s, r, cmin, cmax)
    
#print(day15Part1('day15_test0.txt', 10))
#4861076
#slow
#print(day15Part1('day15_input0.txt', 2000000))
#print(day15Part2('day15_test0.txt', 0, 20))
#10649103160102
print(day15Part2('day15_input0.txt', 0, 4000000))