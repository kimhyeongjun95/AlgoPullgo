def solution(N, number):
    answer = -1
    dp = []

    for i in range(1,9) :
        all_case = set()
        check_number = int(str(N)*i)
        all_case.add(check_number)

        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)

        if number in all_case:
            answer = i
            break

        dp.append(all_case)
        print(dp)       
    return answer

N = 5
number = 12
print(solution(N, number))