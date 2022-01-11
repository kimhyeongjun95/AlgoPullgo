# 테케 3개 틀림
def solution(key, lock):
    def rotate_90_degree(list1):
        n = len(list1)
        result = [[] * n for _ in range(n)]
        for j in range(n):
            for i in range(n-1, -1, -1):
                result[j].append(list1[i][j])
        return result

    def is_True(list1, list2):
        n = len(list1)
        puzzle = [[0] * n * 3 for _ in range(n)]
        for i in list1:
            puzzle.append([0] * n + i + [0] * n)
        puzzle += [[0] * n * 3 for _ in range(n)]
        
        for i in range(1, n * 2 + 1):
            tmp1 = puzzle[i:i+n]
            for j in range(1, n * 2 + 1):
                stamp = []
                for k in range(n):
                    stamp += [tmp1[k][j:j+n]]
                cnt = 0
                for k in range(n):
                    for l in range(n):
                        if stamp[k][l] + list2[k][l] == 1:
                            cnt += 1
                if cnt == n * n:
                    return True                
        return False

    rotate_90 = rotate_90_degree(key)
    rotate_180 = rotate_90_degree(rotate_90)
    rotate_270 = rotate_90_degree(rotate_180)
    for k in [key, rotate_90, rotate_180, rotate_270]:
        if is_True(k, lock):
            return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))