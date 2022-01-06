from collections import deque

def bfs(room, x, y):
    deq = deque([(x, y, 0)])
    visited = [[0 for _ in range(5)] for _ in range(5)]
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while deq:
        x, y, d = deq.popleft()
        visited[x][y] = True
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                
                if room[nx][ny] == 'P':
                    if nd <= 2:
                        return 0

                elif room[nx][ny] == 'O':
                    if nd == 1:
                        deq.append((nx, ny, nd))
    return 1

def solution(places):
    answer = []
    for room in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if not bfs(room, i, j):
                        answer.append(0)
                        flag = True
                        break
            if flag:
                break
        else:
            answer.append(1)

    return answer

places = [["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]] 
print(solution(places))