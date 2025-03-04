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
    p,q = 7,19
    N = p*q
    phi = (p - 1) * (q - 1)
    AN,Ae = 21,5

    e = calc_e(phi)
    d = modInverse(e,phi) #(modular multiplicative inverse of e)

    text = "\"joseph griffin\""
    #text = input("Please Enter the Text to be Encrypted\n:").strip()
    textASCII = asciiConvert(text) #converting all characters into ascii and storing them in the textASCII as a list

    S = [(i**e) % N for i in textASCII]         # signing the elements of textASCII using my private
    AC = [(i**Ae) % AN for i in textASCII]      # encrypting the elements of textASCII using my private
    AC_S = [(i**d) % N for i in AC]             # signing the elements of the message encrypted with alice's public key
    S_AC = [(i**Ae) % AN for i in S]            # encrypting the elements of the message signed with my privat key
    V = [(i**d) % N for i in S]                 # verifying the elements of the signed text into the original message using my public 

    print("Problem 1.")
    print("Part 1.")
    print("For this Section, I listed out all the components of my public/private key as well as Alice's Public key")
    print(f"{"(prime 1)":^20}| {"p":^9}:{p:^10}")
    print(f"{"(prime 2)":^20}| {"q":^9}:{q:^10}")
    print(f"{"(public key)":^20}| {"(N,e)":^9}:{f"({N},{e})":^10}")
    print(f"{"(private key)":^20}| {"(N,d)":^9}:{f"({N},{d})":^10}")
    print(f"{"(alice public key)":^20}| {"(AN,Ae)":^9}:{f"({AN},{Ae})":^10}")
    print()
    
    print("Part 2.")
    print("For this section I simply, took the plaintext of my name and encrypted it with Alice's public")
    print(f"{"(original text)":^30}| {"text":^12}: {text:>80}")
    print(f"{"(ascii value)":^30}| {"textASCII":^12}: {str(textASCII):>80}")
    print(f"{"(encrypted with alice public)":^30}| {"AC":^12}: {str(AC):>80}") 
    print()

    print("Part 3.")
    print("For this section, I signed the plaintext with my private key")
    print(f"{"(original text)":^30}| {"text":^12}: {text:>80}")
    print(f"{"(ascii value)":^30}| {"textASCII":^12}: {str(textASCII):>80}")
    print(f"{"(signed with private)":^30}| {"S":^12}: {str(S):>80}") 
    print()
    print(f"{"(verified as text)":^30}| {"V":^12}: {str(textConvert(V)):>80}") 
    print()

    print("Part 4.")
    print(f"{"(original text)":^30}| {"text":^12}: {text:>80}")
    print(f"{"(ascii value)":^30}| {"textASCII":^12}: {str(textASCII):>80}")
    print(f"{"(encrypted with alice public)":^30}| {"AC":^12}: {str(AC):>80}")
    print(f"{"(signed with my private)":^30}| {"AC_S":^12}: {str(AC_S):>80}")
    print()
    print(f"{"(verified with my public)":^30}| {"AC_V":^12}: {str([(i**e) % N for i in AC_S]):>80}")
    print()

    print("Part 5.")
    print(f"{"(original text)":^30}| {"text":^12}: {text:>80}")
    print(f"{"(ascii value)":^30}| {"textASCII":^12}: {str(textASCII):>80}")
    print(f"{"(signed ascii)":^30}| {"S":^12}: {str(S):>80}")
    print(f"{"(encrypted with alice public)":^30}| {"S_AC":^12}: {str(S_AC):>80}")
    print()

