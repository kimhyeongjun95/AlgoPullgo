# 행렬 테두리 회전하기

def solution(rows, columns, queries):
    matrix = [[row * columns + col +
               1 for col in range(columns)] for row in range(rows)]
    answer = []

    for t, l, b, r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1
        tmp = matrix[top][left]
        minimum = tmp

        for y in range(top, bottom):
            value = matrix[y+1][left]
            matrix[y][left] = value
            minimum = min(minimum, value)

        for x in range(left, right):
            value = matrix[bottom][x+1]
            matrix[bottom][x] = value
            minimum = min(minimum, value)

        for y in range(bottom, top, -1):
            value = matrix[y-1][right]
            matrix[y][right] = value
            minimum = min(minimum, value)

        for x in range(right, left, -1):
            value = matrix[top][x-1]
            matrix[top][x] = value
            minimum = min(minimum, value)

        matrix[top][left+1] = tmp
        answer.append(minimum)

    return answer
