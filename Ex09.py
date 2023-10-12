
# Schrijf een functie ‘max_en_min_uit_list’ met als parameter een list. Deze functie zoekt uit de list het
# maximum en minimum op en geeft deze samen in een string terug. Test deze functie uit op een list met
# getallen en een list met woorden.
# Uit [11, 52, 125, -89, 1245] is het max: 1245 en min: -89
# Uit ['jan', 'feb', 'maa', 'apr', 'mei'] is het max: mei en min: apr
from typing import List

# def max_en_min_uit_list(element_list:List) -> object:
#     max = max(element_list)
#     min = min(element_list)
#     Max_en_Min = max += min
#     return max 


#min en max van woorden is alfabetische volgorde



def max_en_min_uit_list(element_list:List) -> object:
    info = ""
    info += f"Min uit de lijst: {min(element_list)}\n"
    info += f"Max uit de lijst: {max(element_list)}"
    return info






lijst_getallen = [11, 52, 125, -89, 1245]
lijst_woorden = ["jan", "feb", "maa", "apr", "mei"]

print(f"Demo op {lijst_getallen}:\n {max_en_min_uit_list(lijst_getallen)}")
print(f"Demo op {lijst_woorden}:\n {max_en_min_uit_list(lijst_woorden)}")
