def solution(rows, columns, queries):
    answer = []
    num = 1
    matrix = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1
            
    for i in queries:
        r1, c1, r2, c2 = i[0], i[1], i[2], i[3]

        # 맨 윗줄
        tmp = matrix[r1 - 1][c2 - 1]
        min_num = tmp
        for i in range(c2 - 1, c1 - 1, -1):
            matrix[r1 - 1][i] = matrix[r1 - 1][i - 1]
            min_num = min(min_num, matrix[r1 - 1][i - 1])

        # 맨 오른족    
        tmp2 = matrix[r2 - 1][c2 - 1]
        min_num = min(min_num, tmp2)
        for i in range(r2 - 1, r1, -1):
            matrix[i][c2 - 1] = matrix[i - 1][c2 - 1]
            min_num = min(min_num, matrix[i - 1][c2 - 1])
        matrix[r1][c2 - 1] = tmp

        # 아랫줄
        tmp = matrix[r2 - 1][c1 - 1]
        min_num = min(min_num, tmp)
        for i in range(c1, c2 - 1):
            matrix[r2 - 1][i - 1] = matrix[r2 - 1][i]
            min_num = min(min_num, matrix[r2 - 1][i])
        matrix[r2 - 1][c2 - 2] = tmp2
        
        # 왼쪽
        for i in range(r1 - 1, r2 - 2):
            matrix[i][c1 - 1] = matrix[i + 1][c1 - 1]
            min_num = min(min_num, matrix[i + 1][c1 - 1])
        matrix[r2 - 2][c1 - 1] = tmp
        
        answer.append(min_num)
    return answer