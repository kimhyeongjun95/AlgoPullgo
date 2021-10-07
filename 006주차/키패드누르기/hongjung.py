def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    L = [3, 0]
    R = [3, 2]

    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == n:
                        L = [i, j]
                        answer += 'L'
        elif n in [3, 6, 9]:
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == n:
                        R = [i, j]
                        answer += 'R'
        else:
            ti = 0
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == n:
                        ti, tj = i, j
            lx, rx = abs(L[0] - ti), abs(R[0] - ti)
            ly, ry = abs(L[1] - tj), abs(R[1] - tj)
            L_distance = lx + ly
            R_distance = rx + ry
            if L_distance == R_distance:
                if hand == 'right':
                    answer += 'R'
                    R = [ti, tj]
                else:
                    answer += 'L'
                    L = [ti, tj]
            elif L_distance > R_distance:
                answer += 'R'
                R = [ti, 1]
            else:
                answer += 'L'
                L = [ti, 1]
            
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))