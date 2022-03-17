# 프로그래머스 순위 검색

# 언어: cpp, java, python
# 지원 직군 : backend, frontend
# 지원 경력구분 : junior, senior
# 소울푸드 : chicken, pizza

# 지원 조건 선택: 해당 조건에 맞는 지원자는 몇명인가?
# => [조건] 만족 -> 코딩테스트 점수 X점 이상?

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    
    check = defaultdict(list)

    for i in info:
        i = i.split()
        detail = i[:-1]
        value = int(i[-1])
        
        for i in range(5): # 0, 1, 2, 3, 4
            for combo in combinations([0, 1, 2, 3], i):
                temp = detail.copy()
                # 경우의 수 입력
                for idx in combo:
                    temp[idx] = '-'
                # list를 append 불가능
                key = ''.join(temp)
                check[key].append(value)

    for val in check.values():
        val.sort()

    answer = []
    for q in query:
        # info처럼 만듬
        q = q.replace("and ", '')
        q = q.split()
        # 위에 key와 같은 detail
        detail = ''.join(q[:-1])
        value = int(q[-1])
        count = 0
        if check[detail]:
            temp = check[detail]
            idx = bisect_left(temp, value)
            count = len(temp) - idx
        answer.append(count)
    return answer

print(solution(
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))
# [1,1,1,1,2,4]
