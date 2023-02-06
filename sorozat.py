import random

vellista = []

def sor():
    i = 0
    j = 0
    while i < 12:
       vel = random.randint(-10,1000)
       vellista.append(vel)
       i += 1
    #print(vellista)
    kimenet =""
    while j < len(vellista):
        if j == len(vellista)-1:
            kimenet += str(vellista[j])
        else:
            kimenet += str(vellista[j]) + "$"
        j += 1
    print('II/A, B, C:')
    print(f'\t{kimenet}')

def paratlanok_szama():
    i = 0
    db = 0
    while i < len(vellista):
        if vellista[i] % 2 != 0:
            db += 1
        i += 1
    return db

def konzol_kiir():
    print('II/D, E: ')
    print(f'\tA páratlanok száma: {paratlanok_szama()}.')

def fajlba_kiir():
    f = open('eredmeny.txt','w',encoding='utf-8')
    f.write('II/F:')
    f.write(f'\n\tA páratlanok száma: {paratlanok_szama()}.')
    f.close()
