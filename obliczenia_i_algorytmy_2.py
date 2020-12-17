#Maciej Sudol 303073
#Elektronika AGH 3 rok
import random

randomlist = []
for i in range(0,50):
    n= random.randint(1,1000)
    randomlist.append(n)

print("liczba wylosowanych liczb: ",len(randomlist))
print("liczby nie posortowane: ",randomlist)





def bubble_sort(a):
    for i in range (len(a)-1):
        for j in range(len(a)-i-1):
            if(a[j]<a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

    return a

print()


#weryfikacja wbudowaną funkcją:

sorted_manually = bubble_sort(randomlist)
print("posortowane funkcją bubble_sort: \n",sorted_manually)
randomlist.sort(reverse=True)
print("posortowane funkcją wbudowaną: \n",randomlist)



if sorted_manually==randomlist:
    print("listy są identyczne")
else:
    print("algorytm sortowania bąbelkowego nie zadziałał")