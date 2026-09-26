a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=int(input('enter 3rd number'))
if a>b and a>c:
    print (f'{a} is the greatest number')
elif b>a and b>c:
    print (f'{b} is the greatest number')
elif c>a and c>b:
    print (f'{c} is the greatest number')
else :
    print ('wrong command')