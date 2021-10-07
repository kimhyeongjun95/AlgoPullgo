import sys
input = sys.stdin.readline
from collections import deque


# def cal_dist(x, y):
#     q = deque()
#     q.append(x)
#     visit = [0] * (N + 1)
#     visit[x] = 1
    
#     while q:



N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, d = map(int, input().split())
    tree[n1].append((n2, d))
    tree[n2].append((n1, d))

for _ in range(M):
    x, y = map(int, input().split())
    print(cal_dist(x, y))