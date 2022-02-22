dxy = [(1,0), (0,1), (-1,-1)]
def solution(n):
    answer = []
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    i = 1
    temp = n
    m = temp
    while i < n*(n+1)//2+1:
        if not m:
            temp -= 1
            m = temp

        x, y = x + dxy[(n-temp)%3][0], y + dxy[(n-temp)%3][1]
        matrix[x][y] = i

        i += 1
        m -=1

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                answer.append(matrix[i][j])
    return answer

print(solution(4))