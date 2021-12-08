# 프로그래머스 기능개발

from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    while progresses:
        n = len(progresses)
        # 작업
        for _ in range(n):
            progresses.append(progresses.popleft() + speeds[0])
            speeds.append(speeds.popleft())
        
        # 배포
        cnt = 0
        for i in range(n):
            if progresses[i] >= 100:
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
        
        for _ in range(cnt):
            progresses.popleft()
            speeds.popleft()
        
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))