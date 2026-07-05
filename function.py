def factorial():
    n=int(input("enter a number:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print("factorial of ",n,"is",fact)
factorial()

print("<--------------------->")
def fibonacci():
    n=int(input("enter a number:"))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci()

print("<---------------------->")
def prime():
    n=int(input("enter a number:"))
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
prime()

print("<----------------------->")
def armstrong():
    n=int(input("enter a number:"))
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
        if sum==n:
            print(n,"is a armstrong number")
    else:
        print(n,"is not an armstrong number")
armstrong()

print("<----------------------->")
def palindrome():
    n=int(input("enter a number:"))
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
        if rev==n:
            print(n,"is a palindrome")
        else:
            print(n,"is not a palindrome")
palindrome()