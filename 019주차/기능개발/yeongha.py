from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses, speeds = deque(progresses),deque(speeds)

    while progresses:
        n = 0
        for i in range(len(progresses)):  
            progresses[i] += speeds[i]
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            n += 1
        
        if n != 0:
            answer.append(n)

    return answer