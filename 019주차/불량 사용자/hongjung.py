def solution(user_id, banned_id):
    result = []
    for ban in banned_id:
        tmp = []
        star_cnt = ban.count('*')
        length = len(ban)
        for user in user_id:
            if length == len(user):
                cnt = 0
                for i in range(length):
                    if ban[i] == user[i]:
                        cnt += 1
                if cnt + star_cnt == length:
                    tmp.append(user)
        result.append(tmp)

    list_result = [[]]
    def make_list(idx, n, id_list):
        nonlocal result, list_result
        if idx == n:
            id_list.sort()
            if id_list not in list_result:
                list_result += [id_list]
            return

        for id in result[idx]:
            if id not in id_list:
                make_list(idx + 1, n, id_list + [id])
    
    make_list(0, len(result), [])
    answer = len(list_result) - 1
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))