Namirnice = open("test.txt","r")
Namirnice_l = Namirnice.readlines()
for i in range(0,len(Namirnice_l)):
    Namirnice_l[i] = Namirnice_l[i].rstrip("\n")
prijelom = Namirnice_l.index('')

print(Namirnice_l)
print(prijelom)

Svjeze = Namirnice_l[:prijelom]
Dostupne = Namirnice_l[prijelom+1:]
Dostupne_provjera = [False]*len(Dostupne)

print(Svjeze)
print(Dostupne)
print(Dostupne_provjera)

for i in range(0,len(Svjeze)):
    povlaka_index = Svjeze[i].find('-')
    svjeze_donja = int(Svjeze[i][:povlaka_index])
    svjeze_gornja = int(Svjeze[i][povlaka_index+1:])
    print(svjeze_donja)
    print(svjeze_gornja)
    for j in range(0,len(Dostupne_provjera)):
        dostupna = int(Dostupne[j])
        if svjeze_donja <= dostupna <= svjeze_gornja:
            Dostupne_provjera[j] = True

print(Dostupne_provjera)
zbroj_dostupnih = 0

for i in range(0,len(Dostupne_provjera)):
    if Dostupne_provjera[i]:
        zbroj_dostupnih += 1

print(zbroj_dostupnih)