import random

def jumble(s):
    l = list(s)
    random.shuffle(l)
    return ''.join(l)

########################################

L = ['monkey', 'giraffe', 'peach', 'computer', 'python']
random.shuffle(L)
points = 0
for word in L:
    pstr = jumble(word)
    print('Can you guess this ? ---> ', pstr)
    ustr = input('??? ')
    if(ustr == word):
        print('Right guess!')
        points += 1
    else:
        print('Wrong guess!')

print('---------------------------------------')
print('You have earned %d points' % points)
