# 프로그래머스 문자열 압축

def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        temp = ''
        cnt = 1
        for j in range(i, len(s), i):
            if s[j-i:j] == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    temp += str(cnt)
                
                cnt = 1
                temp += s[j-i:j]

        if cnt != 1:
            temp += str(cnt)
        
        cnt = 1
        temp += s[j:j+i]
        
        # print(temp, i)
        answer = min(answer, len(temp))

    return answer

print(solution("abcabcdede"))