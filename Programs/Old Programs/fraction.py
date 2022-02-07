class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self,a,b):
        self.num = a
        self.den = b
        self.simplify()
        
    #Print Fraction as a String
    def __str__(self):
        if self.den==1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)
        
    #Get the Numerator
    def getNum(self):
        return self.num
    #Get the Denominator
    def getDen(self):
        return self.den
    
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.num/self.den
    
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.num,self.den)
        self.num = self.num // x
        self.den = self.den // x
        
    #Find the GCD of a and b
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a % b)
        
    #Complete these methods in lab
    #Adding fractions together using gcd
    def __add__(self,other):
        new_num = ((self.num)*(other.den))+((self.den)*(other.num))
        new_den = self.den * other.den
        x = self.gcd(new_num,new_den)
        new_num = new_num // x
        new_den = new_den // x
        
        if new_den==1:
            return Fraction(new_num, 1)
        else:
            return Fraction(new_num, new_den)
    #
    def __sub__(self,other):
        new_other = other
        new_other.num *= -1
        x = self + new_other
        return x
    
    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        
        if new_den==1:
            return Fraction(new_num,1)
        else:
            return Fraction(new_num,new_den)
    
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        
        if new_den==1:
            return Fraction(new_num,1)
        else:
            return Fraction(new_num,new_den)
    
    def __pow__(self,exp):
        if exp < 0:
            new_num = self.den
            new_den = self.num
            
            for i in range(1,exp*-1):
                new_num = new_num * new_num
                new_den = new_den * new_den
                
            x = self.gcd(new_num, new_den)
            new_num = new_num // x
            new_den = new_den // x
            
            if new_den==1:
                return Fraction(new_num,1)
            else:
                return Fraction(new_num,new_den)
        
        elif exp == 0:
            return 1

        else:
            new_num = self.num
            new_den = self.den
            
            for i in range(1,exp):
                new_num *= new_num
                new_den *= new_den
                
            x = self.gcd(new_num, new_den)
            new_num = new_num // x
            new_den = new_den // x
            
            if new_den==1:
                return Fraction(new_num,1)
            else:
                return Fraction(new_num,new_den)
    
if __name__ == "__main__":
    inst1 = Fraction(6,15)
    inst2 = Fraction(30,70)
    print(inst1)
    print(inst2)
    print(inst1 + inst2)