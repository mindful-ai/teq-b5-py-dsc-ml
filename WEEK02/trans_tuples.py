Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ('red', 'green', 'blue')
>>> T
('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> T1 = ('magenta', 'cyan')
>>> T + T1
('red', 'green', 'blue', 'magenta', 'cyan')
>>> T
('red', 'green', 'blue')
>>> T1
('magenta', 'cyan')
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> len(T)
3
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T1
>>> T1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> 'red' in T
True
>>> 'black' in T
False
>>> #############################################
>>> T[1]
'green'
>>> T[-1]
'blue'
>>> T[::-1]
('blue', 'green', 'red')
>>> T[::2]
('red', 'blue')
>>> ###############################################
>>> T.index('red')
0
>>> T.count('red')
1
>>> sorted(T)
['blue', 'green', 'red']
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> reversed(T)
<reversed object at 0x000001BEEBC1D8D0>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> for item in reversed(T):
	print(item.upper())

	
BLUE
GREEN
RED
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> 
