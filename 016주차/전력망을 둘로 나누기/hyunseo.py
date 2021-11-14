# 프로그래머스 전력망을 둘로 나누기

from collections import deque

def bfs(v, n, grid):
    cnt = 0
    
    queue = deque()
    queue.append(v)
    
    visited = [0 for _ in range(n+1)]
    visited[v] = 1
    
    while queue:
        v = queue.popleft()
        
        for w in grid[v]:
            if not visited[w]:
                visited[w] = 1
                queue.append(w)
                cnt += 1
    
    return cnt


def solution(n, wires):
    global answer
    
    # 인접 리스트
    grid = [[] for _ in range(n+1)]
    
    for i in range(n-1):
        grid[wires[i][0]].append(wires[i][1])
        grid[wires[i][1]].append(wires[i][0])
    
    # 하나씩 연결을 끊고 개수 확인
    for i in range(n-1):
        grid[wires[i][0]].remove(wires[i][1])
        grid[wires[i][1]].remove(wires[i][0])
            
        cnt_node1 = bfs(wires[i][0], n, grid)
        cnt_node2 = bfs(wires[i][1], n, grid)
        
        answer = min(answer, abs(cnt_node1 - cnt_node2))
        
        grid[wires[i][0]].append(wires[i][1])
        grid[wires[i][1]].append(wires[i][0])
    
    return answer


answer = float('inf')

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(9, wires)