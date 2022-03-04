# 프로그래머스 캐시

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque()
    answer = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        elif len(cache) < cacheSize:
            cache.append(city)
            answer += 5
        else:
            cache.popleft()
            cache.append(city)
            answer += 5
            
    return answer