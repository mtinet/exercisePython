def weekSalary(hour, pay) :
    totalPay = hour * pay
    if hour > 12 :
        additionalPay = (hour - 12) * pay * 0.3
        totalPay += additionalPay
    return totalPay

#main

workingHour = int(input('근무시간을 입력하세요 :'))
payPerHour = int(input('시간당 급여를 입력하세요 :'))

answer = weekSalary(workingHour, payPerHour)

print()
print('총 급여는 %d입니다'%int(answer))
