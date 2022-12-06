
def check_marker(input):
    found = set()
    for ch in input:
        if ch in found:
            return -1
        found.add(ch)
    return len(found)
    
def day6_algo(input:str, length = 4):
    window = []
    for i in range(0, len(input)):
        if len(window) == length:
            del window[0]
        window.append(input[i])
        if check_marker(window) == length:
            return i + 1
    return -1
    
def day6(file:str, length = 4):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            return day6_algo(line, length)
    return -1

assert day6_algo('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert day6_algo('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert day6_algo('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert day6_algo('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert day6_algo('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

#1757
#print(day6('day6_input0.txt'))

message_length = 14

assert day6_algo('mjqjpqmgbljsphdztnvjfqwrcgsmlb', message_length) == 19
assert day6_algo('bvwbjplbgvbhsrlpgdmjqwftvncz', message_length) == 23
assert day6_algo('nppdvjthqldpwncqszvftbrmjlhg', message_length) == 23
assert day6_algo('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', message_length) == 29
assert day6_algo('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', message_length) == 26

#2950
print(day6('day6_input0.txt', message_length))