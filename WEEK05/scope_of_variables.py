n = 10

def f1():
    print('F1: ',n)

def f2():
    n = 20
    print('F2: ',n)

def f3():
    n = 30
    def inside():
        nonlocal n
        #n = 40
        
        print('F3 :',n)
    inside()

f1()
f2()

f3()
f1()
