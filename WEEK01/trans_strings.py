Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> type(s)
<class 'str'>
>>> a = 'py'
>>> b = 'th'
>>> c = 'on'
>>> a + b + c
'python'
>>> 12 + 34
46
>>> a * 5
'pypypypypy'
>>> len(s)
6
>>> len(a + b + c)
6
>>> 'tho' in s
True
>>> 'app' in s
False
>>> # del s
>>> #################################
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[-1]
'n'
>>> s[-4]
't'
>>> s[1:5]
'ytho'
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[3:6]
'hon'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> s[::2]
'pto'
>>> s[::1]
'python'
>>> s[1::3]
'yo'
>>> s[::-1]
'nohtyp'
>>> s[::-2]
'nhy'
>>> s[-5:-2]
'yth'
>>> s[-2:-5]
''
>>> ############################################
>>> # case
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> s1 = '213'
>>> s2 = 'df234'
>>> s3 = ' '
>>> s4 = '&^%&^'
>>> s1.isdigit()
True
>>> s2.isdigit()
False
>>> s2.isalnum()
True
>>> s2.isalpha()
False
>>> s3.isspace()
True
>>> s4.isupper()
False
>>> s1.islower()
False
>>> s
'python'
>>> s.islower()
True
>>> s
'python'
>>> s2[0:3].islower()
True
>>> s4
'&^%&^'
>>> chr('&")
    
SyntaxError: EOL while scanning string literal
>>> ord("$")
36
>>> chr(36)
'$'
>>> s2[0:3]
'df2'
>>> s2[0:2]
'df'
>>> s2[0:2].isupper()
False
>>> s2[0:3].islower()
True
>>> s2[0:3].isupper()
False
>>> s5 = '123DFG'
>>> s5[:4].isupper()
True
>>> s5[:4].islower()
False
>>> s[:3].isupper()
False
>>> s[:3].islower()
True
>>> s5[:3].isupper()
False
>>> s5[:3].islower()
False
>>> s5[:5].isupper()
True
>>> s5
'123DFG'
>>> s5.isupper()
True
>>> s5 = '123adv'
>>> s5.isupper()
False
>>> s5.islower()
True
>>> s5 = '123HKkdsf'
>>> s5.islower()
False
>>> s5.isupper()
False
>>> s5
'123HKkdsf'
>>> s5[0:3].isupper()
False
>>> s5
'123HKkdsf'
>>> s5[0:3]
'123'
>>> s5[0:4].isupper()
True
>>> # Searching
>>> 'tho' in s
True
>>> s.find('t')
2
>>> s.index('t')
2
>>> s.index('a')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.index('a')
ValueError: substring not found
>>> s.find('a')
-1
>>> s.count('p')
1
>>> s6 = 'mississippi'
>>> s6.count('s')
4
>>> s6.count('ss')
2
>>> site = 'www.google.com'
>>> site.startswith('www')
True
>>> site.endswith('org')
False
>>> # Modifications
>>> ip = "198-78-2-2"
>>> ip.replace('-','.')
'198.78.2.2'
>>> poem = "twinkle twinkle little star"
>>> poem.split()
['twinkle', 'twinkle', 'little', 'star']
>>> poem.split('e')
['twinkl', ' twinkl', ' littl', ' star']
>>> L = poem.split()
>>> L
['twinkle', 'twinkle', 'little', 'star']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'twinkle-twinkle-little-star'
>>> S = '-'.join(L)
>>> S
'twinkle-twinkle-little-star'
>>> type(S)
<class 'str'>
>>> L
['twinkle', 'twinkle', 'little', 'star']
>>> type(L)
<class 'list'>
>>> s
'python'
>>> s[0] = 'J"
SyntaxError: EOL while scanning string literal
>>> s[0]='J'
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s[0]='J'
TypeError: 'str' object does not support item assignment
>>> s.replace('p', 'j')
'jython'
>>> # Assignments
>>> # Descibe the functions translate and maketrans in python with examples
