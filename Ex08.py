# maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober","november", "decemeber"]
# getallen = [100, 200, 300, 400]

# months= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# numbers = [100, 200, 300, 400]

# Maak een functie ‘kies_element’ aan met als parameter een list. De functie kiest een willekeurig
# element uit de doorgegeven list en geeft deze terug. Test deze functie met
# - Een list met strings, nl. de verschillende maanden
# - Een list met getallen
# Tip: Gebruik de documentatie van de module Random en zoek hoe je een willekeurige waarde uit een
# list kan opvragen. (Onder welke “groep” binnen de Data Types valt een list volgens de theorieles (zie
# schema))
# Print telkens het gekozen element af
from typing import List
import random

#deze functie kiest een element uit de doorgegeven list
#dat kan een getal, woord, datum, ... zijn
#we schrijven daarom achteraan 'object'

def kies_element(list_elementen:List) -> object:
    #de methode random.choice kiest een element uit de list
    random_element = random.choice(list_elementen)
    return random_element


maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober","november", "decemeber"]
getallen = [100, 200, 300, 400]
print(f"Uit de list {maanden} werd {kies_element(maanden)} gekozen")
print(f"Uit de list {getallen} werd {kies_element(getallen)} gekozen")