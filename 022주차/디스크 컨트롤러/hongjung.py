# 참고
import heapq

def solution(jobs):
    answer, curr, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= curr:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            temp = heapq.heappop(heap)
            start = curr
            curr += temp[0]
            answer += curr - temp[1]
            i += 1
        else:
            curr += 1
                
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))


# def solution(jobs):
#     def min_time(curr, accum):
#         nonlocal visited, answer

#         if sum(visited) == len(jobs):
#             if answer > (accum // len(jobs)):
#                 answer = accum // len(jobs)
#             return
        
#         flag = False
#         for i in range(len(jobs)):
#             if visited[i] == 0 and jobs[i][0] <= curr:
#                 flag = True
#                 visited[i] = 1
#                 min_time(curr + jobs[i][1], accum + curr + jobs[i][1] - jobs[i][0])
#                 visited[i] = 0
        
#         if flag == False:
#             min_time(curr + 1, accum)
                
#     visited = [0] * len(jobs)
#     visited[0] = 1
#     answer = float('inf')
#     min_time(jobs[0][1], jobs[0][1])
#     return answer