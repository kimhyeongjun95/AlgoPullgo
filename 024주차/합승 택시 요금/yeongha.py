from collections import defaultdict, deque

def taxi(n, s, e, graph):
    deq = deque([(s, 0)])
    dist = [float('inf') for _ in range(n+1)]
    dist[s] = 0

    while deq:
        x, d = deq.popleft()

        if d > dist[x]:
            continue

        for nx, nd in graph[x]:
            if dist[nx] > dist[x] + nd:
                dist[nx] = dist[x] + nd
                deq.append((nx, dist[nx]))

    return dist[e]


def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    total = float('inf')

    for fare in fares:
        n1, n2, d = fare
        graph[n1].append((n2, d))
        graph[n2].append((n1, d))

    for i in range(1, n+1):
        share_fee = taxi(n, s, i, graph)
        a_fee = taxi(n, i, a, graph)
        b_fee = taxi(n, i, b, graph)
        total = min(total, share_fee + a_fee + b_fee)

    return total


n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n, s, a, b, fares))