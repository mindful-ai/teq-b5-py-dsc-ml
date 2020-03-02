Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import repeat, permutations, combinations
>>> repeat('ANZ', 10)
repeat('ANZ', 10)
>>> list(repeat('ANZ', 10))
['ANZ', 'ANZ', 'ANZ', 'ANZ', 'ANZ', 'ANZ', 'ANZ', 'ANZ', 'ANZ', 'ANZ']
>>> list(permutations('ABCD', 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations('ABCD', 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
>>> ###############
>>> from functools import reduce
>>> reduce(lambda x,y : x+y, [1,2,3,4])
10
>>> ################
>>> L = ['red', 'red', 'green', 'blue', 'green', 'red']
>>> D = {}
>>> for key in L:
	if key in D.keys():
		D[key] = D[key] + 1
	else:
		D[key] = 1

		
>>> D
{'red': 3, 'green': 2, 'blue': 1}
>>> from collections import Counter
>>> z = Counter(L)
>>> z
Counter({'red': 3, 'green': 2, 'blue': 1})
>>> #######################
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 2, 21, 19, 19, 56, 653566)
>>> t.year
2020
>>> t.month
2
>>> t.day
21
>>> t.hour
19
>>> t.minute
19
>>> t.seconds
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t.seconds
AttributeError: 'datetime.datetime' object has no attribute 'seconds'
>>> t.second
56
>>> t.dayname
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t.dayname
AttributeError: 'datetime.datetime' object has no attribute 'dayname'
>>> t.day
21
>>> t.name
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t.name
AttributeError: 'datetime.datetime' object has no attribute 'name'
>>> t.weekday
<built-in method weekday of datetime.datetime object at 0x000002A378717B98>
>>> t.weekday()
4
>>> f = '%A, %d-%B-%Y, %H:%M:%S'
>>> t.strftime(f)
'Friday, 21-February-2020, 19:19:56'
>>> f = '%A, %d-%b-%Y, %H:%M:%S'
>>> t.strftime(f)
'Friday, 21-Feb-2020, 19:19:56'
>>> t = datetime.now()
>>> t.strftime(f)
'Friday, 21-Feb-2020, 19:26:56'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/profiling.py 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------The for loop took:  0:00:00  seconds
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/TEQ-B5-Py/Level01/WEEK04/profiling.py 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------The for loop took:  0:00:09.401391  seconds
>>> ###############################
>>> from operator import itemgetter
>>> f = itemgetter(1)
>>> type(f)
<class 'operator.itemgetter'>
>>> f('apples')
'p'
>>> f(['ant', 'ball', 'cat'])
'ball'
>>> f(([1,2], [3,4], [5,6]))
[3, 4]
>>> L = ['zebra', 'goat', 'dog']
>>> L.sort()
>>> L
['dog', 'goat', 'zebra']
>>> L.sort(key=f)
>>> L
['zebra', 'dog', 'goat']
>>> L.sort(key=itemgetter(-1))
>>> L
['zebra', 'dog', 'goat']
>>> 
