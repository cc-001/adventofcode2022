# write code for C input for online compiler
with open('day1_input0.txt') as f:
    vals = []
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if len(line) > 0:
            vals.append(int(line))
        else:
            vals.append('-1')
    print('const long Input[] = {' + ','.join(map(str, vals)) + '};')