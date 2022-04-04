# 프로그래머스 정수 삼각형

def solution(triangle):
    temp = triangle.copy()
    for i in range(1, len(temp)):
        for j in range(len(temp[i])):
            # 왼쪽
            if j == 0:
                temp[i][j] += temp[i-1][j]
            # 오른쪽
            elif j == len(temp[i]) - 1:
                temp[i][j] += temp[i-1][j-1]
            # 중앙은 위 왼쪽 오른쪽 중 큰 값 더하기
            else:
                temp[i][j] += max(temp[i-1][j-1], temp[i-1][j])

    answer = max(temp[-1])        
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
# 30

#     [7]
#    [3, 8]
#   [8, 1, 0]
#  [2, 7, 4, 4]
# [4, 5, 2, 6, 5]

# [7]
# [3, 8]
# [8, 1, 0]
# [2, 7, 4, 4]
# [4, 5, 2, 6, 5]