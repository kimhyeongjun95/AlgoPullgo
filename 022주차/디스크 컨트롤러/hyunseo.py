# 프로그래머스 디스크 컨트롤러

import heapq

def solution(jobs):
    N = len(jobs)
    heapq.heapify(jobs)
    time = 0
    answer = 0
    ready = []
    
    while jobs or ready:
        while jobs and jobs[0][0] <= time:
            temp = heapq.heappop(jobs)
            heapq.heappush(ready, (temp[1], temp[0]))
        
        if ready:
            use, request = heapq.heappop(ready)
            time += use
            answer += time - request
        else:
            time += 1
    
    return answer//N