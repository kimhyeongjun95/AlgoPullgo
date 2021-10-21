import sys
input = sys.stdin.readline

# def find_MST(s):
#     key[s] = 0

#     for _ in range(V):
#         min_idx = -1
#         min_val = float('inf')
#         for i in range(V+1):
#             if not visited[i] and key[i] < min_val:
#                 min_idx = i
#                 min_val = key[i]

#         # 현재 최소 가중치를 가진 정점 (== min_idx)
#         # 방문 처리
#         visited[min_idx] = 1

#         for i in range(V+1):
#             if adj_mat[min_idx][i] and not visited[i]:
#                 weight = adj_mat[min_idx][i]
#                 if weight < key[i]:
#                     key[i] = weight       
#                     parents[i] = min_idx  


# V, E = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(E)]

# # 인접 행렬
# adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)]
# for n1, n2, w in edges:
#     adj_mat[n1][n2] = w
#     adj_mat[n2][n1] = w

# # 초기화
# key = [float('inf')] * (V + 1)  
# parents = [None] * (V + 1)    
# visited = [0] * (V + 1)         

# s = 1
# find_MST(s)
# print(sum(key[1:]))



def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x

    else:
        parents[root_x] = root_y
        # 만약에 높이가 같다면 rank 증가
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1


def find_MST():
    min_weight = 0

    for edge in edges:
        x, y, w = edge
        if find_set(x) != find_set(y):  
            union(x, y)
            min_weight += w

    return min_weight


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
parents = [i for i in range(V+1)]
ranks = [0] * (V + 1)
edges.sort(key=lambda x: x[2])

print(find_MST())