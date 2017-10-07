def addMultiply(x, y) :
    sum = x + y
    mult = x * y
    return sum, mult

#main
a = int(input('Enter a : '))
b = int(input('Enter b : '))

m, n = addMultiply(a, b)

print(m,n)
