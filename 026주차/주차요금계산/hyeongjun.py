# 프로그래머스 주차 요금 계산

# 출차된 내역 x -> 23:59 출차
# 차량별 누적주차 시간 계산
# 차량번호 오름차순으로 주차요금 return

from collections import defaultdict
import math

def solution(fees, records):
    # 기본시간 기본요금 단위시간 단위요금
    basic_min, basic_rate, unit_min, unit_rate = fees

    recorder = defaultdict(int)
    center = defaultdict(int)    
    pay = defaultdict(int)

    for record in records:
        time, car, action = record.split(' ')
        
        # 들어옴
        if action == 'IN':
            sh, sm = time.split(':')
            how_long = (int(sh) * 60) + (int(sm))
            recorder[car] = how_long
        
        # 나감
        else:
            start_time = recorder[car]
            # recorder.remove(car)
            recorder.pop(car)
            eh, em = time.split(':')
            end_time = (int(eh) * 60) + (int(em))
            center[car] += end_time - start_time

    # 출차 내역 X
    for car, val in recorder.items():
            end_time = (23 * 60) + 59
            center[car] += end_time - val

    for car_number, pay_time in center.items():
        # 기본 시간 초과
        if pay_time > basic_min:
            bill = basic_rate + (math.ceil((pay_time - basic_min) / unit_min) * unit_rate)
            pay[car_number] = bill
        # 기본 시간 내
        else:
            pay[car_number] = basic_rate

    answer = sorted(pay.items(), key=lambda x: x[0])
    answer = [i[1] for i in answer]
    return answer
        

print(solution([180, 5000, 10, 600], 
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
# [14841]
