def solution(table, languages, preference):
    totals = []
    for job_score in table:
        job_score = job_score.split()
        total = 0
        for lang, pref in zip(languages,preference):
            for j in range(1, 6):
                if lang == job_score[j]:
                    total += pref*(6-j)
                    break
        totals.append((job_score[0],total))
    totals.sort(key = lambda x :(-x[1], x[0]))
    return totals[0][0]