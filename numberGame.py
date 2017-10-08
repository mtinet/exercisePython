import random

cnt = 1
r = random.randint(1, 100)


print('컴퓨터가 임의의 값을 선택하였습니다.')

for i in range(10) :
    val = int(input('컴퓨터가 선택한 숫자를 맞춰보세요 : '))
    print()

    if r > val :
        print('더 큰 수를 선택하세요.')
        print()
        cnt += 1
    elif r < val :
        print('더 작은 수를 선택하세요.')
        print()
        cnt += 1
    else :
        print()
        print('정답입니다! %d번만에 맞췄습니다. 입력한 숫자는 %d입니다.'%(cnt, r))
        break
        
