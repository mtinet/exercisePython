def changeDegree(degreeC) :
    changeF = degreeC *9/5 +32
    return changeF

#main
startC = int(input('시작온도를 입력하시오 :'))
endC = int(input('끝 온도를 입력하시오 :'))

for i in range(startC, endC+1):
    resultF = changeDegree(i)
    print('섭씨 %.2f도는 화씨 %.2f도입니다.'%(i,resultF))
