from collections import deque, defaultdict
    
def solution(n, wires):
    def bfs(n):
        deq = deque()
        deq.append(1)
        visited.append(1)

        while deq:
            v = deq.popleft()
            for i in node[v]:
                if i not in visited:
                    deq.append(i)
                    visited.append(i)
                
    answer = 99999
    n1 = 0
    for i in range(len(wires)):
        node = defaultdict(list)
        for item in wires[:i]+wires[i+1:]:
            n1, n2 = item
            node[n1].append(n2)
            node[n2].append(n1)
        visited=[]
        bfs(n1)
        answer = min(answer, abs(len(visited)-(n-len(visited))))
    return answer