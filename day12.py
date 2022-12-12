
def shortest(graph, s, e, check_set):
    visited = []
    queue = [[s]]
    if s == e:
        return []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            conn = graph[node]
            for neighbor in conn:
                new_path = list(path)
                new_path.append(neighbor)
                if len(check_set):
                    if neighbor in check_set:
                        return new_path
                elif neighbor == e:
                    return new_path
                queue.append(new_path)
        visited.append(node)
    return []    

def check_nav(diff, part2):
    if part2:
        return (diff > 0 and diff == 1) or diff <= 0
    return (diff < 0 and diff == -1) or diff >= 0
    
def day12(input:str, part2=False):
    cells = []
    s = ''
    e = ''
    valid_starts = set()
    
    with open(input) as f:
        lines = f.readlines()
        row = 0
        for line in lines:
            line = line.rstrip('\n')
            cells.append([])
            col = 0
            for ch in line:
                if ch == 'S':
                    s = '{},{}'.format(row,col)
                    cells[-1].append('a')
                    valid_starts.add(s)
                elif ch == 'E':
                    e = '{},{}'.format(row,col)
                    cells[-1].append('z')
                else:
                    cells[-1].append(ch)
                    if ch == 'a':
                        valid_starts.add('{},{}'.format(row,col))
                col += 1
            row += 1
                
    graph = {}
    for i in range(0, len(cells)):
        for j in range(0, len(cells[0])):
            connected = []
            val = ord(cells[i][j])
            if i > 0: #up
                diff = val - ord(cells[i-1][j])
                if check_nav(diff, part2):
                    connected.append('{},{}'.format(i-1, j))
            if i < len(cells)-1: #down
                diff = val - ord(cells[i+1][j])
                if check_nav(diff, part2):
                    connected.append('{},{}'.format(i+1, j))
            if j > 0: #left
                diff = val - ord(cells[i][j-1])
                if check_nav(diff, part2):
                    connected.append('{},{}'.format(i, j-1))
            if j < len(cells[0])-1: #right
                diff = val - ord(cells[i][j+1])
                if check_nav(diff, part2):
                    connected.append('{},{}'.format(i, j+1))
            graph['{},{}'.format(i,j)] = connected
    
    path = []
    if part2:
        path = shortest(graph, e, '', valid_starts)
    else:
        path = shortest(graph, s, e, set())
    return len(path) - 1
    
#print(day12('day12_test0.txt'))
#520
#print(day12('day12_input0.txt'))
#print(day12('day12_test0.txt', True))
#508
print(day12('day12_input0.txt', True))