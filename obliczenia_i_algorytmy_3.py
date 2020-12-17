#Maciej Sudol 303073
#Elektronika AGH 3 rok

def scalar_prod(a,b):
    result =0
    if(len(a)!=len(b)):
        print("wektory nie są równych wymiarów!")

    else:
        for i in range(len(a)):
            result += a[i]*b[i]
        return result

   # else:
   # print("wektory są różnych wymiarów")

lengtha = int(input("podaj rozmiar wektora a"))
a=[]
for x in range(0,lengtha):
    val=float(input("podaj wartosc"))
    a.append(val)
print("a = ",a)


lengthb = int(input("podaj rozmiar wektora b"))
b=[]
for x in range(0,lengthb):
    val=float(input("podaj wartosc"))
    b.append(val)
print("b = ",b)

#iloczyn skalarny:
print("iloczyn skalarny a o b =",scalar_prod(a,b))