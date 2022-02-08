# 프로그래머스 메뉴 리뉴얼

# 최소 2명 이상의 손님에게서 주문된 구성 코스요리
# 최소 2가지 이상의 단품메뉴 코스요리

# from collections import defaultdict
# from itertools import combinations, permutations
# def solution(orders, course):
#     check = defaultdict(int)

#     for order in orders:
#         for i in range(2, len(order)+1):
#             for j in permutations(order, i):
#                 check[j] += 1
#     result = []
#     for lens in course:
#         max_number = 0
#         for key, val in check.items():
#             if lens == len(key):
#                 max_number = max(max_number, val)
#         for key, val in check.items():
#             if lens == len(key) and val == max_number and val > 1:
#                 result.append(set(key))
#     result.sort()
#     answer = []
#     for i in result:
#         temp = ''
#         i = list(i)
#         i.sort()
#         for j in i:
#             temp += j
#         answer.append(temp)
#     answer = list(set(answer))
#     answer.sort()
#     return answer    

from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combo = combinations(sorted(order), c)
            temp += combo
        flag = Counter(temp)

        if flag:
            max_value = max(flag.values())
            if max_value > 1:
                for key, val in flag.items():
                    if val == max_value:
                        answer.append(''.join(key))
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# # ["AC", "ACDE", "BCFG", "CDE"]
# print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# # ["ACD", "AD", "ADE", "CD", "XYZ"]
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
# ["WX", "XY"]
