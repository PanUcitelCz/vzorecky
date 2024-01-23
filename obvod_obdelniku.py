#Přivítání uživatele
print("Vítejte v aplikaci pro výpočet obvodu obdelníku")

#Deklarace (spíše inicializace) proměných, následně do nich ukládáme vstup
a = input("Zadejte proměnou a: ")
b = input("Zadejte proměnou b: ")

#Přetypování z stringu na int
a = int(a)
b = int(b)

#Podmínka, kontrola zda v proměných není záporné číslo
if a>0 and b>0:
    #Deklarace proměné výsledek
    vysledek = 2*a+2*b
    #Output pro výsledek
    print("Výsledek je: ", vysledek)
#Pokud nebude platit první podmínka, provede se vždy else
else:
    #Dáváme uživateli vědět, že něco zadal asi špatně
    print("Tak jsi nadrbaný?")