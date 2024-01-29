#Přivítání uživatele
print("Vítejte v aplikaci pro výpočet vzorečků pro obdelník/kvádru")

#Cyklus s podmínkou, pokud je tam True, bude se opakovat pořád, dokud se nezmění ve False
while(True):
    #Dáváme vědětn uživateli, co může zadat a co se stane, když zadá tohle číslo
    print("Pro výpočet objemu zadejte 1.")
    print("Pro výpočet obvodu zadejte 2.")
    print("Pro výpočet obsahu zadejte 3.")
    print("Pro ukončení zadejte 4.")

    #Deklarujeme proměnou volba (spíše inicializujeme) a ukládáme do něj volbu, kterou zadal uživatel
    volba = input("Zadejte Vaši volbu: ")

    #Porovnáváme v podmínce, zda se uživatel do volby zadal 1, pokud ano, provede se výpočet objemu
    if volba == "1":
        #Pouze informuji uživatele, že si zvolil výpočet objemu a že hodnoty má zadávat v cm
        print("Zvolil jste si výpočet objemu, hodnoty zadávejte v cm")

        #Deklarace (spíše inicializace) proměných, následně do nich ukládáme vstup
        a = int(input("Zadejte stranu a: "))
        b = int(input("Zadejte stranu b: "))
        c = int(input("Zadejte stranu c: "))

        #Podmínka, kontrola zda v proměných není záporné číslo
        if a>0 and b>0 and c>0:
            #Deklarace (inicializace) proměné výsledek
            vysledek = a*b*c
            
            #Output pro výsledek
            #Všiměte si, jak čárkou oděluji string, int a znovu string
            print("Objem kvádru je: ", vysledek, " litrů")
        
        #Pokud nebude platit první podmínka, provede se vždy else
        else:
            print("Co to děláš kámo?")

    #Porovnáváme v podmínce, zda se uživatel do volby zadal 2, pokud ano, provede se výpočet obvodu
    elif volba == "2":
        #Pouze informuji uživatele, že si zvolil výpočet objemu a že hodnoty má zadávat v cm
        print("Pro výpočet obvodu zadávejte délku strany v cm")

        #Deklarace (spíše inicializace) proměných, následně do nich ukládáme vstup
        a = int(input("Zadejte stranu a: "))
        b = int(input("Zadejte stranu b: "))

        #Podmínka, kontrola zda v proměných není záporné číslo
        if a>0 and b>0:
            #Deklarace (inicializace) proměné výsledek
            vysledek = 2*a+2*b

            #Output pro výsledek
            #Všiměte si, jak čárkou oděluji string, int a znovu string
            print("Obvod kvádru je: ", vysledek, " cm")

        #Pokud nebude platit první podmínka, provede se vždy else
        else:
            print("Co to děláš kámo?")

    #Porovnáváme v podmínce, zda se uživatel do volby zadal 3, pokud ano, provede se výpočet obsahu
    elif volba == "3":
        #Pouze informuji uživatele, že si zvolil výpočet objemu a že hodnoty má zadávat v cm
        print("Pro výpočet obsahu zadávejte délku strany v cm")

        #Deklarace (spíše inicializace) proměných, následně do nich ukládáme vstup
        a = int(input("Zadejte stranu a: "))
        b = int(input("Zadejte stranu b: "))

        #Podmínka, kontrola zda v proměných není záporné číslo
        if a>0 and b>0:
            #Deklarace (inicializace) proměné výsledek
            vysledek = a*b

            #Output pro výsledek
            #Všiměte si, jak čárkou oděluji string, int a znovu string
            print("Obsah kvádru je: ", vysledek, "cm/2")

        #Pokud nebude platit první podmínka, provede se vždy else
        else:
            print("Co to děláš kámo?")

    #Pokud do volby uživatel zadal 4, provede se příkaz pro ukončení cyklusu a ukončí se program, protože po cyklusu algoritmus dál nepokračuje
    elif volba == "4":
        #Pouze informujeme, že program bude ukončen
        print("Ukončení programu")
        #Break pouze ukončí cyklus, to znamená že ve while se změní true na false a dále pokračovat nebude
        break
    
    #Dáváme uživateli vědět, že něco zadal asi špatně
    #Else se splní, pokud ani jedna z podmínek není pravdivá
    else:
        print("Zadal jsi něco asi špatně")


