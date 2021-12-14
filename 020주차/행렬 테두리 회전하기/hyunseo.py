# 프로그래머스 행렬 테두리 회전하기

def solution(rows, columns, queries):
    numbers = [[columns*r + (c+1) for c in range(columns)] for r in range(rows)]
    
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오 아 왼 위
    answer = []
    
    for x1, y1, x2, y2 in queries:
        way = 0
        x = x1 - 1
        y = y1 - 1
        curr = numbers[x][y]
        min_num = curr
        
        while way < 4:
            nx, ny = x+dxy[way][0], y+dxy[way][1]
            
            if x1-1 <= nx <= x2-1 and y1-1 <= ny <= y2-1:
                curr, numbers[nx][ny] = numbers[nx][ny], curr
                min_num = min(min_num, curr)
                x, y = nx, ny
            else:
                way += 1
                
        answer.append(min_num)
        
    return answer