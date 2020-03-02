def genfibo(n):
    fibo = []
    a = 0
    b = 1
    fibo.append(a)
    fibo.append(b)
    for i in range(n-2):
        c = a + b
        fibo.append(c)
        a = b
        b = c

    return(tuple(fibo))

def checkfibo(n):
    a = 0
    if(n == a):
        return True
    b = 1
    if(n == b):
        return True
    while True:
        c = a + b
        if(c == n):
            return True
        elif(c > n):
            return False
        else:
            a = b
            b = c
