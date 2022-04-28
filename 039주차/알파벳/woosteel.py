R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]

visited = [False for _ in range(26)]

ans = 0

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    
    for i in range(4):
        next_x, next_y = x + dir_x[i], y + dir_y[i]
        if 0 <= next_x < R and 0 <= next_y < C and not visited[ord(graph[next_x][next_y])-65]:
            visited[ord(graph[next_x][next_y])-65] = True
            dfs(next_x, next_y, cnt + 1)
            visited[ord(graph[next_x][next_y])-65] = False
    return

visited[ord(graph[0][0])-65] = True
dfs(0, 0, 1)

print(ans)