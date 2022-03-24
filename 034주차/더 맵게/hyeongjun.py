# 프로그래머스 더 맵게

# 모든 음식의 스코빌 지수를 K 이상
# 지수가 가장 낮은 두 개의 음식 => 섞어서 새로운 음식

# mix = min 스코빌 + (2nd min 스코빌 * 2)

# 모든 음식의 스코빌 지수가 K 이상 될때까지 반복
# 섞어야 하는 최소 횟수 return

import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    count = 0

    while True:
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        temp = first + (second * 2)

        heapq.heappush(scoville, temp)
        count += 1

        for i in scoville:
            if i < K:
                break
        else:
            return count

        if len(scoville) == 1:
            return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
# 2