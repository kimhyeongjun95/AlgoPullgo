from collections import defaultdict

def solution(record):
    chat = []
    user = defaultdict(str)
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            user[r[1]] = r[2]
            chat.append([r[1], 0])
        elif r[0] == 'Leave':
            chat.append([r[1], 1])
        else:
            user[r[1]] = r[2]

    answer = []
    for c in chat:
        tmp1 = user[c[0]] + "님이 "
        tmp2 = ''
        if c[1] == 0:
            tmp2 = '들어왔습니다.'
        else:
            tmp2 = '나갔습니다.'
        answer.append(tmp1 + tmp2)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))