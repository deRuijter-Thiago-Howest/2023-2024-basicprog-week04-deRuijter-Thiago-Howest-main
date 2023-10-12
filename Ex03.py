# Maak een lege list ‘vrienden’ aan.
# We laten de applicatie deze list dynamisch uitbreiden. Telkens wordt aan de gebruiker gevraagd om een
# nieuwe naam op te geven of een lege string. In dat laatste geval stopt de applicatie door de lijst met
# vrienden af te printen.
# Voorbeeld van uitvoering:
# input("Geef de naam van een vriend op, of sluit af met een leeg veld:> ")

# input("Enter a friend's name, or exit with an empty field:> ")


list_vrienden = []

#opvullen van list, we maken gebruik van de while-lus -> zolang gebruiker blijft namen opgeven, doen we verder
input1 = input("Geef de naam van een vriend op, of sluit af met een leeg veld:> ")
while input1 != "":
    #vriend aan de list toevoegen
    list_vrienden.append(input1)
    #nieuwe vriend opvragen
    input1 = input("Geef de naam van een vriend op, of sluit af met een leeg veld:> ")

print(f"uw vrienden zijn: {list_vrienden}")



