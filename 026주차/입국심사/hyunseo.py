# 프로그래머스 입국심사

import heapq

# def solution(n, times):
#     heap = []
#     for t in times:
#         heapq.heappush(heap, (t, t))
    
#     person = 1
#     while person < n:
#         endtime, time = heapq.heappop(heap)
#         heapq.heappush(heap, (endtime+time, time))
#         person += 1
    
#     return heapq.heappop(heap)[0]


def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        
        cnt = 0
        for t in times:
            cnt += mid//t
            
            if cnt >= n:
                break
        
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    
    return left