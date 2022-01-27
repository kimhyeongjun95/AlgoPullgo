from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    stop = []
    singo = defaultdict(set)
    mail = defaultdict(set)

    for r in report:
        a, b = r.split()
        singo[b].add(a)
        mail[a].add(b)

    for key, value in singo.items():
        if len(value) >= k:
            stop.append(key)

    for id in id_list:
        cnt = 0
        for value in mail[id]:
            if value in stop:
                cnt += 1
        answer.append(cnt)
    return answer
