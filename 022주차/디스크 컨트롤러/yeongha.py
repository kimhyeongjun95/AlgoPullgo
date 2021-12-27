import heapq
def solution(jobs):
    l = len(jobs)
    heapq.heapify(jobs)
    first = heapq.heappop(jobs)
    time = first[0] + first[1]
    answer = first[1]
    while jobs:
        ready = []
        heapq.heapify(ready)
        for i in jobs:
            if time >= i[0]:
                heapq.heappush(ready,i[::-1])
        if ready == [] :
            fast = heapq.heappop(jobs)
            answer+= fast[1]
            time = fast[0]+fast[1]
        else:
            fast = heapq.heappop(ready)[::-1]
            time += fast[1]
            answer += time - fast[0]
            jobs.remove(fast)
                
    return answer // l