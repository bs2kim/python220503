def setValue(newValue):
    x = newValue
    print("함수내부:", x)

retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

retValue = swap(3,4)
print(retValue)
