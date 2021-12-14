# 프로그래머스 튜플

# 1. 중복된 원소가 있을 수 있음
# 2. 순서 O, 순서가 다르면 -> 다른 튜플
# 3. 원소 개수는 유한

# 중복되는 원소가 없는 튜플이 주어지면, '집합'을 이용해 표현
# 제일 작은 원소부터 확인해야할듯

# def solution(s):
#     answer = []
#     temp = []
#     result = []
#     s = s[1:-1]
#     # s = s.split(',')
#     print(s)
#     count = []
#     for i in range(len(s)):
#         if s[i] == '{':
#             temp = ''
#         elif s[i] == '}':
#             result.append(list(temp))
#         elif s[i] == ',' and s[i+1].isdigit():
#             result.append(list(temp))
#             temp = ''
#         elif s[i] == ',':
#             continue
#         else:
#             temp += s[i]
#     print(result)
#     result = sorted(result, key=lambda x: len(x))

#     for i in result:
#         for j in i:
#             if j not in answer:
#                 answer.append(j)
#     print(result)
#     return answer

def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key=lambda x: len(x))
    
    for i in s:
        temp = i.split(',')
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # [111, 20]
print(solution("{{123}}")) # [123]
