# Program to identify if the result of subtraction
# is positive, negative or zero

# input

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))


# process

d = a - b

# output

print('RESULT:' , d)
if( d > 0 ):
    print('The result is positive')
elif(d < 0):
    print('THe result is negative')
else:
    print('The result is zero')
