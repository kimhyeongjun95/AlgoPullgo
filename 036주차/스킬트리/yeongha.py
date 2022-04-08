def solution(skill, skill_trees):
    answer = 0
    skill_dict = {}
    for i in range(len(skill)):
        skill_dict[skill[i]] = i
    
    for tree in skill_trees:
        temp = -1
        for i in tree:
            if i in skill_dict:
                n = skill_dict[i]
                if temp > n or n - temp > 1:
                    break
                else:
                    temp = n
        else:
            answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))