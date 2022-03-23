import math

def solution(str1, str2):
    str1_up = str1.upper()
    str2_up = str2.upper()
    str1_list = []
    for i in range(len(str1_up) - 1):
        str1_list.append(str1_up[i] + str1_up[i+1])
    str2_list = []
    for i in range(len(str2_up) - 1):
        str2_list.append(str2_up[i] + str2_up[i+1])

    result_1_list = []
    for s in str1_list:
        if 65 <= ord(s[0]) <= 90 and 65 <= ord(s[1]) <= 90 and s[0] != ' ' and s[1] != ' ':
            result_1_list.append(s)
    
    result_2_list = []
    for s in str2_list:
        if 65 <= ord(s[0]) <= 90 and 65 <= ord(s[1]) <= 90 and s[0] != ' ' and s[1] != ' ':
            result_2_list.append(s)
    
    all_cnt = len(result_1_list) + len(result_2_list)
    result_2_check = [False] * len(result_2_list)
    for i in range(len(result_1_list)):
        for j in range(len(result_2_list)):
            if result_2_check[j] == False and result_1_list[i] == result_2_list[j]:
                result_2_check[j] = True
                break
    
    double_cnt = 0
    for i in result_2_check:
        if i == True:
            double_cnt += 1

    all_cnt -= double_cnt
    if all_cnt == 0 and double_cnt == 0:
        answer = 1 * 65536
    else:
        answer = math.floor(double_cnt / all_cnt * 65536)
    return answer

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
