def solution(user_id, banned_id):
    def find(bad_id):
        stack = list(filter(lambda x: len(x) == len(bad_id), user_id))
        n = 0
        while n < len(bad_id):
            if bad_id[n] == '*':
                n += 1
                continue
            c = len(stack)
            for _ in range(c):
                id = stack.pop(0)
                if id[n] == bad_id[n]:
                    stack.append(id)
            n += 1
        return stack
    
    def make(lst, n):
        nonlocal result

        if n == len(banned_id):
            result.append(''.join(sorted(lst)))
            return
        
        for id in find_list[n]:
            if not id in lst:
                make(lst+[id], n+1)
                
    find_list = []
    for bad_id in banned_id:
        find_list.append(find(bad_id))

    result = []
    make([], 0)
    return len(set(result))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id, banned_id)