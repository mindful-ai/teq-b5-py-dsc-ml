Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello Python Guys!')
Hello Python Guys!
>>> a = 10
>>> b = 20
>>> a + b
30
>>> a * b
200
>>> a > b
False
>>> a < b and b < 30
True
>>> a < b and b < 10
False
>>> s = '1234'
>>> a
10
>>> s
'1234'
>>> type(a)
<class 'int'>
>>> type(s)
<class 'str'>
>>> s + 1000
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s + 1000
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 1000
2234
>>> float(s) + 1000
2234.0
>>> x = 10 - 20
>>> x
-10
>>> abs(x)
10
>>> sin(90)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sin(90)
NameError: name 'sin' is not defined
>>> import math
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14156/180)
0.9999999998667178
>>> math.sin(
	)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    math.sin(
TypeError: sin() takes exactly one argument (0 given)
>>> math.sin(math.radians(90))
1.0
>>> 
======== RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B6/demo.py ========
Enter a number: 12
Enter another number: 23
SUM:  35
>>> ######################################
>>> s = 'apples'
>>> l = list(s)
>>> l
['a', 'p', 'p', 'l', 'e', 's']
>>> import random
>>> random.shuffle(l)
>>> l
['e', 'a', 'p', 'l', 's', 'p']
>>> ''.join(l)
'eaplsp'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/word_jumble.py 
myokne
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/word_jumble.py 
kmneoy
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/word_jumble.py 
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/word_jumble.py", line 13, in <module>
    for word in random.shuffle(L):
TypeError: 'NoneType' object is not iterable
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/word_jumble.py 
Can you guess this ? --->  aechp
??? peach
Right guess!
Can you guess this ? --->  ykeomn
??? monkey
Right guess!
Can you guess this ? --->  ytpnoh
??? pthons
Wrong guess!
Can you guess this ? --->  umocrept
??? alskdfer
Wrong guess!
Can you guess this ? --->  iagerff
??? giragge
Wrong guess!
---------------------------------------
You have earned 2 points
>>> rn = []
>>> for i in range(100):
	rn.append(random.randint(1, 100))

	
>>> rn
[19, 39, 99, 46, 64, 83, 14, 83, 13, 93, 52, 25, 75, 51, 55, 54, 68, 80, 68, 43, 64, 45, 12, 12, 99, 60, 53, 28, 45, 57, 74, 66, 68, 73, 44, 95, 55, 41, 51, 16, 85, 59, 81, 14, 60, 36, 20, 43, 8, 57, 2, 10, 71, 69, 21, 11, 57, 94, 1, 32, 91, 35, 99, 47, 92, 41, 12, 1, 28, 97, 91, 69, 2, 10, 76, 6, 44, 1, 54, 84, 91, 91, 2, 16, 81, 24, 73, 84, 81, 100, 42, 22, 49, 68, 19, 48, 23, 35, 39, 55]
>>> rnc = [random.randint(1, 100) for i in range(100)]
>>> rnc
[20, 44, 72, 86, 63, 100, 53, 52, 82, 12, 74, 47, 85, 69, 75, 54, 17, 3, 13, 83, 70, 87, 8, 32, 87, 32, 61, 18, 17, 11, 57, 75, 51, 2, 9, 26, 24, 74, 5, 49, 27, 65, 51, 59, 89, 76, 98, 3, 36, 8, 87, 53, 36, 51, 92, 65, 92, 78, 10, 37, 33, 12, 13, 40, 98, 43, 59, 60, 28, 98, 15, 44, 83, 50, 6, 53, 67, 52, 1, 6, 49, 65, 96, 7, 63, 90, 14, 50, 96, 54, 57, 40, 64, 20, 90, 25, 65, 28, 61, 85]
>>> rnc = [x = random.randint(1, 100) for i in range(100) if x % 2]
SyntaxError: invalid syntax
>>> rnc
[20, 44, 72, 86, 63, 100, 53, 52, 82, 12, 74, 47, 85, 69, 75, 54, 17, 3, 13, 83, 70, 87, 8, 32, 87, 32, 61, 18, 17, 11, 57, 75, 51, 2, 9, 26, 24, 74, 5, 49, 27, 65, 51, 59, 89, 76, 98, 3, 36, 8, 87, 53, 36, 51, 92, 65, 92, 78, 10, 37, 33, 12, 13, 40, 98, 43, 59, 60, 28, 98, 15, 44, 83, 50, 6, 53, 67, 52, 1, 6, 49, 65, 96, 7, 63, 90, 14, 50, 96, 54, 57, 40, 64, 20, 90, 25, 65, 28, 61, 85]
>>> evens = [x for x in rnc if x % 2 == 0]
>>> evens
[20, 44, 72, 86, 100, 52, 82, 12, 74, 54, 70, 8, 32, 32, 18, 2, 26, 24, 74, 76, 98, 36, 8, 36, 92, 92, 78, 10, 12, 40, 98, 60, 28, 98, 44, 50, 6, 52, 6, 96, 90, 14, 50, 96, 54, 40, 64, 20, 90, 28]
>>> import myprime
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    import myprime
ModuleNotFoundError: No module named 'myprime'
>>> k = list(range(10))
>>> k
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L = [(x, x**2) for x in k]
>>> L
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
>>> L = [x**2 for x in k]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> L = ['monkey', 'giraffe', 'peach', 'computer', 'python']
>>> dc = {s : len(s) for s in L }
>>> dc
{'monkey': 6, 'giraffe': 7, 'peach': 5, 'computer': 8, 'python': 6}
>>> from collections import Counter
>>> dc = { s : {len(s), Counter(list(s))} for s in L}
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dc = { s : {len(s), Counter(list(s))} for s in L}
  File "<pyshell#55>", line 1, in <dictcomp>
    dc = { s : {len(s), Counter(list(s))} for s in L}
TypeError: unhashable type: 'Counter'
>>> Counter(list(s))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    Counter(list(s))
NameError: name 's' is not defined
>>> Counter(list(s[0]))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    Counter(list(s[0]))
NameError: name 's' is not defined
>>> Counter(list(L[0]))
Counter({'m': 1, 'o': 1, 'n': 1, 'k': 1, 'e': 1, 'y': 1})
>>> dc = { s : {len(s), dict(Counter(list(s)))} for s in L}
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dc = { s : {len(s), dict(Counter(list(s)))} for s in L}
  File "<pyshell#59>", line 1, in <dictcomp>
    dc = { s : {len(s), dict(Counter(list(s)))} for s in L}
TypeError: unhashable type: 'dict'
>>> dc = { s : (len(s), dict(Counter(list(s)))) for s in L}
>>> dc
{'monkey': (6, {'m': 1, 'o': 1, 'n': 1, 'k': 1, 'e': 1, 'y': 1}), 'giraffe': (7, {'g': 1, 'i': 1, 'r': 1, 'a': 1, 'f': 2, 'e': 1}), 'peach': (5, {'p': 1, 'e': 1, 'a': 1, 'c': 1, 'h': 1}), 'computer': (8, {'c': 1, 'o': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'e': 1, 'r': 1}), 'python': (6, {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})}
>>> dc['monkey']
(6, {'m': 1, 'o': 1, 'n': 1, 'k': 1, 'e': 1, 'y': 1})
>>> L
['monkey', 'giraffe', 'peach', 'computer', 'python']
>>> n = list(range(10))
>>> n
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L = [x**3 for x in n if n == 7]
>>> L
[]
>>> n
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L = [x**3 for x in n if x == 7]
>>> L
[343]
>>>  L = [x**3 if x == 7 else x for x in n]
 
SyntaxError: unexpected indent
>>> L = [x**3 if x == 7 else x for x in n]
>>> L
[0, 1, 2, 3, 4, 5, 6, 343, 8, 9]
>>> 
