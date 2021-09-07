def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
        '*': (3,0), 0: (3,1), '#': (3,2),
    }
    left = '*'
    right = '#'

    for i in numbers:
        if i in [1, 4, 7]:
            left = i
            answer += 'L'
        
        elif i in [3, 6, 9]:
            right = i
            answer += 'R'
        
        else:
            pos = keypad[i]
            left_pos = keypad[left]
            right_pos = keypad[right]
            left_d = abs(pos[0]-left_pos[0]) + abs(pos[1]-left_pos[1])
            right_d = abs(pos[0]-right_pos[0]) + abs(pos[1]-right_pos[1])

            if left_d < right_d:
                left = i
                answer += 'L'
            
            elif left_d > right_d:
                right =i
                answer += 'R'
            
            else:
                if hand == 'left':
                    left = i
                    answer += 'L'
                else:
                    right = i
                    answer += 'R'

    return answer

