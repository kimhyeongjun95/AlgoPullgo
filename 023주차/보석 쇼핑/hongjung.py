from collections import defaultdict

def solution(gems):
    length = len(set(gems))
    start, end = 0, 0
    answer = [start, end]
    gems_dict = defaultdict(int)
    
    while end <= len(gems):
        if len(gems_dict) == length:
            if sum(answer) == 0:
                answer = [start, end]
            else:
                if answer[1] - answer[0] > end - start:
                    answer = [start, end]
                elif answer[1] - answer[0] == end - start and answer[0] > start:
                    answer = [start, end]
            if gems_dict[gems[start]] == 1:
                del gems_dict[gems[start]]
            else:
                gems_dict[gems[start]] -= 1
            start += 1
        else:
            if end == len(gems):
                break
            if gems[end] in gems_dict.keys():
                gems_dict[gems[end]] += 1
            else:
                gems_dict[gems[end]] = 1
            end += 1

    answer[0] += 1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))


# def solution(gems):
#     gems_list = list(set(gems))
#     length = len(gems_list)
#     answer = []
#     for i in range(len(gems) - length + 1):
#         tmp = 0
#         tmp_list = []
#         for j in range(i, len(gems)):
#             if answer:
#                 if answer[1] - answer[0] < j - i:
#                     break
#                 elif answer[1] - answer[0] == j - i and answer[0] < i:
#                     break

#             if gems[j] not in tmp_list:
#                 tmp_list.append(gems[j])
#                 tmp += 1
#                 if tmp == length:
#                     if answer:
#                         if answer[1] - answer[0] > j - i:
#                             answer = [i, j]
#                         elif answer[1] - answer[0] == j - i and answer[0] > i:
#                             answer = [i, j]
#                     else:
#                         answer = [i, j]
#                     break
#         else:
#             break
    
#     answer[0] += 1
#     answer[1] += 1
#     return answer


# from collections import defaultdict

# def solution(gems):
#     start, end = 0, 0
#     answer = [start, end]

#     gems_dict = defaultdict(int)
#     for g in list(set(gems)):
#         gems_dict[g] = 0

#     while end <= len(gems):
#         if list(gems_dict.values()).count(0) < 1:
#             if sum(answer) == 0:
#                 answer = [start, end]
#             else:
#                 if answer[1] - answer[0] > end - start:
#                     answer = [start, end]
#                 elif answer[1] - answer[0] < end - start:
#                     gems_dict[gems[start]] -= 1
#                     start += 1
#                     continue
#                 elif answer[1] - answer[0] == end - start and answer[0] > start:
#                     answer = [start, end]
#             gems_dict[gems[start]] -= 1
#             start += 1
#         else:
#             if end == len(gems):
#                 break
#             gems_dict[gems[end]] += 1
#             end += 1

#     answer[0] += 1
#     return answer