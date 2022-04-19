def solution(info, edges):
    
    def searchNodes(v): 
        box = list() 
        for e in edges:     
        # i는 부모노드, j는 자식노드 
            i, j = e 
            # 부모노드 번호 비교 
            if v == i: 
                box.append(j)
        return box
    
    def dfs(sheep, wolf, current, path):
        if info[current]: 
            wolf += 1 
        else: 
            sheep += 1
        
        if sheep <= wolf: 
            return 0
        
        maxSheep = sheep  
        
        for p in path: 
            for n in searchNodes(p): 
                if n not in path: 
                    path.append(n) 
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path)) 
                    path.pop() 
        return maxSheep 
    answer = dfs(0, 0, 0, [0])

 



    return answer