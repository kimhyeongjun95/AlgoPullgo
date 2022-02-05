from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0] * 101 for i in range(101)]
    cX, cY = 2 * characterX, 2 * characterY
    iX, iY = 2 * itemX, 2 * itemY
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1, 2*x2+1):
            for j in range(2*y1, 2*y2+1):
                board[i][j] = 1
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1+1, 2*x2):
            for j in range(2*y1+1, 2*y2):
                board[i][j] = 0
    
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0] * 101 for i in range(101)]
    visited[cX][cY] = 1
    queue = deque([(cX, cY)])
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (iX, iY):
            return (visited[x][y] - 1) // 2
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < 101 and 0 <= ny < 101 and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] +1
                queue.append((nx, ny))
        
    return answer
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
print(solution(rectangle, 1, 3, 7, 8))