from collections import defaultdict
def solution(gems):
    answer = []
    l = len(gems)
    unique_l = len(set(gems))

    if unique_l == 1:
        return [1, 1]

    start, end = 0, 0
    flag = True
    dict = defaultdict(int)
    dict[gems[start]] += 1
    while end < l-1:
        end += 1
        dict[gems[end]] += 1
        while dict[gems[start]] > 1:
            dict[gems[start]] -= 1
            start += 1

        if flag:
            if len(dict.keys()) == unique_l:
                short = end-start+1
                answer = [start+1, end+1]
                flag = False
        else:
            if end - start + 1 < short:
                short = end-start+1
                answer = [start+1, end+1]

    return answer

gems = ["A", "B" ,"B", "C", "A", "B", "C", "A","B","C"]
print(solution(gems))