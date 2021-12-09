from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
    
        cnt = 0
        for i in range(len(progresses)):

            if progresses[i] >= 100:
                continue

            progresses[i] += speeds[i]

        # 앞의 기능이 100 이상이면 끝
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1

            # progresses가 없으면
            if not progresses:
                break

        if cnt > 0:
            answer.append(cnt)

    return answer