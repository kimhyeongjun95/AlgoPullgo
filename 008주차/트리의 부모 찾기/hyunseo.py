# 백준 11725 트리의 부모 찾기
def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        for w in graph[v]:
            if result[w] == 0:
                stack.append(w)
                result[w] = v


N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

result = [0 for _ in range(N+1)]
dfs(1)

for number in result[2:]:
    print(number)