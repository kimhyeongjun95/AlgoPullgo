# 프로그래머스 단속카메라

def solution(routes):
    routes.sort(key = lambda x : x[1])
    
    camera = routes[0][1]
    answer = 1
    
    for s, e in routes:
        if camera < s:
            camera = e
            answer += 1
    
    return answer