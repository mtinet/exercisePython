n = int(input('정수를 입력하시오 :'))
max = n

loopCount = 1
while loopCount <= 4 :
    n = int(input('정수를 입력하시오 :'))
    if n > max :
        max = n
    loopCount += 1

print()
print('가장 큰 값은 %d입니다.'%(max))

