# Write a Python program to get the Factorial number of given number.
n=int(input("Enter a number : "))
fact=1

for i in  range (1,n+1,1):
    fact=fact*i
    
print("factorial of number : ",fact)