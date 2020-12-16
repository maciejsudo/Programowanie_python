#Maciej Sudol 303073
#Elektronika AGH 3 rok


#  zadanie zrealizowane w formie ksiazki adresowej
#  imie nazwisko i rok urodzenia powinny byc podane w jednej linii
#  wcisnij q by wyjsc i wyswietlic listę

lines =list()
print('Wprowadz imię, nazwisko oraz datę urodzenia:')

line=input('podaj dane:')
while line !='q':
    lines.append(line)
    line = input('podaj dane:')
print("\n Lista wprowadzonych danych:")
print(*lines,sep ="\n")
