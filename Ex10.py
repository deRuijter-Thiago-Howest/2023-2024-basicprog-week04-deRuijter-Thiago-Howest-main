# lijst_getallen = [5, 6, 9, 5 , 6]

# list_numbers = [5, 6, 9, 5 , 6]


# Schrijf een functie ‘som_in_list’ met als parameter een list van getallen die de totale som van de list
# getallen teruggeeft.
# - Pas eerst de techniek van vorige week toe.
# - Zoek nadien even op of er geen ingebouwde functie bestaat om de som te berekenen van de
# inhoud van een list.
from typing import List

def som_in_list(list_getallen:List[int]) -> int:
    som = sum(list_getallen)
    return som

#optie 2
def som_in_list(list_getallen:List[int]) -> int:
    som = 0
    for getal in list_getallen:
        som += getal
    return som






lijst_getallen = [5, 6, 9, 5 , 6]

print(f"De totale som van lijst getallen is : {som_in_list(lijst_getallen)}")
