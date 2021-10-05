
def cal_can(number, loc):
    can = 0
    if number == 0:
        number = 11
    if loc == 0:
        loc = 11
    if number > loc:
        if number - loc >= 3:
            can += (number - loc) // 3
            can += (number - loc) % 3
        else:
            can = number - loc
    elif loc > number:
        if loc - number >= 3:
            can += (loc - number) // 3
            can += (loc - number) % 3
        else:
            can = loc - number
    elif number == loc:
        return can
    return can


def solution(numbers, hand):
    answer = ''
    lhl, rhl = 10, 12

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            lhl = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            rhl = number
        else:
            if cal_can(number, lhl) == cal_can(number, rhl):
                answer += hand[0].upper()
                if hand == 'left':
                    lhl = number
                else:
                    rhl = number
            elif cal_can(number, lhl) > cal_can(number, rhl):
                answer += 'R'
                rhl = number
            else:
                answer += 'L'
                lhl = number

    return answer
