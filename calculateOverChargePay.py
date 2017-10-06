totalWorkingTime = int(input('총 근무시간을 입력하세요 :'))
payPerHour = int(input('시간당 급여를 입력하세요 :'))

if totalWorkingTime <= 12 :
                pay = totalWorkingTime * payPerHour
                print('이번 주 급여는 %d원 입니다.'%(pay))
else :
                pay = (12 * payPerHour) + ((totalWorkingTime - 12) * payPerHour * 1.3)
                print('이번 주 급여는 %d원 입니다.'%(pay))
                 
                    
            
