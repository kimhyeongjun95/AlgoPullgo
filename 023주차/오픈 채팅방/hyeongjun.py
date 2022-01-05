# 프로그래머스 오픈채팅방
def solution(record):
    answer = []
    user = {}
    orders = [] # "Enter", "Leave", "Change"
    
    for event in record:
        data = event.split()
        # print(data)
        action, userid = data[0], data[1]
        if action in ("Enter", "Change"):
            nickname = data[2]
            user[userid] = nickname
        orders.append((action, userid))
        
    for order in orders:
        key, userid = order[0], order[1]
        if key == 'Enter':
            answer.append(f'{user[userid]}님이 들어왔습니다.')
        elif key == 'Leave':
            answer.append(f'{user[userid]}님이 나갔습니다.')
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])) 
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]