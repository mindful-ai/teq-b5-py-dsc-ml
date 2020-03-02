def average(a, b):
    return (a + b) / 2


#print(average(10, 20))
#print(average(10, 20, 30))

def avg(*args ):
    print(args)
    return sum(args)/len(args)

print(avg(10, 20, 30, 40, 50, 60))

