def solution(s):
    s_list = []
    tmp_list = []
    tmp_num = ''
    for i in s[1:len(s)-1]:
        if i.isdigit():
            tmp_num += i
        elif i == ',':
            if tmp_num:
                tmp_list.append(int(tmp_num))
                tmp_num = ''
        elif i == '}':
            if tmp_num:
                tmp_list.append(int(tmp_num))
                tmp_num = ''
            s_list.append(tmp_list)
            tmp_list = []
    
    for i in range(len(s_list)):
        for j in range(len(s_list) - 1, i - 1, -1):
            if len(s_list[j]) < len(s_list[j-1]):
                s_list[j], s_list[j-1] = s_list[j-1], s_list[j]
    
    answer = []
    for i in range(len(s_list)):
        for j in s_list[i]:
            if j not in answer:
                answer.append(j)

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
