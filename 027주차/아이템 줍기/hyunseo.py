# 프로그래머스 아이템 줍기

from collections import deque

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    border = set()
    inner = set()
    
    for lx, ly, rx, ry in rectangle:
        # 가로
        for x in range(lx*2, rx*2+1):
            for y in [ly*2, ry*2]:
                if (x, y) not in inner:
                    border.add((x, y))
        
        # 세로
        for y in range(ly*2, ry*2+1):
            for x in [lx*2, rx*2]:
                if (x, y) not in inner:
                    border.add((x, y))
        
        for x in range(lx*2+1, rx*2):
            for y in range(ly*2+1, ry*2):
                if (x, y) in border:
                    border.remove((x, y))
                inner.add((x, y))
    
    queue = deque()
    queue.append((characterX*2, characterY*2, 0))
    
    border.remove((characterX*2, characterY*2))
    
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y, dist = queue.popleft()
        if x == itemX*2 and y == itemY*2:
            return dist//2
        
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            
            if (nx, ny) in border:
                border.remove((nx, ny))
                queue.append((nx, ny, dist+1))


rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
print(solution(rectangle, 1, 3, 7, 8))