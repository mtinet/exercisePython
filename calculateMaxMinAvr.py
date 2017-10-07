score = []

for x in range(5) :
    data = int(input('성적을 입력하세요 :'))
    score.append(data) 


print('입력한 성적들 : ', score)
print('최고 성적 : ', max(score))
print('최저 성적 : ', min(score))

avr = sum(score) / len(score)

print('평균 : %.2f'%(avr))
