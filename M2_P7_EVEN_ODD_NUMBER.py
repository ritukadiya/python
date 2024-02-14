#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
n=int(input("Enter a number : "))

for i in range (1,n+1,1):
    if (i%2==0):
        print(i,"Even Number ")

    else:
        print(i,"Odd Number ")    
