import math

import numpy as np

class Monkey:
    def add(a, b):
        return a + b
    def mul(a, b):
        return a * b
    def test(a, b):
        if a % b == 0:
            return True
        return False
        
    def __init__(self, name):
        self.items = []
        self.name = name
        self.inspects = 0
        
        self.fn = Monkey.add
        self.fn_input = -1
        
        self.test_input = 0
        self.test_t = -1
        self.test_f = -1

def parse(input:str):
    monkeys = []
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            if line.find('Monkey') >= 0:
                monkeys.append(Monkey(line.rstrip(':')))
            elif line.find('Starting items: ') >= 0:
                monkeys[-1].items = list(map(lambda x: int(x), line.split('Starting items: ')[1].split(', ')))
            elif line.find('Operation: new = old ') >= 0:
                toks = line.split(' ')
                if toks[-2] == '*':
                    monkeys[-1].fn = Monkey.mul
                else:
                    monkeys[-1].fn = Monkey.add
                if toks[-1] != 'old':
                    monkeys[-1].fn_input = int(toks[-1])
            elif line.find('Test:') >= 0:
                monkeys[-1].test_input = int(line.split(' ')[-1])
            elif line.find('If true:') >= 0:
                monkeys[-1].test_t = int(line.split(' ')[-1])
            elif line.find('If false:') >= 0:
                monkeys[-1].test_f = int(line.split(' ')[-1])
    return monkeys
                
def day11(input:str, rounds:int, div:int):
    monkeys = parse(input)
    
    product = 1
    for m in monkeys:
        product *= m.test_input
        
    for round in range(0, rounds):
        for m in monkeys:
            for worry_level in m.items:
                m.inspects += 1
                fn_input = m.fn_input
                if fn_input < 0:
                    fn_input = worry_level
                if div == 1:
                    worry_level = m.fn(worry_level, fn_input) % product
                else:
                    worry_level = math.floor(m.fn(worry_level, fn_input) / div)
                if Monkey.test(worry_level, m.test_input):
                    monkeys[m.test_t].items.append(worry_level)
                else:
                    monkeys[m.test_f].items.append(worry_level)
            m.items.clear()
    
    monkeys = sorted(monkeys, key=lambda x: x.inspects, reverse=True)
    return monkeys[0].inspects * monkeys[1].inspects
    
#print(day11('day11_test0.txt', 20, 3))
#76728
#print(day11('day11_input0.txt', 20, 3))
#print(day11('day11_test0.txt', 10000, 1))
#21553910156
print(day11('day11_input0.txt', 10000, 1))