# Program to build the multiplication table

# Input

n = int(input('Enter a number for creating the multiplication table: '))

# Process
# OUtput

for i in range(1, 11):
	print(str(n) + ' X ' + str(i) + ' = ' + str(n*i))
