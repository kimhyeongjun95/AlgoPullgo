# 프로그래머스 불량 사용자
# 경우의 수 몇 개? -> 순열 사용

from itertools import permutations
def check(permut, banned_id):
    # permut의 개수와 banned_id의 개수는 같다.
    for i in range(len(permut)):
        if len(permut[i]) != len(banned_id[i]):
            return False

        for j in range(len(permut[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != permut[i][j]:
                return False

    return True

def solution(user_id, banned_id):
    permuts = list(permutations(user_id, len(banned_id)))
    result = []
    for permut in permuts: # 경우의 수

        if check(permut, banned_id):
            # 중복 제거해줘야됨
            permut = set(permut)
            if permut not in result:
                result.append(permut)
    
    return len(result)


    
                    



    


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # '2'