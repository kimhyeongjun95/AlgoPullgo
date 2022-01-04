def solution(record):
    answer = []
    actions = []
    users = []
    nicknames = {}
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            actions.append(0)
            nicknames[rec[1]] = rec[2]
        elif rec[0] == "Leave" :
            actions.append(1)
        else:
            nicknames[rec[1]] = rec[2]
            continue
        users.append(rec[1])
    
    for user, action in zip(users, actions):
        nickname = nicknames[user]
        if action:
            answer.append(nickname + "님이 나갔습니다.")
        else:
            answer.append(nickname + "님이 들어왔습니다.")
    return answer
    
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))