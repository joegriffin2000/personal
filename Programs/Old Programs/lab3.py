from fraction import Fraction

class Summation():
    def __init__(self,n=0,k=1):
        self.__n = n
        self.__k = k
        
    def harmonic(self):
        saved = Fraction(1,self.__k)
        
        while self.__k+1 <= self.__n:
            saved += Fraction(1,self.__k+1)
            self.__k += 1
        
        return saved
    
    def two(self):
        half = Fraction(1,2)
        
        while self.__k <= self.__n:
            half += half
            kValue += 1
            
        return half
    
    def __str__(self):
        H = str(self.harmonic())
        print("(H)=" + H)
        x = H.split('/')
        print("(H)~=" + str(float(x[0])/float(x[1])))
        T = two()
        
        
        
        return ''

def menu():
    usernum = int(input("Enter Number of iterations (integer>0): "))
    
    if usernum == int(usernum):
        print(Summation(usernum))
    else:
        menu()

if __name__ == "__main__":
    summ = Summation()
    print('Welcome to fun with Fractions!')
    menu()