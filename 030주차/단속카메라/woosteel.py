# 프로그래머스 단속카메라(Level 3)
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for enter, exit in routes:
        if camera < enter:
            answer += 1
            camera = exit

    return answer
