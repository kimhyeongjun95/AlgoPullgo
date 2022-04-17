# 프로그래머스 양과 늑대

from collections import defaultdict

def solution(info, edges):
    
    def dfs(sheep, wolf, path):
        if info[path[-1]]:
            wolf += 1
        else:
            sheep += 1
        
        if sheep <= wolf:
            return 0
        
        result = sheep
        
        for p in path:
            for n in field[p]:
                if n not in path:
                    result = max(result, dfs(sheep, wolf, path+[n]))
        
        return result
    
    
    field = defaultdict(list)
    for edge in edges:
        field[edge[0]].append(edge[1])
    
    return dfs(0, 0, [0])