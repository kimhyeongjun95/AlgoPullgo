# 프로그래머스 야근 지수

import heapq
def solution(n, works):
    answer = 0
    works = [-i for i in works]
    heapq.heapify(works)
    while n:
        temp = heapq.heappop(works) + 1
        if temp == 1:
            break
        heapq.heappush(works, temp)
        n -= 1
    
    for work in works:
        answer += work ** 2
    
    return answer
    
print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1, 1])) # 0
