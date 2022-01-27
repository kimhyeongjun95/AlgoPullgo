def solution(n, s, a, b, fares):

    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0

    for fare in fares:
        i, j, cost = fare
        graph[i][j] = graph[j][i] = cost

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    ans = float('inf')
    for k in range(1, n+1):
        ans = min(ans, graph[s][k] + graph[k][a] + graph[k][b])

    return ans
