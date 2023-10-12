# Test met een eenvoudig voorbeeld wat de vermenigvuldigingsoperator tussen een list en een natuurlijk
# getal betekent, alsook de += operator tussen twee lists.


# colors1 = ["red", "green", "blue"]
# colors2 = ["black", "white"]



colors1 = ["rood", "blauw", "oranje"]
colors2 = ["black", "white"]

# Test met een eenvoudig voorbeeld wat de vermenigvuldigingsoperator tussen een list en een natuurlijk
# gebeurt hetzelfde met een getallen list
# met een negatief wordt de list verwijderd

nieuwe_list = colors1 * 2
print(nieuwe_list)
#of
print(f"{colors1 * 3}")

# getal betekent, alsook de += operator tussen twee lists.
# met getallen wordt dat gewoon naast geplakt
colors1 += colors2
print(f"{colors1}")