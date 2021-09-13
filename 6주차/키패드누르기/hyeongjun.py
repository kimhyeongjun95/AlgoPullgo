# 맨 처음 왼쪽 * 오른쪽 # 시작
# 대각선은 갈수 없음, 상하좌우만 가능


distance = {
    '1':{'2': 1, '5': 2, '8': 3, '0': 4},
    '2':{'2': 0, '5': 1, '8': 2, '0': 3},
    '3':{'2': 1, '5': 2, '8': 3, '0': 4},
    '4':{'2': 2, '5': 1, '8': 2, '0': 3},
    '5':{'2': 1, '5': 0, '8': 1, '0': 2},
    '6':{'2': 2, '5': 1, '8': 2, '0': 3},
    '7':{'2': 3, '5': 2, '8': 1, '0': 2},
    '8':{'2': 2, '5': 1, '8': 0, '0': 1},
    '9':{'2': 3, '5': 2, '8': 1, '0': 2},
    '0':{'2': 3, '5': 2, '8': 1, '0': 0},
    '*':{'2': 4, '5': 3, '8': 2, '0': 1},
    '#':{'2': 4, '5': 3, '8': 2, '0': 1},
}
def solution(numbers, hand):

    answer = '' # 정답
    lh = '*' # 초기값
    rh = '#'

    for i in numbers:
        if i in [1, 4, 7, '*']:
            answer += 'L'
            lh = str(i)
        
        elif i in [3, 6, 9, '#']:
            answer += 'R'
            rh = str(i)

        else: # 만약 가운데 열이 나온다면..
            distance_l = distance[lh][str(i)]
            distance_r = distance[rh][str(i)]

            if distance_l < distance_r: # 왼쪽이 짧다면
                lh = str(i)
                answer += 'L'
            
            elif distance_l > distance_r: # 오른쪽이 짧다면
                rh = str(i)
                answer += 'R'
            
            else: # 거리가 같다면
                if hand == 'left':
                    lh = str(i)
                    answer += 'L'
                else:
                    rh = str(i)
                    answer += 'R'
    
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
# print(distance[1][5]) # dict key값을 정수로 받아도 된다.
