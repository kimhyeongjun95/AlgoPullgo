# 프로그래머스 더 맵게

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        answer += 1
        
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))