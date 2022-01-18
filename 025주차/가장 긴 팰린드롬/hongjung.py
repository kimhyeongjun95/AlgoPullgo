from collections import defaultdict

def solution(s):
    alpha_dict = defaultdict(list)
    for i in range(len(s)):
        alpha_dict[s[i]].append(i)
    
    answer = 0
    for k in list(alpha_dict.keys()):
        if len(alpha_dict[k]) > 1:
            for i in range(len(alpha_dict[k]) - 1):
                for j in range(i + 1, len(alpha_dict[k])):
                    if s[alpha_dict[k][i]:alpha_dict[k][j]+1] == s[alpha_dict[k][i]:alpha_dict[k][j]+1][::-1] and alpha_dict[k][j] - alpha_dict[k][i] + 1 > answer:
                        answer = alpha_dict[k][j] - alpha_dict[k][i] + 1
    if answer == 0:
        answer = 1
    return answer

print(solution("abcdcba"))
print(solution("abacde"))
