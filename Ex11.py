# lijst_getallen = [12, 45, 465, 78, 1, 23, 89]
# lege_lijst_getallen = []


# list_numbers = [12, 45, 465, 78, 1, 23, 89]
# empty_list = []


# Schrijf een functie ‘gemiddelde _in_list’ met als parameter een list van getallen die het gemiddelde van
# de getallen teruggeeft.
# getallen = [12, 45, 465, 78, 1, 23, 89]
# lege_lijst_getallen = []
from typing import List




#lange manier
def gemiddelde_in_lijst(getallen_lijst:List[int]) -> float:
    if len(getallen_lijst) != 0:
        gem = sum(getallen_lijst) / len(getallen_lijst)
        return gem
    else:
        print("Foutmelding in de functie: lege list!")
        return None         # --> we geven voorlopig niets terug






getallen = [12, 45, 465, 78, 1, 23, 89]
lege_lijst_getallen = []

print(f"De gemiddelde van eerste Lijst is: {gemiddelde_in_lijst(getallen):.2f}")
print(f"De gemiddelde van tweede Lijst is: {gemiddelde_in_lijst(lege_lijst_getallen)}")