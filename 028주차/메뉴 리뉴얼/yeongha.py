from itertools import combinations

def solution(orders, course):
    answer = []
    lst = []
    for i in course:
        dict = {}
        for j in range(len(orders)-1):
            for k in combinations(orders[j], i):
                k = ''.join(sorted(k))
                if k not in dict:
                    dict[k] = 1
                    for l in range(j+1, len(orders)):
                        if set(list(k)).issubset(set(list(orders[l]))):
                            dict[k] += 1
        lst.append(dict)

    for i in range(len(lst)):
        if lst[i]:
            max_cnt = max(lst[i].values())
            if max_cnt > 1:
                for key, value in lst[i].items():
                    if value == max_cnt:
                        answer.append(key)
    answer.sort()
    return answer