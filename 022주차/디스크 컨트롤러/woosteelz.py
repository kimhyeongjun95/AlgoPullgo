def solution(jobs):
    answer = 0
    curr = 0
    total = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= curr:
                curr += jobs[i][1]
                answer += curr - jobs[i][0]
                jobs.pop(i)
                break

        else:
            curr += 1

    return answer // total
