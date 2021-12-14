from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
    def goto_root(person, money):
        if person == "-":
            return

        if money * 0.1 < 1:
            profits[person] += money
        else:
            profits[person] += money - math.floor(money * 0.1)
            goto_root(parents[person], math.floor(money * 0.1))

    parents = defaultdict(str)
    profits = defaultdict(int)
    for i in range(len(enroll)):
        parents[enroll[i]] = referral[i]
        profits[enroll[i]] = 0
    
    for i in range(len(seller)):
        goto_root(seller[i], amount[i] * 100)

    answer = []
    for e in enroll:
        answer.append(profits[e])
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))