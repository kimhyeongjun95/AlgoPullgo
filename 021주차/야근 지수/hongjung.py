import heapq

def solution(n, works):
    heap = []
    for w in works:
        heapq.heappush(heap, (-w, w))
    
    while n > 0:
        tmp = heapq.heappop(heap)[1]
        if tmp == 0:
            break
        tmp -= 1
        n -= 1
        heapq.heappush(heap, (-tmp, tmp))
        if n == 0:
            break
    
    answer = 0
    for h in heap:
        answer += h[1] ** 2
        
    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))


# 효율성 테스트 성공 못함
# def solution(n, works):

#     while n > 0:
#         works[works.index(max(works))] -= 1
#         if sum(works) == 0:
#             break
#         n -= 1
        
#     answer = 0
#     for w in works:
#         answer += w**2
#     return answer