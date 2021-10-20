# 백준 1717 집합의 표현

# n+1개의 집합
# 합집합 연산, 두 원소가 같은 집합에 포함되어 있는가?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def finder(parent, x):

    # if parent[x] != x:
    #     return finder(parent, parent[x])
    # return

    # 위에보다 빠름
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지
    if parent[x] != x:
        parent[x] = finder(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = finder(parent, a)
    b = finder(parent, b)

    # 집합 내에서 작은 숫자가 루트 노드가 된다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    # 0 : 합집합
    # 1 : 확인 연산
    order, a, b = map(int, input().split())
    
    # 합집합으로 만들어주고
    if order == 0:
        # print(parent, 'before')
        union(parent, a, b)
        # print(parent, 'after')

    # 같은 집합인지 확인(즉, 같은 노드인지 확인)
    elif order == 1:
        if finder(parent, a) == finder(parent, b):
            print('YES')
        else:
            print('NO')