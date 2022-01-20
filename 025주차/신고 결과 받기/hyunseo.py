# 프로그래머스 신고 결과 받기

from collections import defaultdict

def solution(id_list, report, k):
    report_dict = defaultdict(set)
    
    for r in report:
        p1, p2 = r.split()
        report_dict[p2].add(p1)
    
    mail = defaultdict(int)
    for user_id in id_list:
        if len(report_dict[user_id]) >= k:
            for p in report_dict[user_id]:
                mail[p] += 1
    
    answer = []
    for user_id in id_list:
        answer.append(mail[user_id])
        
    return answer