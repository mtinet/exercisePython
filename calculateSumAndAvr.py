korean = int(input('input your Korean rate :'))
math = int(input('input your Math rate :'))
english = int(input('input your English rate :'))

print()
print('Input rate\n------------')
print('Korean rate = %d'%(korean))
print('Math rate = %d'%(math))
print('English rate = %d'%(english))
print('------------')
print()

sum = korean + math + english
avr = sum / 3
print('sum = %d'%(sum))
print('avr = %.2f'%(avr))
      
