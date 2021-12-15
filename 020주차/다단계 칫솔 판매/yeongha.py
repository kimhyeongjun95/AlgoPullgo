def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    dict = {}
    for i, e in enumerate(enroll):
        dict[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = dict[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return money

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))