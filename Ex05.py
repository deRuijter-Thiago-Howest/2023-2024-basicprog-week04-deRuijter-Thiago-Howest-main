# Maak één list aan met de dagen van de week. Gebruik het printcommando (in één codelijn!) om
# volgende output af te printen:
# - Enkel de werkdagen van de week
# - De weekenddagen van de week
# - De onpare dagen van de week
# - De pare dagen van de week
# Tip: welke techniek zagen we vorige week om een deel uit een string op te halen?




# weekdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saterday","Sunday"] 



weekdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saterday","Sunday"]
#Let op: startpositie, eindpositie (element op eindpositie wordt niet meegenomen)
print(f"De werkdagen zijn: {weekdagen[0:5]}")
print(f"De weekenddagen zijn: {weekdagen[5:7]}")
#De pare dagen = dagen op even posities
#gebruik hier nu ook een stapgrootte
print(f"De pare dagen van de week zijn : {weekdagen[0:7:2]}")
print(f"De onpare dagen van de week zijn: {weekdagen[1:7:2]}")