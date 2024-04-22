# natural numbers that are divisible by only 1 and the number itself. 



A=int(input("enter the no  : "))

if A>1:
    for i in range(2,A):
        if (A%i)==0:
            print("it is not prime number")
            break
    else:
        print("no. is prime no")
else:
    print("it is not prime no")
