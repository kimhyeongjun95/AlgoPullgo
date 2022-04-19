# 백준 3584 가장 가까운 공통 조상

# 루트 트리
# 두 정점이 주어질 때, 
# 가장 가까운 공통 조상 : 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(가까운) 노드

# ex) 15, 11 => 4와 8중 4

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    trees = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        trees[b].append(a)
    # 16, 7
    one, two = map(int, input().split())
    one_tree = [one]
    two_tree = [two]
    while trees[one]:
        one_tree.append(trees[one][0])
        one = trees[one][0]
    while trees[two]:
        two_tree.append(trees[two][0])
        two = trees[two][0]

    flag = False
    for i in one_tree:
        if flag:
            break
        for j in two_tree:
            if i == j:
                print(i)
                flag = True
                break
