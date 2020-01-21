def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    
    return fact

n = int(input("Enter Any Number "))
n1 = n

m=0

while n!=0:
    d = n%10
    m = m + fact(d)
    n = n//10

if m == n1:
    print("Krishnamurthi number")

else:
    print("Not A Krishnamurthi Number")
