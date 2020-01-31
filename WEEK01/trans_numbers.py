Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numbers
>>> a = 10
>>> b = 20
>>> # Arithmetic Operators
>>> a + b
30
>>> a - b
-10
>>> a * b
200
>>> a ** 2
100
>>> a/b
0.5
>>> a//b
0
>>> a % b
10
>>> 3 % 2
1
>>> 5 % 3
2
>>> 5 // 2
2
>>> 5 // 3
1
>>> # Relational Operators
>>> a > b
False
>>> a >= b
False
>>> a < b
True
>>> a <= b/2
True
>>> a + b == 30
True
>>> a + b - 10 != a + b = (2 * 5)
SyntaxError: can't assign to comparison
>>> 
>>> a + b - 10 != a + b  -(2 * 5)
False
>>> # Logical operators
>>> a >= 10 and a < b
True
>>> 10 <= a < b
True
>>> if a + b != 30:
	print('Hello')

	
>>> if not (a+b):
	print('Hello')

	
>>> not(a+b)
False
>>> (a+b)
30
>>> (a-b)
-10
>>> not (a-b)
False
>>> not 0
True
>>> not -1
False
>>> not 1
False
>>> # In-built functions
>>> ord('A')
65
>>> chr(65)
'A'
>>> a = 100
>>> type(a)
<class 'int'>
>>> a = 'python'
>>> type(a)
<class 'str'>
>>> b = b / 1.5
>>> type(b)
<class 'float'>
>>> b
13.333333333333334
>>> hex(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    hex(a)
TypeError: 'str' object cannot be interpreted as an integer
>>> a = 100
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> bin(a)
'0b1100100'
>>> t = hex(a)
>>> type(t)
<class 'str'>
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(t)
ValueError: invalid literal for int() with base 10: '0x64'
>>> int(t , 16)
100
>>> s = '1101'
>>> int(s)
1101
>>> int(s,10)
1101
>>> int(s, 8)
577
>>> int(s, 16)
4353
>>> int(s, 2)
13
>>> input('Enter a number: ')
Enter a number: 456
'456'
>>> i = input('Enter a number: ')
Enter a number: 2134
>>> i
'2134'
>>> type(i)
<class 'str'>
>>> i + 10
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    i + 10
TypeError: can only concatenate str (not "int") to str
>>> int(i) + 10
2144
>>> ################################################
>>> a = 10
>>> a ** 0.5
3.1622776601683795
>>> asqrt = a ** 0.5
>>> a == asqrt ** 2
False
>>> a
10
>>> asqrt ** 2
10.000000000000002
>>> #####################################################
>>> factorial(10)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    factorial(10)
NameError: name 'factorial' is not defined
>>> import math
>>> math.factorial(10)
3628800
>>> math.sqrt(10)
3.1622776601683795
>>> math.gcd(10, 8)
2
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * (3.1416/180))
0.9999999999932537
>>> math.sin(90 * (22/7)/180))
SyntaxError: invalid syntax
>>> math.sin(90 * (22/7)/180)
0.9999998001333682
>>> math.sin(90.math.pi/180)
SyntaxError: invalid syntax
>>>  math.sin(90 * math.pi/180)
 
SyntaxError: unexpected indent
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
18
>>> random.randint(1, 100)
29
>>> random.randint(1, 100)
72
>>> random.randint(1, 100)
80
>>> random.randint(1, 100)
82
>>> random.randint(1, 100)
28
>>> random.randint(1, 100)
86
>>> random.randint(1, 100)
47
>>> 
