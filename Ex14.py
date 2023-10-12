# list1 = [78, 4, 5, 6, 4]
# list2 = [89, 78, 4]
# list3 = ['Tamara', 'Delfien', 'Elke', 'Marijn']
# list4 = ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']

# Schrijf een functie ‘geef_gemeenschappelijke_elementen’ die 2 lists binnenkrijgt.
# De functie bepaalt de gemeenschappelijke elementen en geeft deze als een nieuwe list terug. Zorg
# ervoor dat er in de laatste list geen dubbels voorkomen. Zorg ook dat deze gesorteerd is. Print
# vervolgens alles af.
# Test uit op twee lists van getallen en op twee lists van woorden.
from typing import List

def geef_gemeenschappelijke_elementen(List1:list,List2:list) -> List:
    result = []
    #overloop de eerste list
    for element in List1:
        #kijk of dit element in de tweede list zit
        if element in List2:
            #bingo --> toevoegen aan list
            #controle of ik het element nog niet heb (ik wil geen dubbels)
            if not element in result:
                result.append(element)
    return result





list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4]
print(f"De gemeenschappelijke elementen: {geef_gemeenschappelijke_elementen(list1,list2)}")




list3 = ['Tamara', 'Delfien', 'Elke', 'Marijn']
list4 = ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']
print(f"De gemeenschappelijke elementen: {geef_gemeenschappelijke_elementen(list3,list4)}")