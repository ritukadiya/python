# Program to display the Fibonacci sequence up to n-th term

n=int(input("Enter a value"))

n1=0
n2=1
count=0

print("Fibonacci series: ")
for i in range (1,n+1,1):
    print(n1)
    fibo=n1+n2

    n1=n2
    n2=fibo

