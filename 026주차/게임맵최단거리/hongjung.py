from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    graph = [[-1 for _ in range(n)] for _ in range(m)]
    queue = deque([[0, 0]])
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    graph[0][0] = 1
    while queue:
        i, j = queue.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < m and 0 <= nj < n and maps[ni][nj] == 1:
                if graph[ni][nj] == -1:
                    graph[ni][nj] = graph[i][j] + 1
                    queue.append([ni, nj])

    answer = graph[m-1][n-1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))