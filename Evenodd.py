# Even numbers are divisible by 2 without remainders. They end in 0, 2, 4, 6, or 8. Odd numbers are not evenly divisible by 2 and end in 1, 3, 5, 7, or 9


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("no. is Even".format(num))
else:
   print("no. is Odd".format(num))
