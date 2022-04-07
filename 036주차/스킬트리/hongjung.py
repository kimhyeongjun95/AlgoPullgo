from collections import defaultdict

def solution(skill, skill_trees):
    skill_dict = defaultdict(int)
    for i in range(len(skill)):
        skill_dict[skill[i]] = i

    answer = 0
    tmp = []
    for i in skill_trees:
        tmp = []
        for j in i:
            if j in skill:
                tmp.append(j)
        for k in range(len(tmp)):
            if skill_dict[tmp[k]] != k:
                break
        else:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
