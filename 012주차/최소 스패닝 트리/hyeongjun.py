# 백준 1197 최소 스패닝 트리

# 그래프가 주어졌을때
# 최소 스패닝 트리 구하기
# 최소 스패닝 트리 : 그래프의 모든 정점들을 연결하는 부분 그래프 중
#                    가중치의 합이 최소인 트리

# 최소 스패닝 트리의 가중치 구하기

import sys
input = sys.stdin.readline

def finder(parent, see):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지
    if parent[see] != see:
        parent[see] = finder(parent, parent[see])
    return parent[see]

def union(parent, a, b):
    a = finder(parent, a)
    b = finder(parent, b)

    # 집합 내에서 작은 숫자가 루트 노드가 된다.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v: 정점, e: 간선
v, e = map(int, input().split())

# 부모는 일단 자기 자신
parent = [i for i in range(v+1)] 
trees = []
for _ in range(e):
    # 정점1, 정점2, 가중치
    # 1 2 1
    # 2 3 2
    # 1 3 3
    v1, v2, far = map(int, input().split())
    trees.append((far, v1, v2))

# 1. 크루스칼 알고리즘은 오름차순 정렬을 하고
trees.sort()

answer = 0
# 2. 사이클을 형성하지 않는 선에서 정렬된 순서대로 간선 선택
for tree in trees:
    far, v1, v2 = tree
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if finder(parent, v1) != finder(parent, v2):
        union(parent, v1, v2)

        # 가중치 계산
        answer += far

print(answer)    