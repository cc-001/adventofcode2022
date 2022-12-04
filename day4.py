
def make_set(input:str):
    x = set()
    nums = input.split('-')
    for i in range(int(nums[0]), int(nums[1])+1):
        x.add(i)
    return x
    
def day4(input:str, part2 = False):
    count = 0
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            secs = line.split(',')
            a = make_set(secs[0])
            b = make_set(secs[1])
            inter = a.intersection(b)
            if part2:
                if len(inter) > 0:
                    count = count + 1
            else:
                inter_len = len(inter)
                if inter_len == len(a) or inter_len == len(b):
                    count = count + 1
    return count
    
#print(day4('day4_test0.txt'))
#485
#print(day4('day4_input0.txt'))
#print(day4('day4_test0.txt', True))
print(day4('day4_input0.txt', True))