def solution(triangle):
    
    depth = len(triangle)
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
    i = 2
    while i < depth:
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        i += 1

    answer = max(triangle[-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))