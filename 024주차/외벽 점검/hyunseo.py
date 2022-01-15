# 프로그래머스 외벽 점검

from itertools import permutations
from collections import deque

def solution(n, weak, dist):
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i]+n)
    
    answer = float('inf')
    for j in range(weak_len):
        for people in permutations(dist, len(dist)):
            queue = deque(weak[j:j+weak_len])
            people = deque(people)
            
            while queue and people:
                able = queue[0] + people[0]
                while queue and queue[0] <= able:
                    queue.popleft()
                    
                people.popleft()
                
                if not queue:
                    answer = min(answer, len(dist)-len(people))
    
    if answer == float('inf'):
        answer = -1

    return answer

print(solution(200, [0, 100], [1, 1]))