from collections import defaultdict

def hash_coord(coord):
    return '{},{}'.format(coord[0], coord[1])
    
def sign(x):
    if x > 0:
        return 1
    else:
        return -1
        
def move_knot(p, c):
    xd = p[0] - c[0]
    assert abs(xd) <= 2
    
    yd = p[1] - c[1]
    assert abs(yd) <= 2
    
    if yd == 0:
        # same row
        if xd > 1:
            c[0] += 1
        elif xd < -1:
            c[0] -= 1
    elif xd == 0:
        # same col
        if yd > 1:
            c[1] += 1
        elif yd < -1:
            c[1] -= 1
    else:
        # diag
        if abs(xd) == abs(yd) == 2:
            # happens part 2
            c[0] += sign(xd)
            c[1] += sign(yd)
        elif abs(yd) == 2:
            if yd > 1:
                c[0] += sign(xd)
                c[1] += 1
            else:
                c[0] += sign(xd)
                c[1] -= 1
        elif abs(xd) == 2:
            if xd > 1:
                c[0] += 1
                c[1] += sign(yd)
            else:
                c[0] -= 1
                c[1] += sign(yd)

def draw(h, k):
    for j in range(-10, 10):
        row = ''
        for i in range(-10, 10):
            if h[0] == i and h[1] == j:
                row += 'H'
            else:
                blank = True
                index = 0
                for c in k:
                    index += 1
                    if c[0] == i and c[1] == j:
                        row += str(index)
                        blank = False
                        break
                if blank:
                    row += '.'
        print(row)
    print('\n')
                    
def day9_2(input:str, knots:int):
    h = [0, 0]
    k = []
    for i in range(0, knots):
        k.append([0, 0])

    visited = defaultdict(int)
    visited[hash_coord(h)] = 1
    
    with open(input) as f:
        rows = f.readlines()
        for row in rows:
            row = row.rstrip('\n')
            toks = row.split(' ')
            num = int(toks[1])
            dir = toks[0]
            
            for move in range(0, num):                
                if dir == 'L':
                    h[0] -= 1
                elif dir == 'R':
                    h[0] += 1
                elif dir == 'U':
                    h[1] -= 1
                elif dir == 'D':
                    h[1] += 1
                
                for i in range(0, knots):
                    if i == 0:
                        move_knot(h, k[0])
                    else:
                        move_knot(k[i-1], k[i])

                visited[hash_coord(k[-1])] += 1
    return len(visited)
    
#print(day9_2('day9_test0.txt', 1))
#6406
#print(day9_2('day9_input0.txt', 1))
#print(day9_2('day9_test0.txt', 9))
#print(day9_2('day9_test1.txt', 9))
#2643
print(day9_2('day9_input0.txt', 9))