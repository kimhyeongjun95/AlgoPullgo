import heapq

def solution(operations):
    answer = [0,0]
    min_heap = []
    max_heap = []
    cnt = 0

    for o in operations:
        oper = o.split()
        if oper[0] == 'I':
            num = int(oper[-1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            cnt += 1
        else:
            if cnt:
                if '-' in o:
                    num = heapq.heappop(min_heap)
                    max_heap.remove(-num)
                else:
                    num = heapq.heappop(max_heap)
                    min_heap.remove(-num)
                cnt -= 1

    if cnt:
        M = heapq.heappop(max_heap)
        m = heapq.heappop(min_heap)
        answer = [-M, m]

    return answer