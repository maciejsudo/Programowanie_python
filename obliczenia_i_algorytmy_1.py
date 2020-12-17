#Maciej Sudol 303073
#Elektronika AGH 3 rok
import math as m
def quad_equ(a,b,c):
    delta = b*b -4*a*c
    if(delta==0):
        print("funkcja ma jedno miejsce zerowe x=",-b/(2*a))
    if(delta<0):
        print("funkcja ma ujemną deltę - pierwiastki urojone")
    elif (delta>0):
        print("funkcja posiada 2 pierwiastki:\n x1 = ",(-b-m.sqrt(delta))/(2*a),"\n x2 =",(-b+m.sqrt(delta))/(2*a))



print("podaj współczynniki równania kwadratowego:")

a=float(input("\nwspolczynnik a:"))
b=float(input("\nwspolczynnik b:"))
c=float(input("\nwspolczynnik c:"))

quad_equ(a,b,c)