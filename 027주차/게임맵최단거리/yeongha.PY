from collections import deque
dxy = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(maps, n, m):
    deq = deque([(0, 0)])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < n and -1 < ny < m and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                
                if nx == n-1 and ny == m-1:
                    return visited[nx][ny]

                deq.append((nx, ny))

    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return bfs(maps, n, m)


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))