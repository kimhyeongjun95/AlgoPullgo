def solution(rows, columns, queries):
    answer = []
    matrix = [[(i-1) * columns + j for j in range(1, columns+1)] for i in range(1, rows+1)]
    for q in queries:
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        n = matrix[x1][y1]
        min_num = n
        x, y = x1, y1
        while y < y2:
            y += 1
            n, matrix[x][y] = matrix[x][y], n
            min_num = min(min_num, n)
        while x < x2:
            x += 1
            n, matrix[x][y] = matrix[x][y], n
            min_num = min(min_num, n)
        while y > y1:
            y -= 1
            n, matrix[x][y] = matrix[x][y], n
            min_num = min(min_num, n)
        while x > x1:
            x -= 1
            n, matrix[x][y] = matrix[x][y], n
            min_num = min(min_num, n)
        answer.append(min_num)
    return answer

print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))