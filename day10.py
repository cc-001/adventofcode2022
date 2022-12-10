# assume possible reuse in future days

import math
from PIL import Image
import pytesseract

class Emulator:    
    PIXELS = 40
    ROWS = 6
    
    def __init__(self):
        self.cycle = 1
    
        self.cur_inst = ''
        self.cur_pipe = 0
    
        self.x = 1
        self.x_hist = [1]
        self.pipe = {'addx':2, 'noop':1}
        
        self.crt = []
        for i in range(0, self.ROWS):
            self.crt.append(['.']*self.PIXELS)
        
    def run(self, code):
        for inst in code:
            toks = inst.split(' ')
            inst = toks[0].lower()
            
            self.cur_inst = inst
            self.cur_pipe = 1
            while self.cur_pipe > 0:
                #self.printState()
                
                tmp = self.cycle - 1
                row = math.floor(tmp / self.PIXELS)
                pixel = tmp - row * self.PIXELS
                dx = self.x - pixel
                if abs(dx) <= 1:
                    self.crt[row][pixel] = '#'
                else:
                    self.crt[row][pixel] = '.'
                #print('s cyc:{} r:{} p:{} x:{} {}'.format(self.cycle, row, pixel, self.x, self.crt[row][pixel]))
                    
                if self.pipe[self.cur_inst] == self.cur_pipe:
                    if self.cur_inst == 'addx':
                        self.x += int(toks[1])
                        self.cur_pipe = -1
                    elif self.cur_inst == 'noop':
                        self.cur_pipe = -1
                    else:
                        print(self.cur_inst, self.cur_pipe)
                        assert False
                
                #print('e_cyc:{}'.format(self.x))
                
                self.x_hist.append(self.x)          
                self.cycle += 1
                self.cur_pipe += 1
                
    def printState(self):
        print('{} x={}'.format(self.cycle, self.x))
        
    def printCRT(self):
        for row in self.crt:
            print(''.join(row))
            
    def imageCRT(self, scale=12):
        im = Image.new('RGB', (self.PIXELS+2, self.ROWS+2), color=(255,255,255))
        for y in range(0, self.ROWS):
            for x in range(0, self.PIXELS):
                if self.crt[y][x] == '#':
                    im.putpixel((x+1, y+1), (0,0,0))
        return im.resize((im.width*scale, im.height*scale))
                
    def signalStrength(self, cycle_count:int):
        return self.x_hist[cycle_count-1] * cycle_count
        
    def runFile(self, file_name):
        code = []
        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                code.append(line.rstrip('\n').strip())
        self.run(code)
            
def day10Part1(input:str):
    emu = Emulator()
    emu.runFile(input)
    
    sum = 0
    for count in range(20, 240, 40):
        strength = emu.signalStrength(count)
        sum += strength
    return sum
    
def day10Part2(input:str):
    emu = Emulator()
    emu.runFile(input)
    im = emu.imageCRT();
    print(pytesseract.image_to_string(im, config=r'--psm 8'))
    
if __name__ == "__main__":
    #print(day10Part1('day10_test0.txt'))
    #14520
    #print(day10Part1('day10_input0.txt'))
    #day10Part2('day10_test0.txt')
    #PZBGZEJB
    day10Part2('day10_input0.txt')