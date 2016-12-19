# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
# by only moving to the right and down, is indicated in bold red and is equal to 2427.

# data = [
    # [ (131),  673,   234,   103,   18 ],
    # [ (201), (96),  (342),  965,  150 ],
    # [ 630,   803,   (746), (422), 111 ],
    # [ 537,   699,   497,   (121), 956 ],
    # [ 805,   732,   524,   (37), (331)]
# ]

# Find the minimal path sum

import time
ti=time.time()

def to_int(str_list):
    return map(lambda s: int(s), str_list)

def solution():
    
    file_path = 'data/p081_matrix.txt'
    f = open(file_path, 'r')
    lines = f.read().strip().split('\n')

    data = map(lambda line:to_int(line.split(',')), lines)
    
    def get_top(point):
        x,y = point
        if x > 0 and x < len(data):
            return (x-1, y)
        return None

    def get_bottom(point):
        x,y = point
        if x >= 0 and x < len(data)-1:
            return (x+1, y)
        return None

    def get_left(point):
        x,y = point
        if y > 0 and y < len(data[x]):
            return (x, y-1)
        return None

    def get_right(point):
        x,y = point
        if y >= 0 and y < len(data[x])-1:
            return (x, y+1)
        return None

    result = []
    for item in data:
        result.append(map(lambda i:None, item))

    queue = [(0,0)]

    while len(queue):
        point = queue.pop(0)
        x,y =  point

        if result[x][y] is not None:
            continue
        
        top = get_top(point)
        left = get_left(point)
        
        best = 0
        if top is not None and left is not None:
            if result[top[0]][top[1]] > result[left[0]][left[1]]:
                best = result[left[0]][left[1]]
            else:
                best = result[top[0]][top[1]]
        elif top is not None:
            best = result[top[0]][top[1]]
        elif left is not None:
            best = result[left[0]][left[1]]
        
        result[x][y] = best + data[x][y]
        
        if get_right(point) is not None:
            queue.append(get_right(point))
        
        if get_bottom(point) is not None:
            queue.append(get_bottom(point))
    
    return result[len(result)-1][len(result[0])-1]

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
