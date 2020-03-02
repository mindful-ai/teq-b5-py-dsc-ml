Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = lambda x,y : x+y
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f('Hello',' World')
'Hello World'
>>> f([1,2,3],['a', 'b', 'c'])
[1, 2, 3, 'a', 'b', 'c']
>>> L = ['zebra', 'goat', 'sheep', 'giraffe', 'donkey']
>>> L.sort()
>>> L
['donkey', 'giraffe', 'goat', 'sheep', 'zebra']
>>> L.sort(key=lambda s : s[-1])
>>> L
['zebra', 'giraffe', 'sheep', 'goat', 'donkey']
>>> def sortkey(item):
	return item[1]

>>> L.sort(key=sortkey)
>>> L
['zebra', 'sheep', 'giraffe', 'goat', 'donkey']
>>> L.sort(key=lambda item : item[1])
>>> L
['zebra', 'sheep', 'giraffe', 'goat', 'donkey']
>>> ###########################################################
>>> C = [10, 30, 50, 70, 80]
>>> F = []
>>> for t in C:
	f = t * 1.8 + 32
	F.append(f)

	
>>> F
[50.0, 86.0, 122.0, 158.0, 176.0]
>>> F2 = map(lambda t : t * 1.8 + 32, C)
>>> F2
<map object at 0x0000022964F54E10>
>>> list(F2)
[50.0, 86.0, 122.0, 158.0, 176.0]
>>> ##########################################################
>>> import random
>>> rn = []
>>> for i in range(100):
	rn.append(random.randint(1, 100))

	
>>> rn
[48, 36, 4, 14, 56, 77, 83, 54, 1, 59, 59, 56, 74, 26, 28, 75, 44, 47, 75, 65, 76, 71, 10, 59, 81, 31, 4, 46, 71, 24, 18, 82, 38, 42, 22, 96, 15, 17, 56, 70, 77, 81, 100, 4, 51, 51, 28, 52, 35, 85, 32, 20, 15, 27, 5, 91, 21, 23, 96, 35, 10, 27, 93, 71, 71, 69, 43, 82, 16, 64, 6, 86, 19, 43, 59, 60, 95, 43, 41, 21, 31, 94, 67, 1, 50, 25, 47, 29, 5, 3, 44, 89, 81, 30, 88, 40, 81, 77, 53, 48]
>>> div7 = []
>>> for n in rn:
	if(n % 7 == ):
		
SyntaxError: invalid syntax
>>> for n in rn:
	if(n % 7 == 0):
		div7.append(n)

		
>>> n
48
>>> div7
[14, 56, 77, 56, 28, 42, 56, 70, 77, 28, 35, 91, 21, 35, 21, 77]
>>> div7_2 = filter(lambda n : (n % 7 == 0), rn)
>>> div7_2
<filter object at 0x0000022964F51668>
>>> list(div7_2)
[14, 56, 77, 56, 28, 42, 56, 70, 77, 28, 35, 91, 21, 35, 21, 77]
>>> ######################################################################
>>> T1 = ('Mehzabeen', 'Rashmi', 'Karuna', 'Niharika')
>>> T2 = ('Bellary', 'Dharwad', 'Bengaluru', 'Bengaluru')
>>> T1 + T2
('Mehzabeen', 'Rashmi', 'Karuna', 'Niharika', 'Bellary', 'Dharwad', 'Bengaluru', 'Bengaluru')
>>> for i in range(len(T1)):
	print((T1[i], T2[i]))

	
('Mehzabeen', 'Bellary')
('Rashmi', 'Dharwad')
('Karuna', 'Bengaluru')
('Niharika', 'Bengaluru')
>>> T3 = zip(T1, T2)
>>> T3
<zip object at 0x0000022964D2BDC8>
>>> list(T3)
[('Mehzabeen', 'Bellary'), ('Rashmi', 'Dharwad'), ('Karuna', 'Bengaluru'), ('Niharika', 'Bengaluru')]
>>> zip(*T3)
<zip object at 0x0000022964FEBC48>
>>> T4 = zip(*T3)
>>> T4
<zip object at 0x0000022964D2B848>
>>> list(T4)
[]
>>> list(zip(*T3))
[]
>>> T3 = zip(T1, T2)
>>> T3
<zip object at 0x0000022964FEBD88>
>>> list(T3)
[('Mehzabeen', 'Bellary'), ('Rashmi', 'Dharwad'), ('Karuna', 'Bengaluru'), ('Niharika', 'Bengaluru')]
>>> list(T30

     )
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list(T30
NameError: name 'T30' is not defined
>>> list(T3)
[]
>>> T3 = zip(T1, T2)
>>> T4 = zip(*T3)
>>> T4
<zip object at 0x0000022964FEBD88>
>>> list(T4)
[('Mehzabeen', 'Rashmi', 'Karuna', 'Niharika'), ('Bellary', 'Dharwad', 'Bengaluru', 'Bengaluru')]
>>> T4
<zip object at 0x0000022964FEBD88>
>>> T4[0]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    T4[0]
TypeError: 'zip' object is not subscriptable
>>> T4 = list(T4)
>>> T4[0]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    T4[0]
IndexError: list index out of range
>>> T4
[]
>>> T = [('Mehzabeen', 'Rashmi', 'Karuna', 'Niharika'), ('Bellary', 'Dharwad', 'Bengaluru', 'Bengaluru')]
>>> list(zip(T[0], T[1]))
[('Mehzabeen', 'Bellary'), ('Rashmi', 'Dharwad'), ('Karuna', 'Bengaluru'), ('Niharika', 'Bengaluru')]
>>> #############################################################
>>> T1 = ('Mehzabeen', 'Rashmi', 'Karuna', 'Niharika')
>>> enumerate(T1)
<enumerate object at 0x0000022964F964C8>
>>> list(enumerate(T1))
[(0, 'Mehzabeen'), (1, 'Rashmi'), (2, 'Karuna'), (3, 'Niharika')]
>>> ##################################################################
>>> i = 10
>>> while i > 0:
	print(i)
	i -= 1

	
10
9
8
7
6
5
4
3
2
1
>>> range(10, 20)
range(10, 20)
>>> range(-10, -20)
range(-10, -20)
>>> list(range(-10, -20))
[]
>>> list(range(-20, -10))
[-20, -19, -18, -17, -16, -15, -14, -13, -12, -11]
>>> 
