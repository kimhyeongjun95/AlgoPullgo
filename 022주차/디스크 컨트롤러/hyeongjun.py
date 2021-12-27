# 프로그래머스 디스크 컨트롤러

import heapq

def solution(jobs):
    jobs.sort() # 안정렬된 상태로 들어올 수 있음
    count = 0 # 작업이 끝날때까지
    time = jobs[0][0]
    answer = 0
    heap = []
    last = -1

    while count < len(jobs):
        for s, term in jobs:
            if last < s <= time:
                heapq.heappush(heap, (term, s))
        
        if heap:
            last = time
            term, start = heapq.heappop(heap)
            count += 1
            time += term
            answer += (time-start)
        else:
            time += 1
    return answer // len(jobs)
    
print(solution([[0, 3], [1, 9], [2, 6]])) # 9


