def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    tmp = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            tmp += i
            if tmp in num_list:
                answer += str(num_list.index(tmp))
                tmp = ''
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))