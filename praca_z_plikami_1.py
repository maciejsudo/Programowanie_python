#Maciej Sudol 303073
#Elektronika AGH 3 rok
#   skrypt zliczający ilosc plików w katalogu /dev
import os

path ='C:/Users/ASUS/Desktop/python_uczelnia/Programowanie_python/dev'

list = os.listdir(path)
ilosc = len(list)
print('Ilość plików w katalogu wynosi: ',ilosc)