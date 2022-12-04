
def make_set(input:str):
    x = set()
    for ch in input:
        x.add(ch)
    return x
    
def get_prioirty(input):
    if input.isupper():
        return 27 + ord(input) - ord('A')
    else:
        return 1 + ord(input) - ord('a')
        
def day3_part1(input:str):
    sum = 0
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            mid = int(len(line) / 2)
            left = make_set(line[:mid])
            right = make_set(line[mid:])
            inter = left.intersection(right)
            assert len(inter) == 1
            for dup in inter:
                print(dup + ' ' + str(get_prioirty(dup)))
                sum = sum + get_prioirty(dup)
    return sum
    
def day3_part2(input:str):
    sum = 0
    with open(input) as f:
        group = []
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            group.append(make_set(line))
            if len(group) == 3:
                inter = group[0].intersection(group[1]).intersection(group[2])
                assert len(inter) == 1
                for dup in inter:
                    print(dup + ' ' + str(get_prioirty(dup)))
                    sum = sum + get_prioirty(dup)
                group = []
    return sum
    
#print(day3_part1('day3_test0.txt'))
#7821
#print(day3_part1('day3_input0.txt'))
#print(day3_part2('day3_test0.txt'))
#2752
print(day3_part2('day3_input0.txt'))