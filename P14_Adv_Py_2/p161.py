divby5= lambda x: x % 5==0 # cond basically true

num=[1,15,25,66]
a=filter(divby5,num)

print(list(a))