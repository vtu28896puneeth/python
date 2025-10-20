def operation(func):
    def wrapper(x,y):
        print("performing arithmetic operations")
        result=func(x,y)
        print("is operation completed")
        return result
    return wrapper
@operation
def add(x,y):
    return x+y
@operation
def div(x,y):
    if y==0:
        return("Cannot divided by Zero")
    else:
        return x/y
result=add(5,3)
print("Result of addtion: ",result)
result_div=div(5,3)
print("result of division: ",result_div)
