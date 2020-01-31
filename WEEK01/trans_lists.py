Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L1 = ['red', 'blue', 'green']
>>> L2 = ['white', 'grey', 'black']
>>> type(L1)
<class 'list'>
>>> L = L1 + L2
>>> L
['red', 'blue', 'green', 'white', 'grey', 'black']
>>> L1 * 3
['red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green']
>>> L
['red', 'blue', 'green', 'white', 'grey', 'black']
>>> len(L)
6
>>> 'red' in L
True
>>> 'green' in L1 + L2
True
>>> L3 = ['red', 'blue', 'green']
>>> del L[1]
>>> L
['red', 'green', 'white', 'grey', 'black']
>>> L3
['red', 'blue', 'green']
>>> del L3
>>> L3
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    L3
NameError: name 'L3' is not defined
>>> ######################################################
>>> L1
['red', 'blue', 'green']
>>> L[1] = 'yellow'
>>> L
['red', 'yellow', 'white', 'grey', 'black']
>>> L[1]
'yellow'
>>> L[1][1]
'e'
>>> L[1][1] = 'x'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    L[1][1] = 'x'
TypeError: 'str' object does not support item assignment
>>> ########################################################
>>> L
['red', 'yellow', 'white', 'grey', 'black']
>>> L[0]
'red'
>>> L[-2]
'grey'
>>> L[2:5]
['white', 'grey', 'black']
>>> L[-3:-1]
['white', 'grey']
>>> L[::2]
['red', 'white', 'black']
>>> L[::-1]
['black', 'grey', 'white', 'yellow', 'red']
>>> L[::1]
['red', 'yellow', 'white', 'grey', 'black']
>>> L[::-1]
['black', 'grey', 'white', 'yellow', 'red']
>>> L[::-2]
['black', 'white', 'red']
>>> ######################################################
>>> # adding elements
>>> L
['red', 'yellow', 'white', 'grey', 'black']
>>> L.append('green')
>>> L
['red', 'yellow', 'white', 'grey', 'black', 'green']
>>> L.append('pink')
>>> L
['red', 'yellow', 'white', 'grey', 'black', 'green', 'pink']
>>> L.insert(1, 'blue')
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'black', 'green', 'pink']
>>> L3 = ['orange', 'magenta', 'cyan']
>>> L.append(L3)
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'black', 'green', 'pink', ['orange', 'magenta', 'cyan']]
>>> L.extend(L3)
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'black', 'green', 'pink', ['orange', 'magenta', 'cyan'], 'orange', 'magenta', 'cyan']
>>> # Remove elements
>>> L.pop()
'cyan'
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'black', 'green', 'pink', ['orange', 'magenta', 'cyan'], 'orange', 'magenta']
>>> L.pop()
'magenta'
>>> L.remove('black')
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'green', 'pink', ['orange', 'magenta', 'cyan'], 'orange']
>>> L.pop(-2)
['orange', 'magenta', 'cyan']
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'green', 'pink', 'orange']
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'green', 'pink', 'orange']
>>> # Searching
>>> L.append('red')
>>> L.append('red')
>>> L.append('green')
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'green', 'pink', 'orange', 'red', 'red', 'green']
>>> 'red' in L
True
>>> L.index('red')
0
>>> L.count('red')
3
>>> # Rearranging
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'green', 'pink', 'orange', 'red', 'red', 'green']
>>> reversed(L)
<list_reverseiterator object at 0x000002C0A19440B8>
>>> list(reversed(L))
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red']
>>> L
['red', 'blue', 'yellow', 'white', 'grey', 'green', 'pink', 'orange', 'red', 'red', 'green']
>>> L.reverse()
>>> L
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red']
>>> L5
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    L5
NameError: name 'L5' is not defined
>>> L5 = ['zebra', 'donkey', 'monkey', 'ant', 'cat']
>>> sorted(L5)
['ant', 'cat', 'donkey', 'monkey', 'zebra']
>>> L5
['zebra', 'donkey', 'monkey', 'ant', 'cat']
>>> L5.sort()
>>> L5
['ant', 'cat', 'donkey', 'monkey', 'zebra']
>>> L5.sort(reverse=True)
>>> L5
['zebra', 'monkey', 'donkey', 'cat', 'ant']
>>> ##################################################################3
>>> L
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red']
>>> L1 = L
>>> L1
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red']
>>> L1.append('magenta')
>>> L1
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L2 = L[:]
>>> L2
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L2.append('cyan')
>>> L
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L1
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L2
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta', 'cyan']
>>> from copy import deepcopy
>>> L5 = deepcopy(L)
>>> L
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L5
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> L.append('brown')
>>> L
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta', 'brown']
>>> L1
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta', 'brown']
>>> L2
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta', 'cyan']
>>> L5
['green', 'red', 'red', 'orange', 'pink', 'green', 'grey', 'white', 'yellow', 'blue', 'red', 'magenta']
>>> 
