class Fraction:
    
    #the methods go here
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    def __str__(self): #when printing an instance show this
        return str(self.num)+' / '+str(self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        
        if newnum//common==1 and newden//common==1:
            return 1
        else:
            return Fraction(newnum//common, newden//common)
    
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        
        if newnum//common == 0:
            return 0
        else:
            return Fraction(newnum//common, newden//common)
        
    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        
        if newnum//common == 0:
            return 0
        else:
            return Fraction(newnum//common, newden//common)        
    
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum == secondnum
    
    def show(self):
        print self.num, '/', self.den
