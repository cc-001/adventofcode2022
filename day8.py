    
def day8(input:str, part2=False):
    rows = []
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            rows.append(list(map(lambda x: int(x), line)))
    
    row_len = len(rows)
    col_len = len(rows[0])
    max_score = -1
    
    count = 0
    for i in range(0, row_len):
        if i == 0 or i == row_len - 1:
            count += row_len
            continue
        for j in range(0, col_len):
            if j == 0 or j == col_len - 1:
                count += 1
            else:
                height = rows[i][j]
                
                vis = True
                scores = [0,0,0,0]
                for k in range(j - 1, -1, -1):
                    scores[0] += 1
                    if rows[i][k] >= height:
                        vis = False
                        break
                if vis and not part2:
                    count += 1
                    continue
                
                vis = True                
                for k in range(j + 1, col_len):
                    scores[1] += 1
                    if rows[i][k] >= height:
                        vis = False
                        break
                if vis and not part2:
                    count += 1
                    continue
                
                vis = True                
                for k in range(i - 1, -1, -1):
                    scores[2] += 1
                    if rows[k][j] >= height:
                        vis = False
                        break
                if vis and not part2:
                    count += 1
                    continue
                
                vis = True                
                for k in range(i + 1, row_len):
                    scores[3] += 1
                    if rows[k][j] >= height:
                        vis = False
                        break
                if vis and not part2:
                    count += 1
                    continue
                    
                final_score = scores[0]*scores[1]*scores[2]*scores[3]
                if final_score > max_score:
                    max_score = final_score
    
    if part2:
        return max_score
    return count
    
#print(day8('day8_test0.txt'))
#1779
#print(day8('day8_input0.txt'))
#print(day8('day8_test0.txt', True))
#172224
print(day8('day8_input0.txt', True))