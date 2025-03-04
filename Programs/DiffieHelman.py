

#Conversion functions for text-to-ascii & ascii-to-text respectively
def asciiConvert(text):
    return [ord(i) for i in text]
def textConvert(ascii):
    return "".join([chr(i) for i in ascii])

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

    print("Problem 2." )
    print(f"g:{g}")
    print(f"p:{p}")

    print(f"alicePriv:{alicePriv}")
    print(f"bobPriv:{bobPriv}")

    alicePub = power(g, alicePriv, p) # generated alice public
    bobPub = power(g, bobPriv, p) # generated bob public

    print(f"alicePub:{alicePub}")
    print(f"bobPub:{bobPub}")

    aliceSecret = power(bobPub, alicePriv, p)  # Secret key for Alice
    bobSecret = power(alicePub, bobPriv, p)  # Secret key for Bob

    print(f"aliceSecret:{aliceSecret}")
    print(f"bobSecret:{bobSecret}")