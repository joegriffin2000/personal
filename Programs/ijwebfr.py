# RSA_Algorithm.py
# This script implements the functionality of the RSA encryption algorithm. 
# by Joe Griffin 

#Conversion functions for text-to-ascii & ascii-to-text respectively
def asciiConvert(text):
    return [ord(i) for i in text]
def textConvert(ascii):
    return "".join([chr(i) for i in ascii])

def gcd(a: int, b: int) -> int:
    """Calculates the GCD (Greatest Common Denominator) of two numbers. Used for calculating the e as it needs to be co-prime to phi(n).

    Args:
        a (int): first integer for calcuation.
        b (int): second integer for calcuation.

    Returns:
        int: greatest common denominator between a and b.
    """    
    while b:
        a, b = b, a % b
    return a

def calc_e(phi: int) -> int:
    """Calculates the e value for the public key of the RSA algorithm.

    Args:
        phi (int): phi(n) which is used as an upper bounds on the e value.

    Returns:
        int: the e value. here, it is the lowest co prime number to phi(n).
    """    
    for e in range(2,phi):
        if gcd(e, phi) == 1:
            return e

def modInverse(e: int, phi: int) -> int:
    """Calculates the d value (Modular Multiplicative Inverse of e) for the private key of the RSA Algorithm

    Args:
        e (int): the e value. 
        phi (int): phi(n) which is used as an upper bounds on the d value.

    Returns:
        int: the d value from the modular multiplicative inverse function. here it is the lowest value where it, multiplied by e and modded by phi(n), is equal to 1
    """    
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

if __name__ == "__main__":
    p,q = 13,19
    N = p*q

    phi = (p - 1) * (q - 1)

    e = calc_e(phi)
    d = modInverse(e,phi)

    text = "joseph griffin"
    textASCII = asciiConvert(text) #converting all characters into ascii and storing them in the textASCII as a list

    C = [(i**e) % N for i in textASCII] #encrypting the elements of textASCII using the e 

    print(textConvert(C))

    M = [(i**d) % N for i in C] #decrypting the elements of the cypher text into the original message using d (modular multiplicative inverse of e)

    print(textConvert(M))