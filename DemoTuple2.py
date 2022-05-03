# DemoTuple.py

a={1,2,3,3}
print(a)
print(type(a))
b = {3,4,4,5}
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple연습
tp=(1,2,3)
print(type(tp))
print(len(tp))
print(tp[0])

def times(a,b):
    return a+b, a*b

result = times(3,4)
print(result)

