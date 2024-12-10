def gcd(a,b):
    if b > a:
        t = a
        a = b
        b = t
    while (b!=0):
        r = a % b
        a = b
        b = r
        
    return a

print("Insert a Number to Find the GCD.")
user1 = int(input("First #:"))
user2 = int(input("Second #:"))

print("")
print("The GCD of",user1,"and",user2,"is",gcd(user1,user2))