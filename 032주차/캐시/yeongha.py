from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 0
    cache = deque([0] * cacheSize)
    for city in cities:
        city = city.lower()
        if city not in cache:
            cache.popleft()
            answer += 5
        else:
            cache.remove(city)
            answer += 1
        cache.append(city)
    return answer