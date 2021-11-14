from itertools import permutations
def solution(expression):
    answer = 0
    operators = []
    numbers = []
    nums = ''
    for i in expression:
        if i.isdigit():
            nums += i
        else:
            numbers.append(int(nums))
            operators.append(i)
            nums = ''
    numbers.append(int(nums))

    uni = set(operators)
    for priority in permutations(uni, len(uni)):
        operators_copy = operators[:]
        numbers_copy = numbers[:]
        for oper in priority:
            result = [numbers_copy[0]]
            new_oper = []
            for i in range(len(operators_copy)):
                if operators_copy[i] == oper:
                    if operators_copy[i] == '+':
                        num = result.pop() + numbers_copy[i+1]
                    elif operators_copy[i] == '-':
                        num = result.pop() - numbers_copy[i+1]
                    else:
                        num = result.pop() * numbers_copy[i+1]
                    result.append(num)
                else:
                    new_oper.append(operators_copy[i])
                    result.append(numbers_copy[i+1])
            numbers_copy = result
            operators_copy = new_oper
        answer = max(answer, abs(numbers_copy[0]))

    return answer

expression = "100-200*300-500+20"
print(solution(expression))