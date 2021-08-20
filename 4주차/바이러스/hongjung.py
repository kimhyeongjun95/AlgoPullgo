import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
connection = [list(map(int, sys.stdin.readline().split())) for _ in range(E)] # 노드와 간선 묶음 리스트를 크게 하나의 리스트로 묶어줌

def dfs(v):
    stack = []
    result = [] # 최종 경로를 위한 리스트

    stack.append(v)
    while stack:
        v = stack.pop()
        if visited[v] == 0: # 만약 v가 방문체크가 되어있지 않다면
            visited[v] = 1 # 방문체크
            result.append(v) # 최종경로에 추가
        
        for w in range(1, V+1):
            if graph[v][w] == 1 and visited[w] == 0: # v에 연결된 w를 찾아 스택에 추가
                stack.append(w)
        
    if result: # 1은 바이러스 감염 노드의 수에서 제외이므로 -1
        return len(result) - 1
    else:
        return 0


graph = [[0] * (V+1) for _ in range(V+1)] # 빈 그래프 만들어 주기
for line in connection: # 양방향으로 전치행렬로 저장
    graph[line[0]][line[1]] = 1
    graph[line[1]][line[0]] = 1

visited = [0 for _ in range(V+1)] # 방문체크를 위한 리스트

print(dfs(1))