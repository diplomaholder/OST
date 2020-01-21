n = int(input("Enter Any Number "))


def isPerfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum += i
    if sum == n:
        return 1

    else:
        return 0

if isPerfect(n):
    print("Perfect Number")

else:
    print("Not A Perfect Number")

    



