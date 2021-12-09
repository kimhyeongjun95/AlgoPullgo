# 프로그래머스 가장 먼 노드
# 1번 노드에서 가장 멀리 떨어진 노드 몇개인지 return
from collections import deque
def bfs(nodes, n):
    queue = deque([])
    visited = [-1] * (n+1)
    visited[1] = 0
    queue.append(1)
    while queue:
        see = queue.popleft()

        for i in nodes[see]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[see] + 1
    
    return visited

def solution(n, edge):
    global visited
    nodes = [[] for _ in range(n+1)]
    for one, two in edge:
        nodes[one].append(two)
        nodes[two].append(one)
    result = bfs(nodes, n)
    answer = result.count(max(result))
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3

