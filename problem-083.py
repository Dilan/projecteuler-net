# -*- coding: utf-8 -*-

# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
# by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


# data = [
    # [ (131),  673,  (234), (103), (18) ],
    # [ (201), (96),  (342),  965,  (150) ],
    # [ 630,   803,   746,   (422), (111) ],
    # [ 537,   699,   497,   (121),  956 ],
    # [ 805,   732,   524,   (37),  (331) ]
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
    data = read_data_from_file('data/p083_matrix.txt')
    
    # init empty
    result = []
    for row in data:
        result.append([None] * len(row))
    # init start point
    result[0][0] = data[0][0]
    
    queue = []
    queue.append((0,0))

    while len(queue):
        point_A = queue.pop(0)
        res_at_point_A = result[point_A[0]][point_A[1]]
        
        for direction in ['up', 'down', 'right', 'left']:
            point_B = move(direction, point_A, result)
            
            if point_B is not None:
                res_at_point_B = result[point_B[0]][point_B[1]]
                data_at_point = data[point_B[0]][point_B[1]]
                
                if res_at_point_B is None or res_at_point_B > (data_at_point + res_at_point_A):
                    result[point_B[0]][point_B[1]] = (data_at_point + res_at_point_A)
                    queue.append(point_B)
    
    return result[-1][-1]

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
