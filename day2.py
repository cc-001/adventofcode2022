import os

shape_score = {'X':1,'Y':2,'Z':3,'A':1,'B':2,'C':3}

outcome = {'AX':3,'AY':6,'AZ':0,'BX':0,'BY':3,'BZ':6,'CX':6,'CY':0,'CZ':3}

score_part2 = {'X':0,'Y':3,'Z':6}
shape_part2 = {'AX':'C','AY':'A','AZ':'B','BX':'A','BY':'B','BZ':'C','CX':'B','CY':'C','CZ':'A'}

def day2_part1(input:str):
    total_score = 0
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            tmp = line.split(' ')
            p2 = tmp[1].strip()
            round_score = outcome[tmp[0]+p2] + shape_score[p2]
            total_score = total_score + round_score
    return total_score
    
def day2_part2(input:str):
    total_score = 0
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            tmp = line.split(' ')
            p2 = tmp[1].strip()
            shape = shape_part2[tmp[0]+p2]
            round_score = score_part2[p2] + shape_score[shape]
            total_score = total_score + round_score
    return total_score  

# 11475
#print(day2_part1('day2_input.txt'))
# 16862
print(day2_part2('day2_input.txt'))