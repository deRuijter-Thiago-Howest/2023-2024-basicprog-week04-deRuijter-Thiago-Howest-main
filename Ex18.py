
#opdracht: https://leho-howest.instructure.com/courses/19316/files/3467858?module_item_id=734342


#we gebruiken 3 lists -> voor elke type werknemer een afzonderlijke list
brutowedde_arbeider = []
brutowedde_bediende = []
brutowedde_kader = []


def opvragen_weddes():
    aantal_werkenemers = int(input("Geef het aantal werkenemers op:> "))
    for index in range(0, aantal_werkenemers):
        #welk type?
        type = input("Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > ")
        #welk wedde?
        wedde = int(input("Geef het brutowedde op:> "))
        if type == "A":
            brutowedde_arbeider.append(wedde)
        elif type == "B":
            brutowedde_bediende.append(wedde)
        elif type == "K":
            brutowedde_kader.append(wedde)
        else:
            print("Ongeldige type, de wedde werd niet verwerkt.")



def print_weddes():
    print("Overzicht:")
    for wedde in brutowedde_arbeider:
        print(f"A \t {wedde}$")
    for wedde in brutowedde_bediende:
        print(f"B \t {wedde}$")
    for wedde in brutowedde_kader:
        print(f"K \t {wedde}$")


def print_totaal_overzicht():
    print(f"aantal werknemers: {len(brutowedde_arbeider) + len(brutowedde_bediende) + len(brutowedde_kader)}")
    print(f"aantal arbeiders: {len(brutowedde_arbeider)}")
    print(f"aantal bedienden: {len(brutowedde_bediende)}")
    print(f"aantal kaderpersoneel: {len(brutowedde_kader)}")
    print(f"totaal brutowedde: {sum(brutowedde_arbeider) + sum(brutowedde_bediende) + sum(brutowedde_kader)} $")

opvragen_weddes()

print_weddes()

print_totaal_overzicht()










