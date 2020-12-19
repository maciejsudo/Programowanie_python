#Maciej Sudol 303073
#Elektronika AGH 3 rok

#   CSV

import csv


while(1):

    print("\n  ----Notatnik (baza danych)----\n| A - Dodaj nowe zadanie \n| S - Pokaz listę zadan \n| D - usuń wybrany wpis \n| Q - Wyjdz ")
    #writer.writerow(["zadanie: kto ma wykonać?: data wykonania:"])
    # for row in writer:
    select = input("  --co chcesz zrobić, wpisz znak--:")

    if(select=='A'):
         with open('Notatnik.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            task = input("wpisz zadanie")
            who = input("wpisz kto ma wykonać zadanie")
            date = input("wpisz datę wykonania zadania")
            writer.writerow([task,who,date])
            #file.close()
    if(select=='S'):
        with open('Notatnik.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            print("\n|zadanie|kto ?|kiedy?|\n")

            x=0
            for row in reader:
                print(x,')',','.join(row))
                x+=1
    if(select=='D'):
        count=int(input("wskaż linię do usunięcia"))
        with open('Notatnik.csv', 'r', newline='') as file:
            lista=[]
            reader = csv.reader(file)
            for row in reader:
                lista.append(row)
        with open('Notatnik.csv', 'w', newline='') as file:
            reader = csv.reader(file)
            del lista[count-1]
            writer = csv.writer(file)
            writer.writerows(lista)
    if(select=='Q'):
        break




