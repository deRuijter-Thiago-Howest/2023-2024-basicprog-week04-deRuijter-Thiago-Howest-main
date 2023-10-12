
# Schrijf een functie ‘tel_elementen_binnen_interval’ met drie parameters: een list, een minimum en een
# maximum. De functie telt hoeveel elementen uit de list binnen het interval [min, max] vallen en geeft
# dat aantal terug.


# from typing import List
# def tel_elementen_binnen_interval(List:List, min:int, max:int) -> int:
#     nieuwe_list = []
#     for element in range(min,max):
#         nieuwe_list.append(element)
#         result = len(nieuwe_list)
#     return result





# list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
# list2 = ['a', 'b', 'c', 'd', 'e', 'f']

# min = int(input("Geef hier een minimum op: "))
# max = int(input("Geef hier een maximum op: "))

# print(f"{tel_elementen_binnen_interval(list1,min,max)} elementen vallen binnen de gegeven interval")


from typing import List
from typing import Union
def tel_elementen_binnen_interval(List:List, min:Union[str,int], max:Union[str,int]) -> int:
    
    teller = 0
    for element in List:
        if min <= element <= max:
            teller += 1

    return teller

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']


type = str(input("is het een getallenlijst: 'G' of een letterslijst: 'L'  :> "))

if type == 'G':

    min = int(input("Geef hier een minimum op: "))
    max = int(input("Geef hier een maximum op: "))

    print(f"{tel_elementen_binnen_interval(list1,min,max)} elementen vallen binnen de gegeven interval")
elif type == 'C':

    min = str(input("Geef hier een minimum op: "))
    max = str(input("Geef hier een maximum op: "))
    print(f"{tel_elementen_binnen_interval(list1,min,max)} elementen vallen binnen de gegeven interval")
else:
    print("foutieve input")