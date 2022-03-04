# 프로그래머스 [1차] 캐시

from collections import deque
def solution(cacheSize, cities):

    answer = 0
    cache = deque([])

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city.lower())
            answer += 5                
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# 21