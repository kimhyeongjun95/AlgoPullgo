from collections import defaultdict

def solution(id_list, report, k):
    id_dict = defaultdict(list)
    id_cnt = defaultdict(int)
    for id in id_list:
        id_dict[id]
        id_cnt[id]

    for r in report:
        r = r.split()
        if r[1] not in id_dict[r[0]]:
            id_dict[r[0]].append(r[1])
            id_cnt[r[1]] += 1

    answer = [0] * len(id_list)
    for i in range(len(id_list)):
        for j in id_dict[id_list[i]]:
            if id_cnt[j] >= k:
                answer[i] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))