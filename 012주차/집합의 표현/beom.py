import sys
input = sys.stdin.readline


def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):

    root_x = find_set(x)
    root_y = find_set(y)

    # root_x의 트리의 높이(rank)가 더 클 경우
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    # root_y의 트리의 높이가 더 크거나, 혹은 둘이 같을 경우
    else:
        parents[root_x] = root_y
        # 만약에 높이가 같다면 rank 증가
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
ranks = [0] * (N + 1)

for _ in range(M):
    cal, a, b = map(int, input().split())
    if cal == 1:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
