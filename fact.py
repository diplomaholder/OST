def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    
    return fact

n = int(input("Enter Any Number "))


f = fact(n)

print(f"The Factorial of {n} is {f}")