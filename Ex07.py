# Maak volgende lists aan:
# - Een list met 4 gehele getallen
# - Een list met 5 decimale getallen
# - Een list met 3 strings
# Maak nu één functie ‘geef_info_list’ die een string teruggeeft bestaande uit:
# - De naam van de list
# - Elk element met zijn index
# Roep deze functie voor de verschillende lists op


# collection1 = [12, 45, -9, -15]
# collection2 = [12.23, 45.1, 9.478, 15.125, -3.14]
# collection3 = ["Joerie", "Marie", "Henk", "Stijn"]

from typing import List

gehele_getallen = [0,3,4,9]
decimale_getallen = [2.5, 3.8, 4.6,10.9, 6.4]
strings = ["appel", "peer", "appelsien"]


#deze functie geeft tekst (string) terug: 
# def geef_info_list(naam_list:str, list_elementen: List) -> str:
    
#     info = ""
#     info += f"De naam van de list in {naam_list}\n"
#     info += f"De list is {list_elementen}"
#     return info




#tweede versie
def geef_info_list(naam_list:str, list_elementen: List) -> str:
    
    info = ""
    info += f"De naam van de list in {naam_list}\n"
    teller = 0
    for element in list_elementen:
        info += f"{element} zit op positie {teller}\n"
        teller += 1
    return info

def geef_info_list(naam_list:str, list_elementen: List) -> str:
    
    info = ""
    info += f"De naam van de list in {naam_list}\n"
    for element in list_elementen:
        info += f"{element} zit op positie {list_elementen.index(element)}\n"
    return info

print(geef_info_list("gehele getallen",gehele_getallen))
print(geef_info_list("decimale getallen",decimale_getallen))
print(geef_info_list("strings",strings))

#als index niets vindt geeft hij -1 terug
