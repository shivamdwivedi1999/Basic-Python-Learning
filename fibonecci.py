#0,1,1,2,3,5,8,13,21,34..............

n=int(input("enter the digit"))
t1=0
t2=1
print(0)
print(1)
for i in range (t1,n):
    nextTerm = t1 + t2
    t1 = t2
    t2 = nextTerm
    print(nextTerm)