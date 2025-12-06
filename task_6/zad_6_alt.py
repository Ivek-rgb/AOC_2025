import time

start = time.perf_counter() 

zadaca = open("test.txt","r")
zadaca_l = zadaca.readlines()
zadaca_n = [""]*len(zadaca_l)

zbroj_rez_zbr = 0
zbroj_rez_mno = 1
zbroj_rez_uk = 0
#print(len(zadaca_l))

for zadaca in range(len(zadaca_l) - 1):
    zadaca_l[zadaca] = zadaca_l[zadaca].rstrip("\n")
#print(zadaca_l)

zadaca_c = [""]*(len(zadaca_l[0]))

for zadaca in range(len(zadaca_c)):
    for i in range(len(zadaca_l) - 1):
        zadaca_c[zadaca] += zadaca_l[i][zadaca]


for zadaca in range(len(zadaca_c)):
    zadaca_c[zadaca] = zadaca_c[zadaca].rstrip()
    zadaca_c[zadaca] = zadaca_c[zadaca].strip()

for zadaca in range(len(zadaca_l[len(zadaca_l)-1])):
    zadaca_op = zadaca_l[len(zadaca_l)-1].split()

#print(zadaca_op)

#print(zadaca_c)

brojac_jed = 0

for index in range(len(zadaca_c)):
    if zadaca_c[index] != "":
        if zadaca_op[brojac_jed] == "*":
            zbroj_rez_mno *= int(zadaca_c[index])
        elif zadaca_op[brojac_jed] == "+":
            zbroj_rez_zbr += int(zadaca_c[index])
    else:
        if zadaca_op[brojac_jed] == "*":
            zbroj_rez_uk += zbroj_rez_mno
        elif zadaca_op[brojac_jed] == "+":
            zbroj_rez_uk += zbroj_rez_zbr
        brojac_jed += 1
        zbroj_rez_zbr = 0
        zbroj_rez_mno = 1

if zadaca_op[brojac_jed] == "*":
    zbroj_rez_uk += zbroj_rez_mno
elif zadaca_op[brojac_jed] == "+":
    zbroj_rez_uk += zbroj_rez_zbr
brojac_jed += 1

print("Ukupno: ", zbroj_rez_uk)

end = time.perf_counter() 
print(f"elapsed time {(end-start):.6f} seconds")
