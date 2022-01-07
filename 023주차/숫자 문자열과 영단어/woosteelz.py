def solution(s):
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    temp = ''
    ans = ''
    for i in s:
        if temp in num_dict:
            ans += num_dict[temp]
            temp = ''
        if i.isdigit():
            ans += i
        else:
            temp += i
    if temp in num_dict:
        ans += num_dict[temp]

    return int(ans)
