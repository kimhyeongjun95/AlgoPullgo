word = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
def solution(s):
    answer = ''
    flag = True
    for i in s:
        if not i.isdigit():
            if flag:
                number = i
                flag = False
            else:
                number += i
                if len(number) > 2 and number in word:
                    answer += word[number]
                    number = ''
                    flag = True
        else:
            answer += i

    return int(answer)

s = "2three45sixseven"
print(solution(s))