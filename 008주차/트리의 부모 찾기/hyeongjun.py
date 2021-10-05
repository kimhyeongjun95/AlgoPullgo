# 백준 11725 트리의 부모 찾기

# 트리의 루트를 1이라고 정했을때
# 각 노드의 부모를 출력

# import sys
# input = sys.stdin.readline

# n = int(input())
# tree = [[0] * 3 for _ in range(n+1)]
# for i in range(n-1):
#     one, two = map(int, input().split())

#     # 인덱스 0: 부모 1: 왼자 2: 오자

#     # 1이 들어간 경우
#     # continue : 밑에 if문들이 실행되지 않고 다음 입력을 받기위해.
#     if one == 1:
#         tree[two][0] = 1 # 부모 설정
#         continue
#     elif two == 1:
#         tree[one][0] = 1
#         continue

#     # 
#     if tree[one][0] > 0: # 이미 one이 부모를 가지고 있다면
#         if tree[one][1] == 0: # 왼쪽 자식
#             tree[one][1] = two
#         else:
#             tree[one][2] = two # 오른쪽 자식
        
#         tree[two][0] = one # 부모 설정

#     elif tree[two][0] > 0: # 이미 two가 부모를 가지고 있다면
#         if tree[two][1] == 0: # 왼쪽 자식
#             tree[two][1] = one
#         else: # 오른쪽 자식
#             tree[two][1] = one
#         tree[one][0] = two # 부모 설정

# print(tree)
# for i in range(2, len(tree)):
#     print(tree[i][0])

#DFS BFS로 안풀어서 틀린건가?
import sys
input = sys.stdin.readline
from collections import deque

def dfs():
    queue = deque([1])
    # cnt = 1
    while queue:
        popped = queue.popleft()
        for i in tree[popped]: # 1번
            if parent[i] == 0:
                parent[i] = popped # 2번 : 부모노드 설정
                queue.append(i) # 3번
                # print(parent, cnt)
                # print(queue)
                # cnt += 1
        # print(popped)
        # tree : [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
        # 1. popped = 1 (1) 6, 4 (2) 둘다 1 삽입 (3) 6, 4 append ///// [6, 4]
        # 2. popped = 6 (1) 1, 3 (2) 둘다 6 삽입 (3) 1, 3 append ///// [4, 1, 3]
        # 3. popped = 4 (1) 1, 2, 8
        #               (2) 1은 pass 2와 7에 4 삽입
        #               (3) 2, 7 append ///// [1, 3, 2, 7]
        # 4. popped = 1 (1) 6, 4 pass ///// [3, 2, 7]
        # 5. popped = 3 (1) 6, 5 (2) 5에 3삽입 (3) 5 append [2, 7, 5]
        # 6. popped = 2
        # 7. popped = 7
        # 8. popped = 5
        # parent[1] 자리에 6이 들어가지만 사실상 1은 확인 안할거기에..

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)] # 방문 기록 용도

for _ in range(n-1):
    one, two = map(int, input().split())
    tree[one].append(two)
    tree[two].append(one)

dfs()

for i in range(2, len(parent)):
    print(parent[i])
# print(tree)
# print(parent)