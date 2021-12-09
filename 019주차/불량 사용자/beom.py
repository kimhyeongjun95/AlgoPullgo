from itertools import permutations
 
 
def match(user, banned_id):
    for i in range(len(user)):
        if len(user[i]) == len(banned_id[i]):
            for j in range(len(user[i])):
                if user[i][j] != banned_id[i][j]:
                    if banned_id[i][j] == '*':
                        continue
                    else:
                        return False
        else:
            return False
    return True
 
 
def solution(user_id, banned_id):
    answer = []
 
    for banned_user in permutations(user_id, len(banned_id)):
        if match(banned_user, banned_id):
            banned_user = set(banned_user)
            if banned_user not in answer:
                answer.append(banned_user)
 
 
    return len(answer)
