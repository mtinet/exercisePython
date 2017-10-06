inputInt = int(input('정수를 입력하세요 : '))
a = 1
count = 0

while a < inputInt :
    if inputInt % a == 0 :
        print(a)
        a += 1
        count += 1
    else :
        a += 1
print('%d의 약수의 개수 :'%(inputInt), count)
