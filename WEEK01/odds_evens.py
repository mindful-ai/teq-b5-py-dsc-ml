# Program to accept numbers from the user
# separate the odds and evens

# Input

L = []
userin = ''
while userin != 'q':
    userin = input('Enter a number (q to stop): ')
    if(userin.isdigit() == True):
        L.append(int(userin))
    

# Process

print('You have entered the following numbers: ')
print(L)

odds = []
evens = []
for item in L:
    if(item % 2 == 0):
        evens.append(item)
    else:
        odds.append(item)

# Output

print('---------------------------------------')
print('\nODDS:')
print(odds)
print('\nEVENS:')
print(evens)
