def solution(enroll, referral, seller, amount):
	# key = 판매원, value = key를 추천한 추천인
    head = dict()
    # key = 판매원, value = key의 이익
    profit = dict()
    
    for e, r in zip(enroll, referral):
        head[e] = r
        profit[e] = 0

    for name, m in zip(seller, amount):
        # 판매수익
        price = 100 * m
        
        while True:
            # 추천인이 "-" 이거나 판매수익이 0이면
            if name == "-" or price <= 0:
                break

            # 추천인에게 줘야 할 이익금의 10%인 fee를 뺀 나머지를 판매원의 수익에 더함    
            next_money = int(price * 0.1)
            profit[name] += price - next_money
            # 다음 추천인 탐색
            name = head[name]
            price = next_money
    
    return list(profit.values())
