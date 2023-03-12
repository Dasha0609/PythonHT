n = input("Pls enter 3-digit number: ")
n = int(n)
 
a = n % 10
b = n % 100 // 10
c = n // 100
 
print("Sum of all numbers is:", a + b + c)

