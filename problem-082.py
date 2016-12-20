# -*- coding: utf-8 -*-

# The minimal path sum in the 5 by 5 matrix below, 
# by starting in any cell in the left column and finishing in any cell in the right column, 
# and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

# data = [
    # [ 131,   673,  (234), (103), (18)],
    # [ (201), (96), (342),  965,  150 ],
    # [ 630,   803,   746,   422,  111 ],
    # [ 537,   699,   497,   121,  956 ],
    # [ 805,   732,   524,    37,  331 ]
# ]

import time
ti=time.time()

def read_data_from_file(file_path):
    f = open(file_path, 'r')
    lines = f.read().strip().split('\n')
    def to_int(str_list):
        return map(lambda s: int(s), str_list)
    return map(lambda line:to_int(line.split(',')), lines)

def move(direction, point, matrix):
    next_point = {
        'up':    (point[0]-1, point[1]),
        'down':  (point[0]+1, point[1]),
        'left':  (point[0],   point[1]-1),
        'right': (point[0],   point[1]+1)
    }[direction];

    if (next_point[0] >= 0 and next_point[0] < len(matrix) and 
            next_point[1] >= 0 and next_point[1] < len(matrix[next_point[0]])):
        return (next_point[0],next_point[1])
    return None

def get(point, matrix):
    return matrix[point[0]][point[1]]

def solution():
    data = read_data_from_file('data/p082_matrix.txt')
    
    result = [] # init
    for x, item in enumerate(data):
        result.append([])
        for y, s in enumerate(item):
            result[x].extend([ s if y == 0 else 0 ])
    
    max_val = len(data)
    for y in range(1, max_val):
        for x in range(0, max_val):
            lp = move('left', (x,y), data)
            result[x][y] = get(lp, result) + get((x,y), data)
        
        for x in range(0, max_val-1):
            dp = move('down', (x,y), data)
            current = get((x,y), result)
            
            jump_down_cost =  get(dp, data) + current
            
            if jump_down_cost < get(dp, result):
                # print 'down - (x,y)', (x,y), 'to', dp
                result[dp[0]][dp[1]] = jump_down_cost
        
        for x in range(max_val-1, 0, -1):
            up = move('up', (x,y), data)
            current = get((x,y), result)
            
            jump_up_cost = get(up, data) + current
            
            if jump_up_cost < get(up, result):
                result[up[0]][up[1]] = jump_up_cost

    return min(map(lambda item: item[-1], result))

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
