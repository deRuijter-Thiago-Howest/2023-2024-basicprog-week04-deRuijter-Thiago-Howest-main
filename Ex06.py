# Vraag aan de gebruiker een woord. Overloop deze string. Bewaar alle klinkers samen in één list, de
# medeklinkers in een andere list.
# Print beide lists af. Hoe zorg je ervoor dat zowel hoofdletters als kleine letters in de list terechtkomen?



# woord = input("Geef een woord op:> ")

# word = input("Enter a word:> ")


#we maken 2 lists aan waarin we resp de klinkers en medeklinkers gaan bewaren
klinkers = []
medeklinkers = []

Woord = str(input("Geef hier een woord op:> "))


#we kunnen eenvoudig de letters in een woord overlopen met de for-lus
for letter in Woord : 
    #controle: klinker, medeklinker?
    if letter == 'a' or letter == 'e' or letter == 'u' or letter == 'i' or letter == 'o':
        klinkers.append(letter)
    else:
        medeklinkers.append(letter)

print(klinkers)
print(medeklinkers)

#thuis schrijf bovenstaande code korter (efficienter)
#zorg dat de gebruiker kleine en hoofdletters door elkaar mag gebruiken