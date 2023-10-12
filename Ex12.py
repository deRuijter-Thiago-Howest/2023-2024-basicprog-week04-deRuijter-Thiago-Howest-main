


# list_numbers1 = [4, 5, 6, 4]
# list_numbers2 = [89, 78, 4]


# Schrijf een functie ‘zijn_totaal_verschillend’ die 2 lists binnenkrijgt.
# De functie geeft False terug indien er minimum één gemeenschappelijk element gevonden wordt.
# True wordt pas teruggegeven als beide helemaal verschillend zijn
from typing import List

def zijn_totaal_verschillend(List1:List[int], List2:List[int]) -> int:
    aantal_elementen = []
    for element in List1:
        if element in List2:
            aantal_elementen.append(element)
            result = len(aantal_elementen)
        else:
            result = len(aantal_elementen)

       
    return result



list_getallen1 = [4, 5, 6, 4]
list_getallen2 = [89, 78, 4]
print(f"er zitten {zijn_totaal_verschillend(list_getallen1,list_getallen2)} gemeenschappelijke elementen in list1 en list2")