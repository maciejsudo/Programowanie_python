#Maciej Sudol 303073
#Elektronika AGH 3 rok
#   skrypt do konwersji rozszerzeń plików *.jpg na *.png
#   na początku funkcja zwroc pliki dostaje sie do folderu z plikami jpg
#   nastepnie z udzialem nowej sciezki wywoływana jest funkcja jpg2png
#   na koniec dla porownania wyswietlana jest zawartosc katalogu dev
from PIL import Image
import os

path='C:/Users/ASUS/Desktop/python_uczelnia/Programowanie_python/zad3_png_vs_jpg'

def jpg2png(path):
    if path[len(path)-3:len(path)] =='jpg':
        im = Image.open(path)
        path2 = path[0:len(path)-3] + 'png'
        im.save(path2)
    else:
        print("konwersja sie nie powiodla")


def zwroc_pliki(path):
    list=os.listdir(path)
    ilosc = len(list)
    if(ilosc!=0 ):
        print('\nPostac plikow w katalogu: \n',path,'\nprzed konwersją:')
        for i in range(0, ilosc):
            new_path = path + '/' + list[i]
            print(list[i])
            jpg2png(new_path)


#   wywołanie funkcji
zwroc_pliki(path)
#   sprawdzenie plików po konwersji:
print("\nPliki wewnątrz katalogu dev po konwersji:")
list=os.listdir(path)
print( *list, sep = "\n")
