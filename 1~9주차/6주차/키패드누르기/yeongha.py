def solution(numbers, hand):
    answer = ''
    last_L, last_R = 10, 12

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            last_L = num
        elif num in [3, 6, 9]:
            answer += 'R'
            last_R = num
        else:
            if num == 0:
                num = 11

            if sum(divmod(abs(num-last_L),3)) < sum(divmod(abs(num-last_R),3)):
                answer += 'L'
                last_L = num
            elif sum(divmod(abs(num-last_L),3)) > sum(divmod(abs(num-last_R),3)):
                answer += 'R'
                last_R = num
            else:
                if hand == 'left':
                    answer += 'L'
                    last_L = num
                else:
                    answer += 'R'
                    last_R = num  
    return answer