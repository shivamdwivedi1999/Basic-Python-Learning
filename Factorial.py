#n! = n × (n-1) × (n-2) × (n-3) × ….× 3 × 2 × 1


num = int(input("enter the no"))
fact = 1
for i in range(1, num + 1):
    fact=fact*i
print("factorial of ", num, " is ", fact)
