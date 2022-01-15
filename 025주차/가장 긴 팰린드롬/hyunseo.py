# 프로그래머스 가장 긴 팰린드롬

# def solution(s):
#     answer = 1
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if s[j] == s[i]:
#                 start = i
#                 end = j
                
#                 flag = True
#                 while start <= end:
#                     if s[start] != s[end]:
#                         flag = False
#                         break
                    
#                     start += 1
#                     end -= 1
                
#                 if flag:
#                     answer = max(answer, j-i+1)

#     return answer


def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                answer = max(answer, j-i+1)

    return answer