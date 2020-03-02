Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> set(s)
{'i', 'm', 's', 'p'}
>>> s = {'a', 'b', 'c', 'd', 'e', 'f'}
>>> s
{'a', 'f', 'b', 'c', 'e', 'd'}
>>> s1 = set('defghi')
>>> s1
{'i', 'h', 'f', 'g', 'e', 'd'}
>>> s + s1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s + s1
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s * 3
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s * 3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> 'a' in s
True
>>> ########################################################
>>> s & s1
{'e', 'd', 'f'}
>>> s | s1
{'i', 'a', 'f', 'h', 'b', 'g', 'c', 'e', 'd'}
>>> s ^ s1
{'i', 'a', 'b', 'c', 'h', 'g'}
>>> ##########################################################
>>> s.add('x')
>>> s
{'a', 'f', 'b', 'c', 'e', 'x', 'd'}
>>> s2 = { 'y', 'z' }
>>> s.update(s2)
>>> s
{'a', 'f', 'b', 'z', 'c', 'e', 'y', 'x', 'd'}
>>> len(s)
9
>>> s
{'a', 'f', 'b', 'z', 'c', 'e', 'y', 'x', 'd'}
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s.remove('f')
>>> s
{'a', 'b', 'z', 'c', 'e', 'y', 'x', 'd'}
>>> s.pop('y')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.pop('y')
TypeError: pop() takes no arguments (1 given)
>>> s.pop()
'a'
>>> s
{'b', 'z', 'c', 'e', 'y', 'x', 'd'}
>>> s.pop()
'b'
>>> s.intersection(s1)
{'d', 'e'}
>>> s.union(s1)
{'i', 'h', 'f', 'g', 'z', 'c', 'e', 'y', 'x', 'd'}
>>> 
