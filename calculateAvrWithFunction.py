def calculate(kor, eng, math) :
    total = kor + eng + math
    average = total / 3
    return average

#main
korScore = int(input('국어 성적을 입력하시오:'))
engScore = int(input('영어 성적을 입력하시오:'))
mathScore = int(input('수학 성적을 입력하시오:'))
print()

avr = calculate(korScore, engScore, mathScore)
print('평균 :', avr)
                
