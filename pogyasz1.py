from Csomag import Csomag
csomaglista = []
def feldolgoz():
    f = open('csomag.txt','r', encoding='utf-8')
    f.readline().strip()
    sorok = f.readlines()
    f.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("#")
        csomaglista.append(Csomag(sor))
        i += 1
def szam():
    print('III/A, B: ')
    print(f'\tA pogyászok száma: {len(csomaglista)}')

def atlag():
    i = 0
    ossz= 0
    db = 1
    while i < len(csomaglista):
        if csomaglista[i].szelesseg == 51:
            ossz += csomaglista[i].suly
            db += 1
        i += 1
    atl = int(float((ossz)/db)*1000)
    print('III/C:')
    print(f'\tAz 51 cm-es pogyászok átlag súlyértéke: {atl} g')

def magas():
    max = 0
    i = 1
    index = 0
    while i < len(csomaglista):
        if csomaglista[i].magassag > max:
            max = csomaglista[i].magassag
            index = i
        i += 1
    print('III/D:')
    print(f'\tA legmagasabb pogyász méretei: {csomaglista[index].szelesseg}X{csomaglista[index].magassag}X{csomaglista[index].melyseg}, súlya: {csomaglista[index].suly} kg')
