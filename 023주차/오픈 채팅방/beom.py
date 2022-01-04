def solution(record):
    answer = []
    user = dict()
    
    for i in record:
        r = i.split()
        if r[0] == 'Enter' or r[0] == 'Change':
            user[r[1]] = r[2]

    for i in record:
        r = i.split()
        if r[0] == 'Enter':
            answer.append(user[r[1]]+'님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(user[r[1]]+'님이 나갔습니다.')
            
    return answer