def func(n):
    return lambda x:x*n
result=func(2)
print("Double the number of 15=",result(15))
result=func(3)
print("triple the number of 15=",result(15))
result=func(4)
print("quadruple the number of 15=",result(15))
result=func(5)
print("tquintuple the number of 15=",result(15))
