#Maciej Sudol 303073
#Elektronika AGH 3 rok
#
#
#
path='wlasne_repozytorium_tekstowe.txt'

f = open(path,'r', encoding = 'utf-8')


change={
    " i ": " oraz ",
    " oraz ": " i ",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu"
}


lst = []
for line in f:
    for first in change:
        if first in line:
            line = line.replace(first,change[first])
    lst.append(line)
f.close()
f = open(path,'w', encoding = 'utf-8')
for line in lst:
    f.write(line)
f.close()
