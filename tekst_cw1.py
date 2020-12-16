#Maciej Sudol 303073
#Elektronika AGH 3 rok
#
#
#
path='wlasne_repozytorium_tekstowe.txt'

f = open(path,'r', encoding = 'utf-8')
delete_list = ['się',' i ','oraz','nigdy','dlaczego']
lst = []
for line in f:
    for word in delete_list:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open(path,'w', encoding = 'utf-8')
for line in lst:
    f.write(line)
f.close()

