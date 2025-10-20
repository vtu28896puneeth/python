nums=list(input("enter a sequence of comma-separated 4-digit binary number:").split(','))
res=[i for i in nums if int(i,2)%6==0]
print(res)
