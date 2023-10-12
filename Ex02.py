# Maak een lege list ‘nieuwe_list_getallen’ aan.
# Vul deze list op met getallen startend vanaf 1, met stapgrootte 13, tem 482.
# Doe nu het volgende:
# - Print de list af.
# - Print de list in omgekeerde volgorde af.
# - Verwijder het eerste element (waarde 482) en print opnieuw de list af.
# - Zoek de werkwijze om een specifiek element uit de list te verwijderen


#we starten met een lege list
nieuwe_list_getallen = []
#opvullen met getallen startend vanaf 1 , stapgrootte 13, tot 482
for getal in range(1,483, 13):
    nieuwe_list_getallen.append(getal)
print(nieuwe_list_getallen)

#print list in omgekeerde volgorde

nieuwe_list_getallen.reverse()
print("omgekeerde list")
print(nieuwe_list_getallen)

#verwijder het eerste element en print opnieuw de list af.
nieuwe_list_getallen.remove(482)
print(nieuwe_list_getallen)

#verwijder in de list een bepaald element op een doorgegeven positie
del(nieuwe_list_getallen[37]) 

