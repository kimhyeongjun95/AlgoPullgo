# 프로그래머스 기능개발

import math
from collections import deque
def solution(progresses, speeds):
    # [7, 3, 9]가 나와야 한다.
    result = deque([])
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i]) # 소수점 올림
        result.append(day)

    answer = []
    while result:
        popped = result.popleft()
        count = 1
        while result and popped >= result[0]: # 뒤에 숫자 '이상'이면서 빈리스트가 아닐때
            result.popleft()
            count += 1
        answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]