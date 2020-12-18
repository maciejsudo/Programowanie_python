#Maciej Sudol 303073
#Elektronika AGH 3 rok
import numpy as np

class my_complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def abs(self):
        return np.sqrt(self.r*self.r+self.i*self.i)

    def mult(self, other):
        new_r = self.r * other.r - self.i * other.i
        new_i = self.i * other.r + self.r * other.i
        return my_complex(new_r, new_i)

    def add(self, other):
        new_r = self.r + other.r
        new_i = self.i + other.i
        return my_complex(new_r, new_i)

    def sub(self, other):
        new_r = self.r - other.r
        new_i = self.i - other.i
        return my_complex(new_r, new_i)

    def conj(self):
        new_r = self.r
        new_i = -1*self.i
        return my_complex(new_r, new_i)

    def div(self, other):
        if( other.r!=0.0 or other.i !=0.0):
            new=self.mult(other.conj(),)
            factor=other.abs()*other.abs()
            new_r = new.r/factor
            new_i = new.i/factor
            return my_complex(new_r, new_i)
        else:
            return my_complex(None, None)


x = my_complex(3.0, 4.0)
print("x = ",x.r,"+", x.i,"j")

y = my_complex(0.0, 2.0)
print("y = ",y.r,"+", y.i,"j\n")

con = x.conj()
print("sprzeżenie (x) = ",con.r,"+", con.i,"j")


print("moduł = |x| = ",x.abs()) #moduł

sum = x.add(y)
print("x + y = ",sum.r,"+",sum.i,"j")

sub = x.sub(y)
print("x - y = ",sub.r,"+",sub.i,"j")

mult = x.mult(y)
print("x * y = ",mult.r,"+",mult.i,"j")

div = x.div(y)
print("x / y = ",div.r,"+",div.i,"j")


