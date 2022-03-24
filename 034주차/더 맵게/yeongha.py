import heapq as h

def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    while len(scoville)>1:
        hot = h.heappop(scoville)+h.heappop(scoville)*2
        h.heappush(scoville,hot)
        answer += 1
        if scoville[0] > K :
            return answer 
    return -1