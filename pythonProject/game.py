from random import randint

los = randint(1,100)
odp = 0
ilosc = 0



while  odp != los :
    ilosc += 1
    odp = int(input("Podaj kolejną liczbę: "))
    if odp > los:
        print("Szukana liczba jest mniejsza od podanej.")
    elif odp < los :
        print("Szukana liczba jest większa od podanej. ")
print(f"Wylosowana liczba to {los} zgadłeś ją za {ilosc} razem. ")