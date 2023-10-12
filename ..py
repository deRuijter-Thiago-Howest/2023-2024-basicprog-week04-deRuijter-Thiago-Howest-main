from typing import List, Union

def tel_elementen_binnen_interval(input_list: List[Union[int, float, str]], minimum, maximum) -> int:
    count = 0
    for element in input_list:
        if minimum <= element <= maximum:
            count += 1
    return count

list2 = ['a', 'b', 'c', 'd', 'e', 'f']
min_value = 'c'  # Minimumwaarde (str)
max_value = 'e'  # Maximumwaarde (str)



print(f"Aantal elementen in de lijst binnen het interval: {tel_elementen_binnen_interval(list2,min_value,max_value)}")