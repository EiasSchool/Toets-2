#vraag 1
vraag1 = input('Beschik jij over een geldig vrachtwagenrijbewijs? Y/N\n').upper()

if vraag1 == 'Y':
    vrachtwagenrijbewijs = True
elif vraag1 == 'N':
    vrachtwagenrijbewijs = False
else:
    print('Je moet kiezen tussen J/N')

#vraag 2
vraag2 = input('Bent u in het bezit van een hoge hoed? Y/N\n').upper()

if vraag2 == 'Y':
    hogehoed = True
elif vraag2 == 'N':
    hogehoed = False
else:
    print('Je moet kiezen tussen J/N')

# vraag 3
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

#ervaring vragen (vraag 4, 5, 6)
vraag4 = input('Heeft u praktische ervaring met dressuur voor dieren? Y/N\n').upper()

if vraag4 == 'Y':
    vraag4ervaring = int(input('Hoeveel jaar praktijkervaring heeft u met dressuur voor dieren?\n'))
    if vraag4ervaring >= 4:
        dressuurervaring = True
else:
    dressuurervaring = False

vraag5 = input('Heb je ervaring met jongleren?\n').upper()

if vraag5 == 'Y':
    vraag5ervaring = int(input('Hoeveel jaar ervaring heeft u met jongleren?\n'))
    if vraag5ervaring >= 5:
        jonglerenervaring = True
else:
    jonglerenervaring = False

vraag6 = input('Heb je praktische ervaring met acrobatiek?\n').upper()

if vraag6 == 'Y':
    vraag6ervaring = int(input('Hoeveel jaar praktijkervaring heeft u in acrobatiek?\n'))
    if vraag6ervaring > 3:
        acrobatiekervaring = True
else:
    acrobatiekervaring = False

#vraag 7
vraag7 = int(input('Wat is uw geslacht 1)man 2)vrouw 3)anders\n'))

extracriteriacheck = False

while True:
    try:
        if vraag7 == 1:
            snorvraag = input('Heeft u een snor? Y/N\n').upper()
            if snorvraag == 'Y':
                extracriteriacheck = True
            break
        elif vraag7 == 2:
            haarvraag = input('Heeft u rood krulhaar? Y/N\n').upper()
            if haarvraag == 'Y':
                extracriteriacheck = True
            break
        elif vraag7 == 3:
            glimlachvraag = input('Heeft u een brede glimlach? Y/N\n').upper()
            if glimlachvraag == 'Y':
                extracriteriacheck = True
            break
    except ValueError:
        print('type een nummer')

#check voor de ervaring
ervaring = dressuurervaring or jonglerenervaring or acrobatiekervaring

#check if aangenomen of niet
if vrachtwagenrijbewijs and hogehoed and lichaamsgewicht and ervaring and extracriteriacheck:
    print('Gefeliciteerd u bent aangenomen') 
else:
    print('Helaas u bent niet aangenomen')

#print waarom
if not vrachtwagenrijbewijs:
    print('U heeft geen rijbewijs')
if not hogehoed:
    print('U heeft geen hoge hoed')
if not lichaamsgewicht:
    print('U lichaamsgewitch is niet tussen de 90 en 120kg')
if not ervaring:
    print('U heeft niet genoeg ervaring')
if not extracriteriacheck:
    print('U heeft geen aanvullende criteria die wij nodig hebben')