# 프로그래머스 튜플
def solution(s):
    sets = []
    temp = []
    temp_num = ''
    start = False
    for word in s[1:len(s)-1]:
        if word == '{':
            start = True
        elif start and word.isnumeric():
            temp_num += word
        elif start and word == ',':
            temp.append(int(temp_num))
            temp_num = ''
        elif word == '}':
            start = False
            temp.append(int(temp_num))
            temp_num = ''
            sets.append(temp)
            temp = []
    
    sets.sort(key = lambda x : len(x))
    
    answer = []
    for a_set in sets:
        for a in a_set:
            if a not in answer:
                answer.append(a)
                break
    
    return answer