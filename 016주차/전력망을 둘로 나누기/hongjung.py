def solution(n, wires):
    answer = 100
    for i in range(len(wires)):
        temp_list = wires[:]
        temp_list.pop(i)

        parent = list(range(n+1))
        rank = [0] * (n + 1)

        def search_root(n):
            if parent[n] == n:
                return n
            return search_root(parent[n])

        for pair in temp_list:
            a = search_root(pair[0])
            b = search_root(pair[1])
            if a != b:
                if rank[a] >= rank[b]:
                    parent[b] = a
                    rank[a] += 1
                else:
                    parent[a] = b
                    rank[b] += 1
        
        root_list = []
        for j in range(1, n+1):
            root_list.append(search_root(j))
        
        roots = list(set(root_list))
        if len(roots) == 2:
            if abs(root_list.count(roots[0]) - root_list.count(roots[1])) < answer:
                answer = abs(root_list.count(roots[0]) - root_list.count(roots[1]))
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))