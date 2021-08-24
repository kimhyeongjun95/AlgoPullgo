import sys
input = sys.stdin.readline

def dfs(v):
    stack = []
    stack.append(v)
    result = []
    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            result.append(v)

            for w in range(1, V+1):
                if Graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

    return result

# input 받기
V = int(input())
E = int(input())
temp = []
for _ in range(E):
    temp += list(map(int, input().split()))

Graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]

for i in range(0, len(temp) - 1, 2):
    Graph[temp[i]][temp[i + 1]] = 1  # 인접한 노드 표기
    Graph[temp[i+1]][temp[i]] = 1  # 반대 방향도 표기(무방향 그래프이므로)

print(len(dfs(1))-1)
