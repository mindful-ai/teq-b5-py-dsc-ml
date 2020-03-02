from datetime import datetime

t1 = datetime.now()

for i in range(1000):
    print('-',end='')

t2 = datetime.now()

print('The for loop took: ', t2 - t1, ' seconds')

