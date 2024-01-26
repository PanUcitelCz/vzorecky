while True:

    print("Vítejte v aplikaci pro výpočet vzorečků pro obdelník/kvádru")

    print("Pro výpočet objemu zadejte 1.")
    print("Pro výpočet obvodu zadejte 2.")
    print("Pro výpočet obsahu zadejte 3.")
    print("Pro ukončení zadejte 4.")

    volba = input("Zadejte Vaši volbu: ")

    if volba == "1":
        print("Zadávejte v dm")
        a = int(input("Zadejte stranu a: "))
        b = int(input("Zadejte stranu b: "))
        c = int(input("Zadejte stranu c: "))

        if a>0 and b>0 and c>0:
            vysledek = a*b*c
            print("Objem kvádru je: ", vysledek, " litrů")
        else:
            print("Co to děláš kámo?")

    elif volba == "2":
        print("Pro výpočet obvodu zadávejte délku strany v cm")
        a = int(input("Zadejte stranu a: "))
        b = int(input("Zadejte stranu b: "))

        if a>0 and b>0:
            vysledek = 2*a+2*b
            print("Obvod kvádru je: ", vysledek, " cm")
        else:
            print("Co to děláš kámo?")

    elif volba == "3":
        print("Pro výpočet obsahu zadávejte délku strany v cm")
        a = int(input("Zadejte stranu a: "))
        b = int(input("Zadejte stranu b: "))

        if a>0 and b>0:
            vysledek = a*b
            print("Obsah kvádru je: ", vysledek, "cm/2")
        else:
            print("Co to děláš kámo?")

    elif volba == "4":
        print("Ukončení programu")
        break
    
    else:
        print("Zadal jsi něco asi špatně")


