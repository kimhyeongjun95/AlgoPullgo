# 프로그래머스 오픈 채팅방

def solution(record):
    users = {}
    command = []
    for rec in record:
        temp = list(rec.split())
        
        if temp[0] != 'Leave':
            users[temp[1]] = temp[2]
        
        if temp[0] != 'Change':
            command.append((temp[0], temp[1]))
        
    answer = []
    for cmd, id in command:
        if cmd == 'Enter':
            answer.append(f'{users[id]}님이 들어왔습니다.')
        else:
            answer.append(f'{users[id]}님이 나갔습니다.')
    
    return answer