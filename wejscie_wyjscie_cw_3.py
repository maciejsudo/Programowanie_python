#Maciej Sudol 303073
#Elektronika AGH 3 rok



x=input('Ustaw kod otwierający zamek szyfrowy:\n ')

y=input('Podaj kod zeby otworzyc zamek:\n ')
while(x!=y):
    y=input(' BŁĘDNY KOD!!! podaj kod ponownie:\n ')
print('podano własciwy kod - zamek został otwarty')


