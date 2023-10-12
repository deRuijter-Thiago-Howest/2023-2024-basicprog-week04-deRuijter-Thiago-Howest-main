# getal1 = int(input("Geef het minimum op:> "))
# getal2 = int(input("Geef het maximum op:> "))
# print(f"De vijf geselecteerde getallen hiertussen zijn: {kies_5_getallen(getal1, getal2)}")

# number1 = int(input("Enter the minimum:> "))
# number2 = int(input("Enter the maximum:> "))
# print(f"The five selected numbers in between are: {choose_5_numbers(number1, number2)}")

# Schrijf een functie ‘kies_5_getallen’ die twee waarden (min en max) als parameter binnenkrijgt. De
# functie kiest 5 unieke getallen uit het interval [min, max], voegt deze toe aan een list en geeft
# uiteindelijk deze list terug.
# Opgelet: er mogen geen dubbels in de teruggegeven lijst voorkomen.
# Test voldoende uit
from typing import List
from random import randint
 
def kies_5_getallen(min:int,max:int) -> List:
    result = []
    #zolang er geen 5 elementen in de lijst zitten
    while len(result) != 5:
        #kies een getal tussen min en max, en voeg het toe aan de list
        getal = randint(min,max)
        #ik wil geen dubbels:
        if not getal in result:
             result.append(getal)

    return result




minimum = int(input("Geef het minimum op:> "))
maximum = int(input("Geef het maximum op:> "))
print(f"De vijf geselecteerde getallen hiertussen zijn: {kies_5_getallen(minimum,maximum)}")