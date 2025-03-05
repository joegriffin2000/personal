# Diffie_Hellman.py
# This script implements the functionality of the RSA encryption algorithm. 
# by Joe Griffin 

LB = "-"*100

def power(a, b, m):
    if b == 1:
        return a
    else:
        return pow(a, b) % m
    
if __name__ == "__main__":
    g = 10 #generator
    p = 541 #prime

    alicePriv = 11
    bobPriv = 13

    print("Problem 2.")
    print("For this problem, I put each step of my calculation in its own section and divided them with linebreaks.")
    print("First, I named all of my knowns, then I calulated both public keys, and then finally I showed the matching secrets.")
    print(LB)
    print(f"{"(generator)":^20}| {"g":^16}:{g:^10}")
    print(f"{"(prime)":^20}| {"p":^16}:{p:^10}")
    print(f"{"(alice private)":^20}| {"alicePriv":^16}:{str(alicePriv):^10}")
    print(f"{"(bob private)":^20}| {"bobPriv":^16}:{str(bobPriv):^10}")
    
    print(LB)
    print(f"{"(alice public)":^20}| {"alicePub":^16}: {"(g)^alicePriv % p":^24}: {f"({g})^{alicePriv} % {p}":^10}")
    print(f"{"(bob public)":^20}| {"bobPub":^16}: {"(g)^bobPriv % p":^24}: {f"({g})^{bobPriv} % {p}":^10}")

    print(LB)

    alicePub = power(g, alicePriv, p) # generated alice public
    bobPub = power(g, bobPriv, p) # generated bob public

    print(f"{"(alice public)":^20}| {"alicePub":^16}:{str(alicePub):^10}")
    print(f"{"(bob public)":^20}| {"bobPub":^16}:{str(bobPub):^10}")
    print(LB)

    print(f"{"(alice secret)":^20}| {"aliceSecret":^16}: {"(bobPub)^alicePriv % p":^24}: {f"({bobPub})^{alicePriv} % {p}":^10}")
    print(f"{"(bob secret)":^20}| {"bobSecret":^16}: {"(alicePub)^bobPriv % p":^24}: {f"({alicePub})^{bobPriv} % {p}":^10}")
    print(LB)

    aliceSecret = power(bobPub, alicePriv, p)  # Secret key for Alice
    bobSecret = power(alicePub, bobPriv, p)  # Secret key for Bob

    print(f"{"(alice secret)":^20}| {"aliceSecret":^16}:{str(aliceSecret):^10}")
    print(f"{"(bob secret)":^20}| {"bobSecret":^16}:{str(bobSecret):^10}")