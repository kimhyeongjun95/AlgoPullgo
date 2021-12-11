def solution(rows, columns, queries):
    def move(q):
        nonlocal puzzle
        start = puzzle[q[0]-1][q[1]-1]
        min_num = start
        for i in range(q[0] - 1, q[2] - 1):
            puzzle[i][q[1]-1] = puzzle[i+1][q[1]-1]
            min_num = min(min_num, puzzle[i][q[1]-1])

        for i in range(q[1] - 1, q[3] - 1):
            puzzle[q[2]-1][i] = puzzle[q[2]-1][i+1]
            min_num = min(min_num, puzzle[q[2]-1][i])

        for i in range(q[2] - 2, q[0] - 2, -1):
            puzzle[i+1][q[3]-1] = puzzle[i][q[3]-1]
            min_num = min(min_num, puzzle[i+1][q[3]-1])
        
        for i in range(q[3] - 2, q[1] - 2, -1):
            puzzle[q[0]-1][i+1] = puzzle[q[0]-1][i]
            min_num = min(min_num, puzzle[q[0]-1][i+1])

        puzzle[q[0]-1][q[1]] = start
        return min_num

    puzzle = [[0] * columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            puzzle [i][j] = n
            n += 1

    answer = []
    for q in queries:
        answer.append(move(q))
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))



def solution2(rows, columns, queries):
    def move(q):
        nonlocal puzzle
        tmp_list_1 = []
        tmp_list_3 = []
        for i in range(q[1] - 1, q[3] - 1):
            tmp_list_1.append(puzzle[q[0]-1][i])
            tmp_list_3.append(puzzle[q[2]-1][i+1])

        tmp_list_2 = []
        tmp_list_4 = []
        for i in range(q[0] - 1, q[2] - 1):
            tmp_list_2.append(puzzle[i][q[3]-1])
            tmp_list_4.append(puzzle[i+1][q[1]-1])
        
        idx = 0
        for i in range(q[1], q[3]):
            puzzle[q[0]-1][i] = tmp_list_1[idx]
            puzzle[q[2]-1][i-1] = tmp_list_3[idx]
            idx += 1

        idx = 0
        for i in range(q[0], q[2]):
            puzzle[i][q[3]-1] = tmp_list_2[idx]
            puzzle[i-1][q[1]-1] = tmp_list_4[idx]
            idx += 1
        
        return min(tmp_list_1 + tmp_list_2 + tmp_list_3 + tmp_list_4)

    puzzle = [list(range(1 + columns * row, rows + 1 +columns * row)) for row in range(rows)]
    answer = []
    for q in queries:
        answer.append(move(q))
    return answer

print(solution2(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution2(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution2(100, 97, [[1,1,100,97]]))