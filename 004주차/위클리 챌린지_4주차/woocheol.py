def solution(table, languages, preference):
    answer = {
        'CONTENTS': 0,
        'GAME': 0,
        'HARDWARE': 0,
        'PORTAL': 0,
        'SI': 0,
    }

    for i in range(5):
        table[i] = list(map(str, table[i].split()))

    for i in range(len(languages)):
        for j in range(5):
            if languages[i] in table[j]:
                answer[table[j][0]
                       ] += (6 - table[j].index(languages[i])) * preference[i]

    max_score = max(answer.values())
    ans = ''
    for key, value in answer.items():
        if value == max_score:
            ans = key
            break

    return ans
