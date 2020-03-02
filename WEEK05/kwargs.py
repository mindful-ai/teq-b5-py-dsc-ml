def function( **kwargs ):
    print(kwargs)


function(a=10, b=20, c=30)



def multirole(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

multirole(10, 20, 30, 40, 50, 60, x=10, y=20, z=30)
    
multirole(a=30, b=40, c=50)

multirole(2,3,4,m=30, n=40, o=50)
