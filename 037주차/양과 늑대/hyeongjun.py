# 프로그래머스 양과 늑대

# 만약 늑대의 수 >= 양의 수:
# 모든 양을 잡아먹어버림

# 양이 최대한 늑대에게 안 잡하먹히도록 하면서 돌아오기

# info 0 : 양, 1 : 늑대
# edges [부모, 자식]

from collections import defaultdict, deque


def dfs(queue, sheep, wolf):
    global answer
    answer = max(sheep, answer)
    
    for _ in range(len(queue)):
        popped = queue.popleft()
        # 양
        if infos[popped] == 0:
            for j in trees[popped]:
                queue.append(j)
            dfs(queue, sheep + 1, wolf)
            for j in trees[popped]:
                queue.pop()
        # 늑대
        elif infos[popped] == 1:
            # 양의 수가 늑대 + 1보다 더 많음
            if sheep > wolf + 1:
                for j in trees[popped]:
                    queue.append(j)
                dfs(queue, sheep, wolf + 1)
                for j in trees[popped]:
                    queue.pop()
            
        queue.append(popped)


def solution(info, edges):
    global answer, infos, trees
    answer = 0
    infos = info
    trees = defaultdict(list)
    for one, two in edges:
        trees[one].append(two)
    queue = deque([0])
    dfs(queue, 0, 0)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# 5