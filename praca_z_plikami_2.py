# Maciej Sudol 303073
# Elektronika AGH 3 rok
#   skrypt zliczający ilosc plików w katalogu /dev
#   funkcja rekurencyjna przechodzi po kazdym katalogu wewnatrz \dev
#   jezeli jakis katalog zawiera katalogi to funkcja tam wchodzi
#   jezeli natrafia na plik (nie katalog) to tylko wyswietla jego nazwę
import os

path = 'C:/Users/ASUS/Desktop/python_uczelnia/Programowanie_python/dev'


def drzewo_katalog(path):
    if (os.path.isdir(path)):
        list = os.listdir(path)
        ilosc = len(list)
        if (ilosc != 0):
            print('\nIlosc plikow w folderze: \n', path, '\nwynosi ', ilosc, ' :')
            print(*list, sep="\n")
            for i in range(0, ilosc):
                new_path = path + '/' + list[i]
                drzewo_katalog(new_path)

drzewo_katalog(path)