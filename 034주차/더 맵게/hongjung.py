import heapq

def solution(scoville, K):
    answer = 0
    error = False
    heapq.heapify(scoville)
    while scoville:
        try:
            num1 = heapq.heappop(scoville)
            num2 = heapq.heappop(scoville)
            num3 = num1 + num2 * 2
            answer += 1
            heapq.heappush(scoville, num3)
            if scoville[0] >= K:
                break
        except:
            error = True
            break
    
    if error:
        return -1
    else:
        return answer

print(solution([1, 2, 3, 9, 10, 12], 7))