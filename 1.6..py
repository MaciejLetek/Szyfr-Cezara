"""#sprawdzanie możliwości boków trójkąta
import math
print('wlasnosci trojkata o podanych wymiarach: ')
def trojkat(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        print('- MOZE ISTNIEC')
        if a**2+b**2 == c**2:
            print('- TROJKAT JEST PROSTOKATNY')
            print('- POLE =', a*b/2)
        elif c**2+b**2 == a**2:
            print('- TROJKAT JEST PROSTOKATNY')
            print('- POLE =', c*b/2)
        elif a**2+c**2 == b**2:
            print('- TROJKAT JEST PROSTOKATNY')
            print('- POLE =', a*c/2)
        else:
            print('- TROJKAT NIE JEST PROSTOKATNY')
            p = 0.5*(a+b+c) #pole liczymy na podstawie wzoru Herona
            pole = (p*(p-a)*(p-b)*(p-c))**0.5
            print('- POLE =', round(pole,4))
        print('- OBWOD =', a + b + c)
    else:
        print('TAKI TROJKAT NIE MOZE ISTNIEC')
        wybor = int(input('chcesz sprobowac jeszcze raz?\n TAK = 1\tNIE = 0\n'))
        if wybor == 1:
            print('OK, sprobujmy jeszcze raz!')
            a = int(input('podaj 1 bok: '))
            b = int(input('podaj 2 bok: '))
            c = int(input('podaj 3 bok: '))
            trojkat(a,b,c)
        else: print('OK, milo bylo :)')

a = int(input('podaj 1 bok: '))
b = int(input('podaj 2 bok: '))
c = int(input('podaj 3 bok: '))
trojkat(a,b,c)"""

#szyfr cezara
w = ''
z = 'zupka'
for i in range(len(z)):
    w += chr(ord(z[i])-3)

print(w)

def szyfr_cezara(klucz,haslo):
    szyfrogram = ""
    nowe = haslo.upper()
    for i in range(len(haslo)):
        if nowe[i].isalpha():
            if ord(nowe[i])+klucz > 90:
                szyfrogram += chr(ord(nowe[i])+klucz-25)
            else:
                szyfrogram += chr(ord(nowe[i])+klucz)
        else: szyfrogram += " "
    return szyfrogram


def deszyfruj(klucz,szyfrogram):
    deszyfrogram = ""
    for i in range(len(szyfrogram)):
        if szyfrogram[i].isalpha():
            if ord(szyfrogram[i])-klucz < 65:
                deszyfrogram += chr(ord(szyfrogram[i])-klucz+25)
            else:
                deszyfrogram += chr(ord(szyfrogram[i])-klucz)
        else: deszyfrogram += " "
    return deszyfrogram

klucz = int(input('podaj klucz: '))
haslo = input('podaj haslo: ')
szyfrogram = szyfr_cezara(klucz,haslo)
print('zaszyfrowana wiadomosc: ', szyfrogram)
print("Odszyfrowana wiadomosc ", deszyfruj(klucz,szyfrogram))



