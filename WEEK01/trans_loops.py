Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in 'python':
	print(i)

	
p
y
t
h
o
n
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(1, 100, 10))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
>>> print(5 + ' X ' + 1 + ' = ' + 5*1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(5 + ' X ' + 1 + ' = ' + 5*1)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(str(5) + ' X ' + str(1) + ' = ' + str(5*1))
5 X 1 = 5
>>> for i in 'abcdefghij':
	print(str(5) + ' X ' + str(1) + ' = ' + str(5*1))

	
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(1, 11):
	print(str(5) + ' X ' + str(i) + ' = ' + str(5*i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 5 + 5
10
>>> 5 + 'd'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    5 + 'd'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(5) + 'd'
'5d'
>>> i = 0
>>> while i < 11:
	i += 1
	print(str(5) + ' X ' + str(i) + ' = ' + str(5*i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
5 X 11 = 55
>>> 
