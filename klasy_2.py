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
        new_i = -self.i
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

while(1):
    print("wybierz jakie działanie chcesz wykonać:\n"
        "+ Dodawanie A + B\n"
        "- Odejmowanie A - B\n"
        "M Moduł |A|\n"
        "* Mnożenie A * B\n"
        "/ Dzielenie A / B\n"
        "S Sprzężenie A'\n"
        "Q Wyjdź\n")
    data=input("podaj znak: ")



    if (data=="+"):
        print("podaj liczbe A")
        realA = float(input("Realis A:"))
        imagA = float(input("Imaginalis A:"))
        A=my_complex(realA,imagA)
        print("A = ", A.r, "+", A.i, "j")

        print("podaj liczbe B")
        realB = float(input("Realis B:"))
        imagB = float(input("Imaginalis B:"))
        B=my_complex(realB, imagB)
        print("B = ", B.r, "+", B.i, "j")
        summ = A.add(B)
        print("\nA + B = ", summ.r, "+", summ.i, "j")

    if (data=="-"):
        print("podaj liczbe A")
        realA = float(input("Realis A:"))
        imagA = float(input("Imaginalis A:"))
        A=my_complex(realA,imagA)
        print("A = ", A.r, "+", A.i, "j")

        print("podaj liczbe B")
        realB = float(input("Realis B:"))
        imagB = float(input("Imaginalis B:"))
        B=my_complex(realB, imagB)
        print("B = ", B.r, "+", B.i, "j")
        substract = A.sub(B)
        print("\nA - B = ", substract.r, "+", substract.i, "j")

    if (data=="*"):
        print("podaj liczbe A")
        realA = float(input("Realis A:"))
        imagA = float(input("Imaginalis A:"))
        A=my_complex(realA,imagA)
        print("A = ", A.r, "+", A.i, "j")

        print("podaj liczbe B")
        realB = float(input("Realis B:"))
        imagB = float(input("Imaginalis B:"))
        B=my_complex(realB, imagB)
        print("B = ", B.r, "+", B.i, "j")

        multiplication = A.mult(B)
        print("\nA * B = ", multiplication.r, "+", multiplication.i, "j")

    if (data=="M"):
        print("podaj liczbe A")
        realA = float(input("Realis A:"))
        imagA = float(input("Imaginalis A:"))
        A=my_complex(realA,imagA)
        print("A = ", A.r, "+", A.i, "j")
        print("\n|A|=",A.abs())

    if (data=="S"):
        print("podaj liczbe A")
        realA = float(input("Realis A:"))
        imagA = float(input("Imaginalis A:"))
        A=my_complex(realA,imagA)
        print("A = ", A.r, "+", A.i, "j")
        conjugate=A.conj()
        print("\n A' =", conjugate.r, "+", conjugate.i, "j")

    if (data=="/"):
        print("podaj liczbe A")
        realA = float(input("Realis A:"))
        imagA = float(input("Imaginalis A:"))
        A=my_complex(realA,imagA)
        print("A = ", A.r, "+", A.i, "j")

        print("podaj liczbe B")
        realB = float(input("Realis B:"))
        imagB = float(input("Imaginalis B:"))
        B=my_complex(realB, imagB)
        print("B = ", B.r, "+", B.i, "j")

        divide = A.div(B)
        print("\nA / B = ", divide.r, "+", divide.i, "j")



    elif(data=="Q"):
        break

