import anytree
    
def day7(input:str, part2=False):
    cwd = None
    root = None
    
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            
            if line[0] == '$':    
                if line.find('cd') == 2:
                    dir = line.split(' ')[2]
                    if dir == '/':
                        assert root == None
                        cwd = anytree.Node('/', type='dir', size=0)
                        root = cwd
                    elif dir == '..':
                        cwd = cwd.parent
                    else:
                        for child in cwd.children:
                            if child.type == 'dir' and child.name == dir:
                                cwd = child
                                break;
            else:
                if line.find('dir') == 0:
                    dir = line.split(' ')[1]
                    new_dir = anytree.Node(dir, parent=cwd, type='dir', size=0)
                else:
                    toks = line.split(' ')
                    size = int(toks[0])
                    new_file = anytree.Node(toks[1], parent=cwd, type='file', size=size)
                    cwd.size += size
                    
    #print(anytree.RenderTree(root, style=anytree.AsciiStyle()).by_attr())
    for iter in anytree.PostOrderIter(root, filter_=lambda node: node.type == 'dir'):
        if iter.parent:
            iter.parent.size += iter.size
    
    if part2:
        unused = 70000000 - root.size
        delta = 30000000 - unused
        valid = []
        for iter in anytree.PostOrderIter(root, filter_=lambda node: node.type == 'dir'):
            if iter.size >= delta:
                valid.append(iter.size)
        valid.sort()
        return valid[0]
    else:
        sum = 0
        for iter in anytree.PreOrderIter(root, filter_=lambda node: node.type == 'dir' and node.size < 100000):
            sum += iter.size
        return sum
    
#print(day7('day7_test0.txt'))
#1086293
#print(day7('day7_input0.txt'))
#366028
print(day7('day7_input0.txt', True))