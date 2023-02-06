

def ertek():
    nev = input('Étel neve:')
    rendelo = input('Étel rendelőjének neve:')
    ert = int(input('Értékelés (1-5): '))
    print('I/A, B:')
    print(f'Étel neve: {nev}')
    print(f'Étel rendelőjének neve: {rendelo}')
    print('I/C:')

    if ert <= 0 :
        print('Az értékelés nem lehet negatív vagy nulla!')
    elif ert > 5:
        print('5 pont feletti értékelés nem elfogadható!')
    else:
        print('Köszönjük az értékelést!')


