# 프로그래머스 2020 카카오 인턴십 키패드 누르기

def solution(numbers, hand):
    answer = ''
    
    # 번호 별 위치
    location = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
                4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
                7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
                0 : (3, 1)}

    # 현재 손의 위치
    left = (3, 0)
    right = (3, 2)

    for number in numbers:
        # 왼쪽 줄
        if number in (1, 4, 7):
            answer += 'L'
            left = location[number]
        # 오른쪽 줄
        elif number in (3, 6, 9):
            answer += 'R'
            right = location[number]
        # 가운데 줄
        else:
            # 거리 비교해서 더 짧은 거리 손 이동
            curr = location[number]
            ld = abs(left[0] - curr[0]) + abs(left[1] - curr[1])
            rd = abs(right[0] - curr[0]) + abs(right[1] - curr[1])

            if ld < rd:
                answer += 'L'
                left = curr
            elif rd < ld:
                answer += 'R'
                right = curr
            # 만약 거리가 같다면 왼/오른손잡이 여부에 따라 이동
            else:
                if hand == 'left':
                    answer += 'L'
                    left = curr
                else:
                    answer += 'R'
                    right = curr

    return answer