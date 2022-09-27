try:
    f=int(input("ENTER THE NUMBER OF FRESH LOAVES PURCHASED----> "))
    o=int(input("ENTER THE NUMBER OF DAY OLD LOAVES PURCHASED---->"))
    reg=185
    print("REGULAR PRICE---> ",reg)
    nl=185*f
    ol=(185*0.6)*0
    tot=nl+ol
    print("AMOUNT OF NEW LOAVES---> ",\"%02d"%(nl))
    print("AMOUNT OF DAY OLD LOAVES---> ",ol)
    print("TOTAL AMOUNT---> ",tot)
