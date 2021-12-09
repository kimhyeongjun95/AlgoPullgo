from itertools import permutations


def check(users, banneds):

    for i in range(len(users)):
        if not len(users[i]) == len(banneds[i]):
            return False

        for j in range(len(users[i])):
            if not banneds[i][j] == '*' and not users[i][j] == banneds[i][j]:
                return False

    return True


def solution(user_id, banned_id):
    answer = []

    users = list(permutations(user_id, len(banned_id)))

    for user in users:
        if check(user, banned_id):
            user = list(user)
            user.sort()
            if user not in answer:
                answer.append(user)
    print(answer)

    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
         ["fr*d*", "*rodo", "******", "******"])
