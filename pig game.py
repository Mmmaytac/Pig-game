import random
def toplanan_xal():
    cem=0
    print('davam etmek ucun"y", bitirmek ucun "n" daxil edin')
    print('oyun basladi')
    while True:
        eded=random.randint(1,6)
        cem+=eded
        print(f'eded:{eded}, cem:{cem}')
        if cem<=51:
            print('siz davam ede ve ya oyunu bitire bilersiniz')
            secim = input('davam etmek isteyirsiz?: ')
            if secim == 'y':
                continue
            elif secim == 'n':
                print(f'son elde etdiyiniz netice={cem}')
                return  cem
                break
            else:
                print('siz duzgun secim etmediniz ve uduzdunuz!')
                return 'uduzdu'
                break
        else:
            print(f'son elde etdiyiniz netice={cem}')
            print('SIZ UDUZDUNUZ!')
            return 'uduzdu'
            break
y_dic={}
yarisci_sayi=int(input('nece nefer yarisir?: '))
for i in range(yarisci_sayi):
    yarisci_adi=input('adinizi daxil edin:')
    yarisci_bali=toplanan_xal()
    y_dic[yarisci_adi]=yarisci_bali
print(y_dic)
def qalibin_teyini():
    lst=list(y_dic.values())
    en_boyuk_xal=0
    for xal in lst:
        if xal!='uduzdu' and xal>en_boyuk_xal:
            en_boyuk_xal=xal
    return en_boyuk_xal
for ad in y_dic.keys():
    if y_dic[ad]==qalibin_teyini():
        print(f'oyunun qalibi {ad.upper()}!')
