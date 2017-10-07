print('각 항목별 국어, 수학, 영어의 성적은 다음 dict와 같음')
print()

score = {1:[80, 90,86],
         2:[78,88,85],
         3:[85,85,92],
         4:[70,69,65],
         5:[90,95,100]}

print(score)
print()

for key, value in score.items() :
    print('%d번 -'%(key), '평균 : %.2f'%(sum(value) /len(value)))
    
