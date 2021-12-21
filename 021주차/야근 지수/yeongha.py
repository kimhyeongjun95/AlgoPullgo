import heapq

def solution(n, works):
    heapq.heapify(works)
    answer = 0
    max_heap = []
    for i in works:
        heapq.heappush(max_heap, (-i, i))
    for _ in range(n):
        if max_heap[0][1] == 0:
            break
        i = heapq.heappop(max_heap)[1]-1
        heapq.heappush(max_heap,(-i,i))
    answer = sum([i[1]**2 for i in max_heap])

    return answer