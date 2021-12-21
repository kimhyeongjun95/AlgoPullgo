def solution(k, dungeons):
    def move_dg(rest, cnt):
        nonlocal length, answer, visited
        
        flag = False
        for i in range(length):
            if visited[i] == 0 and rest >= dungeons[i][0]:
                flag = True
                visited[i] = 1
                move_dg(rest - dungeons[i][1], cnt + 1)
                visited[i] = 0

        if flag == False:
            if cnt > answer:
                answer = cnt
            return

    length = len(dungeons)
    visited = [0] * length
    answer = -1
    move_dg(k, 0)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))