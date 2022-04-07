# 프로그래머스 스킬트리

# 선행 스킬 순서 : 스파크 -> 라이트닝 볼트 -> 썬더
# 순서에 없으면 아무때나 O

from collections import deque
def solution(skill, skill_trees):

    answer = 0
    for i in skill_trees:
        trees = deque(skill)
        success = True
        for j in i:
            # 선행스킬 O & 순서 O
            if j in trees and j == trees[0]:
                trees.popleft()
            # 선행스킬 O & 순서 X
            elif j in trees and j != trees[0]:
                success = False
                break
            # 선행스킬 X => pass
        if success:
            answer += 1
    return answer

                

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	))

# 2