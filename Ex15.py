# test = ["A", 89, 78, 4, "A", "test", 4]
# print(f"{test}\nZonder dubbels: {verwijder_dubbels(test)}")


# test = ["A", 89, 78, 4, "A", "test", 4]
# print(f"{test}\nWithout duplicates: {remove_duplicates(test)}")


# Schrijf een functie ‘verwijder_dubbels’ die een list als parameter heeft. Deze functie geeft een nieuwe
# list zonder duplicaten terug. Test uit door de beide lists af te printen.
from typing import List

def verwijder_dubbels(List:List) -> List:
    result = []
    #overloop de list: controleer of element al in result zit
    #zo niet, voeg toe aan list
    #indien wel: blijf eraf

    for element in List:
        if not element in result:
            result.append(element)
    return result


test = ["A", 89, 78, 4, "A", "test", 4]
print(f"{test}\nZonder dubbels: {verwijder_dubbels(test)}")

