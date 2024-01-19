#Uživitale přivítáme v aplikaci
print("Vítejte v aplikaci pro výpočet obvodu obdelníku")

#Deklarace proměných (spíše inicializace)
a = input("Zadejte délku strany a: ")
b = input("Zadejte délku strany b: ")

#Přetypování na int
a = int(a)
b = int(b)

#Kontrolujeme zda uživatel nezadal záporné číslo
if a>0 and b>0:
    print("Výsledek je: ")
    print(2*a+2*b)

#Pokud nebude platit první podmínka, splníse else
else:
    print("Co pak to děláš? Všakj jsi zadal záporná čísla")