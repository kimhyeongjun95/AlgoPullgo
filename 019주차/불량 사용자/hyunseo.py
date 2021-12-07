# 프로그래머스 불량 사용자
def is_same(id1, id2):
    for i in range(len(id1)):
        if id1[i] == '*':
            pass
        elif id1[i] != id2[i]:
            return False
    
    return True


def solution(user_id, banned_id):
    able_banned = []
    for b_id in banned_id:
        temp = []
        for u_id in user_id:
            if len(b_id) == len(u_id) and is_same(b_id, u_id):
                temp.append(u_id)
        able_banned.append(temp)
    
    N = len(able_banned)
    answer = []

    def pick_id(n, temp):
        if n == N:
            temp.sort()
            if temp not in answer:
                answer.append(temp)
            return

        for id in able_banned[n]:
            if n == 0:
                pick_id(n+1, [id])
            elif id not in temp:
                pick_id(n+1, temp+[id])
    
    pick_id(0, [])
        
    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))