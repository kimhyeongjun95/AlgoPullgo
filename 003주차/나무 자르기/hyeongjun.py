# 절단기에 높이 H 지정 -> 한 줄에 연속해있는 나무를 모두 절단
# H 위의 부분이 잘라질 것이다.

# 20 15 10 17 : 15
# 15 15 10 15 -> 5미터와 2미터를 집에 들고간다. 총 7미터

# 필요한 만큼만 집으로 가져가려고 한다. M만큼의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램


# 나무의 수 N, 나무의 길이 M
# 4 7
# 20 15 10 17
# -> 15

# 만약 몇 이상이면 m을 구하는지?
# 1. 역순 정렬하기
# 2. 비교해서 계속 이상이면.. -= 1
# 3. M == ?

# -----------------------------------------디버깅----------------------------------------
# from collections import deque # deque는 sort가 안된다!
# pop(0)은 시간초과된다
# pop()도 시간초과된다.
# import sys 넣어도 초과된다.
# 2중 for문이 n2니까 2중 for문을 없애면?

# 알고리즘 분류 -> 이분탐색으로 풀면?
# 1. 중간값부터 10 30 이란 나무가 있다면.. 20중간값보다 컸을때 잘린 나무들이 M보다 작거나 같은지? 반복계산

import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
# trees.sort() sort를 할 필요가 없음

# def search(p, m):
#     start = 0
#     end = max(p)

#     while start <= end:
#         middle = (start+end) // 2 
#         target = 0

#         for x in p:
#             if x >= middle:
#                 target += x - middle

#         if target == m:
#             return middle

#         if target >= m:
#             start = middle + 1

#         else:
#             end = middle - 1
#     return end

# print(search(trees, m))
        
trees.sort()

target = 0
p_list = []

popped = trees.pop() # 초기값 설정
p_list.append(popped)

while target < m:

    if p_list[0] == trees[-1]: # p_list에는 같은 크기의 숫자만 append 될것이다.
        popped = trees.pop()
        p_list.append(popped)

    for i in range(len(p_list)):
        p_list[i] -= 1
        target += 1 # p_list의 길이만큼 target이 커짐

# while target < m:

#     if p_list[0] == trees[-1]: # p_list에는 같은 크기의 숫자만 append 될것이다.
#         popped = trees.pop()
#         p_list.append(popped)

#     p_list[0] -= 1 
#     target += 1 * len(p_list)

print(p_list[0])