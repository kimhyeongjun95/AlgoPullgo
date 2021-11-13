from collections import deque, defaultdict
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

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
answer = 99999
n1 = 0
for i in range(len(wires)):
    node = defaultdict(list)
    visited=[]
    for item in wires[:i]+wires[i+1:]:
        n1, n2 = item
        node[n1].append(n2)
        node[n2].append(n1)
    bfs(n1)
    print(visited)
    answer = min(answer,abs(len(visited)-(n-len(visited))))
print(answer)