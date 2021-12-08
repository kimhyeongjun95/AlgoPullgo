def solution(progresses, speeds):
    answer = []
    while progresses:
        tmp = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            while progresses:
                if progresses[0] >= 100:
                    tmp += 1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    break
            if tmp:
                answer.append(tmp)
    
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))