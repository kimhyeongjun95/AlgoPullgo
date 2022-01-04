# 프로그래머스 보석 쇼핑

def solution(gems):
    n = len(gems)
    n_set = len(set(gems))
    
    include = {}
    for gem in set(gems):
        include[gem] = 0
    
    start = 0
    end = n_set - 1
    kind = 0
    for i in range(start, end+1):
        if include[gems[i]] == 0:
            kind += 1
        include[gems[i]] += 1
    
    able = []
    
    while True:
        if kind == n_set:
            able.append([start, end])
            if include[gems[start]] == 1:
                kind -= 1
            include[gems[start]] -= 1
            
            start += 1
            if start > n - n_set:
                break
        else:
            end += 1
            if end == n:
                break
                
            if include[gems[end]] == 0:
                kind += 1
            include[gems[end]] += 1
    
    able.sort(key=lambda x: x[1]-x[0])
    return [able[0][0]+1, able[0][1]+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))