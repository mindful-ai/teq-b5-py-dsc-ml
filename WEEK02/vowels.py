# Program to find the count of vowels

txt = input('Enter some text: ')
txt = txt.lower()

vowels = 'aeiou'

for c in vowels:
    print('%s occurs %d times' % (c, txt.count(c)))
    
