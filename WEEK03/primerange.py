
# import required modules
import myprime

# input
start = int(input('Enter a start point: '))
end = int(input('Enter the end end point: '))

# process
primes = []
for num in range(start, end+1): # start of the for loop
    if(myprime.checkprime(num)): # check if the number is prime
        primes.append(num) # append it to the master list if found prime

# output
print('PRIMES:')
print(primes)
