import random

m_pg = ['madagascar', 'ratatouille', 'tarzan', 'cars', 'frozen']
m_13 = ['terminator', 'x-men', 'avengers', 'black panther', 'transformers']
m_18 = ['joker', 'revanant', 'conjuring', 'insideous', 'expendables']

# Collect user information

name = input('Enter your name: ')
age  = int(input('Enter your age: '))

# select the movies

if (age < 13):
    m1 = random.choice(m_pg)
    m2 = random.choice(m_pg)
elif (13 <= age < 18):
    m1 = random.choice(m_13)
    m2 = random.choice(m_13 + m_pg)
else:
    m1 = random.choice(m_18)
    m2 = random.choice(m_18 + m_13 + m_pg)

# Present the movies recommendations

print('-'*60)
print('Hi! ', name)
print('You could watch the following movies this weekend: ')
print('1. ', m1)
print('2. ', m2)
