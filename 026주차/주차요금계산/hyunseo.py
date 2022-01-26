# 프로그래머스 주차 요금 계산

from collections import defaultdict
import math

def solution(fees, records):
    car_time = defaultdict(int)
    temp = defaultdict(int)
    cars = set()
    
    for record in records:
        time, car, cmd = record.split()
        h, m = time.split(':')
        cars.add(car)
        
        if cmd == 'IN':
            temp[car] += int(h) * 60 + int(m)
        else:
            car_time[car] += int(h) * 60 + int(m) - temp[car]
            del temp[car]
    
    if temp:
        for car, time in temp.items():
            car_time[car] += 23 * 60 + 59 - time
    
    answer = []
    for car in sorted(cars):
        if car_time[car] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((car_time[car] - fees[0]) / fees[2]) * fees[3])
            
    return answer