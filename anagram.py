# Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.


# Input : s1 = "dad"
#         s2 = "bad"
# Output : The strings aren't anagrams.

num1=input("Enter the first no")
num2=input("Enter the second no")
if (sorted(num1)==sorted(num2)):
    print("yes this is Anagram ")
else:
    print("no this is not Anagram no")