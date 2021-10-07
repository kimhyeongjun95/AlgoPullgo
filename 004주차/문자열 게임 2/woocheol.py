# 20437번 문자열 게임2

def get_string_len(string, num):
    ans = []
    dict_str = {}
    for i in range(len(string)):
        if string[i] in dict_str:
            dict_str[string[i]].append(i)
        else:
            dict_str[string[i]] = [i]
    
    print(dict_str)
    # {'s': [0], 'u': [1, 7], 'p': [2], 'e': [3], 'r': [4, 11], 'a': [5, 8, 13], 'q': [6], 't': [9], 'o': [10, 15], 'n': [12], 'd': [14]}

    for val in dict_str.values():
        if len(val) == num:
            print(val, '!!')
            ans.append(val[-1] - val[0] + 1)
        elif len(val) > num:
            for idx in range(len(val) - num + 1):
                print(val, '###')
                temp = val[idx:idx+num]
                print(temp, '@@@')
                ans.append(temp[-1] - temp[0] + 1)
    print(ans)

    if ans:
        return [min(ans), max(ans)]
    return [-1]


TC = int(input())

for _ in range(TC):
    string = input()
    num = int(input())
    print(*get_string_len(string, num))
