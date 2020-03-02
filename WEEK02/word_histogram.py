text = '''
If you fall asleep with me
You can dream and drowse
The minutes turn to hours
We could climb a tree or two
And watch the sun go down
Upon our sleepy town
After all the time I spent with you
Summer went away
And we just weren't the same
It's just you and me alone
Not grown ups but not kids
You kissed me on the lips
Last Chance to Evacuate Planet Earth Before It Is Recycled
'''

words = text.split()

D = {}
for word in words:
    if word in D.keys():
        D[word] = D[word] + 1
    else:
        D[word] = 1

print("WORD HISTOGRAM:")
# print(D)

for word in sorted(D.keys()):
    print(word + ' -------> ' + str(D[word]))
          
