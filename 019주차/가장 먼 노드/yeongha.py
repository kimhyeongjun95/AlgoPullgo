from collections import defaultdict, deque
def solution(n, edge):
    def bfs():
        nonlocal min_dists
        deq = deque([(1,0)])
        
        while deq:
            m, d = deq.popleft()

            for v in graph[m]:
                if min_dists[v-1] == 0:
                    min_dists[v-1] = d+1
                    deq.append([v, d+1])

    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    min_dists = [1] + [0 for _ in range(n-1)]
    bfs()
    answer = min_dists[1:].count(max(min_dists))
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))