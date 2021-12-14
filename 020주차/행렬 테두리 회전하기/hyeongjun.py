# 프로그래머스 행렬 테두리 회전하기

def solution(rows, columns, queries):
    arr = []
    count = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(count)
            count += 1
        arr.append(temp)
    
    answer = []
    for x1, y1, x2, y2 in queries:
        temp = arr[x1-1][y1-1]
        min_number = temp

        for i in range(x1-1,x2-1):
            swipe = arr[i+1][y1-1]
            arr[i][y1-1] = swipe
            min_number = min(min_number, swipe)

        for i in range(y1-1,y2-1):
            swipe = arr[x2-1][i+1]
            arr[x2-1][i] = swipe
            min_number = min(min_number, swipe)

        for i in range(x2-1,x1-1,-1):
            swipe = arr[i-1][y2-1]
            arr[i][y2-1] = swipe
            min_number = min(min_number, swipe)

        for i in range(y2-1,y1-1,-1):
            swipe = arr[x1-1][i-1]
            arr[x1-1][i] = swipe
            min_number = min(min_number, swipe)

        arr[x1-1][y1] = temp
        answer.append(min_number)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]])) # [1]