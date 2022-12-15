
def dir(x):
    if x < 0:
        return 1
    return -1
    
def get_key(x, y):
    return '{},{}'.format(x, y)
    
def load(input:str):
    cave = {}
    ymax = -1
    with open(input) as f:
        il = list(map(lambda x: x.rstrip('\n'), f.readlines()))
        for i in il:
            if len(i) == 0:
                continue
            line = []
            toks = i.split(' ')
            for tok in toks:
                if tok[0] == '-':
                    continue
                else:
                    coords = tok.split(',')
                    line.append([int(coords[0]), int(coords[1])])
                    if line[-1][1] > ymax:
                        ymax = line[-1][1]
                    if len(line) == 2:
                        dx = line[0][0] - line[1][0]
                        for x in range(abs(dx)+1):
                            cave[get_key(line[0][0] + x*dir(dx), line[0][1])] = '#'
                        dy = line[0][1] - line[1][1]
                        for y in range(abs(dy)+1):
                            cave[get_key(line[0][0], line[0][1] + y*dir(dy))] = '#'
                        line.pop(0)
    cave['ymax'] = ymax
    return cave

def blocked(cave, part1, x, y):
    in_cave = get_key(x, y) in cave
    if part1:
        return in_cave
    return in_cave or (y >= (cave['ymax']+2))
    
def sim(cave, s, part1):
    ymax = cave['ymax']
    count = 0
    it = s
    
    while True:
        if blocked(cave, part1, it[0], it[1]+1): #down
            if blocked(cave, part1, it[0]-1, it[1]+1): #dl
                if blocked(cave, part1, it[0]+1, it[1]+1): #dr
                    count += 1
                    if not part1 and it == s:
                        return count
                    cave[get_key(it[0], it[1])] = 'o'
                    it = s
                    continue
                else:
                    it = [it[0]+1, it[1]+1]
            else:
                it = [it[0]-1, it[1]+1]
        else:
            it = [it[0], it[1]+1]
        if part1:
            if it[1] >= ymax:
                return count
    
def day14(input:str, part1=True):
    cave = load(input)
    return sim(load(input), [500,0], part1)
    
#print(day14('day14_test0.txt'))
#779
#print(day14('day14_input0.txt'))
#print(day14('day14_test0.txt', False))
#27426
print(day14('day14_input0.txt', False))