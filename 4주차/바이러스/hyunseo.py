def dfs(v):
    global cnt
    cnt += 1

    visited[v] = 1

    for w in range(1, V+1):
        if network[v][w] == 1 and visited[w] == 0:
            dfs(w)


V = int(input())
E = int(input())

network = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0]*(V+1)

# 1번 컴퓨터는 카운팅에 포함x
cnt = -1

for _ in range(E):
    i, j = map(int, input().split())
    network[i][j] = 1
    network[j][i] = 1

# 인접 행렬 확인
# for i in range(V+1):
#     print('{} | {}'.format(i, network[i]))

dfs(1)
print(cnt)