vraag1 = input('Beschik jij over een geldig vrachtwagenrijbewijs? Y/N\n').upper()

if vraag1 == 'Y':
    vrachtwagenrijbewijs = True
elif vraag1 == 'N':
    vrachtwagenrijbewijs = False
else:
    print('Je moet kiezen tussen J/N')

vraag2 = input('Bent u in het bezit van een hoge hoed? Y/N\n').upper()

if vraag2 == 'Y':
    hogehoed = True
elif vraag2 == 'N':
    hogehoed = False
else:
    print('Je moet kiezen tussen J/N')

while True:
    try: 
        vraag3 = int(input('Wat is uw lichaamsgewicht in kg?\n'))
        if vraag3 >= 90 and vraag3 <= 120:
            lichaamsgewicht = True
            break
        else:
            lichaamsgewicht = False
            break
    except ValueError:
        print('typ een nummer')

#ervaring vragen
vraag4 = input('Heeft u praktische ervaring met dressuur voor dieren? Y/N\n').upper()

if vraag4 == 'Y':
    vraag4ervaring = int(input('Hoeveel jaar praktijkervaring heeft u met dressuur voor dieren?'))
    if vraag4ervaring >= 4:
        dressuurervaring = True
else:
    dressuurervaring = False

vraag5 = input('Heb je ervaring met jongleren?\n').upper()

if vraag5 == 'Y':
    vraag5ervaring = int(input('Hoeveel jaar ervaring heeft u met jongleren?'))
    if vraag5ervaring >= 5:
        jonglerenervaring = True
else:
    jonglerenervaring = False

vraag6 = input('Heb je praktische ervaring met acrobatiek?\n').upper()

if vraag6 == 'Y':
    vraag6ervaring = int(input('Hoeveel jaar praktijkervaring heeft u in acrobatiek?'))
    if vraag6ervaring > 3:
        acrobatiekervaring = True
else:
    acrobatiekervaring = False

ervaring = dressuurervaring or jonglerenervaring or acrobatiekervaring

if vrachtwagenrijbewijs and hogehoed and lichaamsgewicht and ervaring:
    print('Gefeliciteerd u bent aangenomen') 
else:
    print('Helaas u bent niet aangenomen')