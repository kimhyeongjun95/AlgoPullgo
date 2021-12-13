from collections import defaultdict

def solution(s):
    set_dict = defaultdict(int)
    flag = False
    for i in s:
        if i.isdigit():
            if not flag:
                number = i
                flag = True
            else:
                number += i
        else:
            if flag:
                set_dict[int(number)] += 1
                flag = False
                
    number_count = sorted(set_dict.items(), key=lambda x:x[1], reverse=True)
    answer = [num for num, cnt in number_count]
    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))