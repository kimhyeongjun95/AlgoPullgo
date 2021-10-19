import sys

def mst():
    global key, visited

    key[1] = 0
    for _ in range(V):
        min_idx = -1
        min_val = float('inf')
        for i in range(1, V+1):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]
        visited[min_idx] = True
        for i in adj_list[min_idx]:
            if not visited[i[0]] and i[1] < key[i[0]]:
                key[i[0]] = i[1]


V, E = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    adj_list[s].append([e, w])
    adj_list[e].append([s, w])

key = [float('inf') for _ in range(V+1)]
visited = [False for _ in range(V+1)]
mst()

print(sum(key[1:]))