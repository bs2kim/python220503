x = 2
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x = 5
    return a+x

print(func2(1))


g = lambda x,y:x*y
print(g(3,4))
print(globals())