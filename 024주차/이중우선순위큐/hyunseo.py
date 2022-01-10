# 프로그래머스 이중우선순위큐

import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for operation in operations:
        oper = operation.split()
        
        if oper[0] == 'I':
            heapq.heappush(max_heap, -int(oper[1]))
            heapq.heappush(min_heap, int(oper[1]))
        elif max_heap and oper[1] == '1':
            heapq.heappop(max_heap)
            if not max_heap or -max_heap[0] < min_heap[0]:
                max_heap = []
                min_heap = []
        elif min_heap:
            heapq.heappop(min_heap)
            if not min_heap or -max_heap[0] < min_heap[0]:
                max_heap = []
                min_heap = []
            
    answer = [0, 0]
    if max_heap:
        answer = [-max_heap[0], min_heap[0]]
        
    return answer