def solution(play_time, adv_time, logs):
    p_h, p_m, p_s = map(int, play_time.split(':'))

    a_h, a_m, a_s = map(int, adv_time.split(':'))
    a_time = 3600*a_h + 60*a_m + a_s

    total = 3600*p_h + 60*p_m + p_s

    dp = [0] * (total + 1) 
    for log in logs:
        start, end = log.split('-')
        s_h, s_m, s_s = map(int, start.split(':'))
        e_h, e_m, e_s = map(int, end.split(':'))
        start = 3600*s_h + 60*s_m + s_s
        end = 3600*e_h + 60*e_m + e_s - 1
        dp[start] += 1
        dp[end] -= 1


    for i in range(1, total):
        dp[i] = dp[i] + dp[i-1]

    for i in range(1, total):
        dp[i] = dp[i] + dp[i-1]

    max_t = 0
    answer = 0
    for i in range(0, total-a_time):
        t = dp[i+a_time] - dp[i]
        if t > max_t:
            max_t = t
            answer = i + 1

    h = answer // 3600
    m = answer % 3600 // 60
    s = answer % 3600 % 60
    
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))