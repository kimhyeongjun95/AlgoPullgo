def solution(routes):
    answer = 1
    routes_sorted = sorted(routes, key = lambda x : x[1])
    end = routes_sorted[0][1]
    for i in range(1, len(routes)):
        if routes_sorted[i][0] > end:
            answer += 1
            end = routes_sorted[i][1]
    return answer

print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[15, 25], [-14, -5], [-18, -13], [-5, -3], [-18, -14]]))