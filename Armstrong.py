#407= 4^3+0^3+7^3
#345= 3^3+4^3+5^3

#371 = (3*3*3)+(7*7*7)+(1*1*1)  
#where:  
#(3*3*3)=27  
#(7*7*7)=343  
#(1*1*1)=1  
#So:  
#27+343+1=371 

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
