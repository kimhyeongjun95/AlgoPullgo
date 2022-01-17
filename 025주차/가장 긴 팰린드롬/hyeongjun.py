# 프로그래머스 가장 긴 팰린드롬
# 가장 긴 팰린드롬의 길이를 return

# 제일 큰 길이부터 해서 -= 1 하면서 만약 갱신되면 바로 break

def solution(s):
    answer = 0
    for i in range(len(s)+1, -1, -1):
        for j in range(len(s)-i+1):
            if i % 2 == 1: # 길이가 홀수
                mid = i // 2
                temp = s[j+mid+1:j+mid+1+mid]
                if s[j:j+mid] == temp[::-1]:
                    answer = i
                    return answer

            elif i % 2 == 0: # 길이가 짝수
                mid = i // 2
                temp = s[j+mid:j+mid+mid]
                if s[j:j+mid] == temp[::-1]:
                    answer = i
                    return answer

# print(solution("abcdcba")) # 7
# print(solution("abacde")) # 3
# print(solution("abccba")) # 6
# print(solution("abcdcba")) # 7
# print(solution("afdsgologe")) # 5

# 프로그래머스 모범 답안

# def longest_palindrom(s):
#     for i in range(len(s),0,-1):
#         for j in range(len(s)-i+1):
#             if s[j:j+i] == s[j:j+i][::-1]:
#                 return i