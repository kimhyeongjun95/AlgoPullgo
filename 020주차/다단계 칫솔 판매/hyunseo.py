# 프로그래머스 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    # 추천인
    recommender = {}
    profit = {}
    for i in range(len(enroll)):
        recommender[enroll[i]] = referral[i]
        profit[enroll[i]] = 0
    
    # 이익
    for i in range(len(seller)):
        temp = amount[i]*100
        parents = recommender[seller[i]]
        child = seller[i]
        
        while True:
            profit[child] += temp - temp//10
            temp //= 10
            
            if parents == '-' or temp == 0:
                break
            
            child = parents
            parents = recommender[child]
        
    answer = []
    for p in enroll:
        answer.append(profit[p])
        
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))